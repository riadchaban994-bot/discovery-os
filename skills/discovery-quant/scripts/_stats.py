"""
Minimal statistics helpers with no hard dependency on scipy.

Everything here is implemented from standard numerical recipes so the discovery
scripts run on a plain Python install. numpy is used when available for speed and
for Monte Carlo, but is optional except where noted.

Accuracy notes:
  - norm_cdf uses math.erf and is accurate to machine precision.
  - norm_ppf uses Acklam's rational approximation with one Halley refinement:
    absolute error below 1e-9 across the usable range.
  - t_cdf uses the regularised incomplete beta function (continued fraction),
    accurate to ~1e-10. Falls back to the normal approximation above df=2000
    where the difference is below display precision anyway.
"""

import math

# --------------------------------------------------------------------------
# Normal distribution
# --------------------------------------------------------------------------


def norm_cdf(x):
    """P(Z <= x) for standard normal."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_sf(x):
    """P(Z > x)."""
    return 1.0 - norm_cdf(x)


_A = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
      1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
_B = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
      6.680131188771972e+01, -1.328068155288572e+01]
_C = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
      -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
_D = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
      3.754408661907416e+00]


def norm_ppf(p):
    """Inverse standard normal CDF. Acklam's algorithm plus one Halley step."""
    if not 0.0 < p < 1.0:
        raise ValueError("norm_ppf requires 0 < p < 1, got %r" % (p,))
    plow, phigh = 0.02425, 1.0 - 0.02425
    if p < plow:
        q = math.sqrt(-2.0 * math.log(p))
        x = (((((_C[0] * q + _C[1]) * q + _C[2]) * q + _C[3]) * q + _C[4]) * q + _C[5]) / \
            ((((_D[0] * q + _D[1]) * q + _D[2]) * q + _D[3]) * q + 1.0)
    elif p > phigh:
        q = math.sqrt(-2.0 * math.log(1.0 - p))
        x = -(((((_C[0] * q + _C[1]) * q + _C[2]) * q + _C[3]) * q + _C[4]) * q + _C[5]) / \
            ((((_D[0] * q + _D[1]) * q + _D[2]) * q + _D[3]) * q + 1.0)
    else:
        q = p - 0.5
        r = q * q
        x = (((((_A[0] * r + _A[1]) * r + _A[2]) * r + _A[3]) * r + _A[4]) * r + _A[5]) * q / \
            (((((_B[0] * r + _B[1]) * r + _B[2]) * r + _B[3]) * r + _B[4]) * r + 1.0)
    # Halley refinement
    e = norm_cdf(x) - p
    u = e * math.sqrt(2.0 * math.pi) * math.exp(x * x / 2.0)
    x = x - u / (1.0 + x * u / 2.0)
    return x


# --------------------------------------------------------------------------
# Incomplete beta -> Student t
# --------------------------------------------------------------------------


def _betacf(a, b, x, itmax=300, eps=3.0e-12):
    """Continued fraction for the incomplete beta function (Lentz's method)."""
    tiny = 1.0e-30
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < tiny:
        d = tiny
    d = 1.0 / d
    h = d
    for m in range(1, itmax + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < tiny:
            d = tiny
        c = 1.0 + aa / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        de = d * c
        h *= de
        if abs(de - 1.0) < eps:
            break
    return h


def betainc(a, b, x):
    """Regularised incomplete beta I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = (math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
             + a * math.log(x) + b * math.log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return math.exp(lbeta) * _betacf(a, b, x) / a
    return 1.0 - math.exp(lbeta) * _betacf(b, a, 1.0 - x) / b


def t_sf(t, df):
    """P(T > t) for Student's t with df degrees of freedom."""
    if df > 2000:
        return norm_sf(t)
    x = df / (df + t * t)
    p = 0.5 * betainc(df / 2.0, 0.5, x)
    return p if t > 0 else 1.0 - p


def t_two_sided_p(t, df):
    return 2.0 * t_sf(abs(t), df)


# --------------------------------------------------------------------------
# Chi-square (1 df exact, general via series)
# --------------------------------------------------------------------------


def _lower_gamma_reg(s, x, itmax=500, eps=1e-14):
    """Regularised lower incomplete gamma P(s, x)."""
    if x < 0 or s <= 0:
        raise ValueError("bad args to lower gamma")
    if x == 0:
        return 0.0
    if x < s + 1.0:
        ap, total, delta = s, 1.0 / s, 1.0 / s
        for _ in range(itmax):
            ap += 1.0
            delta *= x / ap
            total += delta
            if abs(delta) < abs(total) * eps:
                break
        return total * math.exp(-x + s * math.log(x) - math.lgamma(s))
    # continued fraction for Q, then complement
    tiny = 1e-300
    b = x + 1.0 - s
    c = 1.0 / tiny
    d = 1.0 / b
    h = d
    for i in range(1, itmax + 1):
        an = -i * (i - s)
        b += 2.0
        d = an * d + b
        if abs(d) < tiny:
            d = tiny
        c = b + an / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        de = d * c
        h *= de
        if abs(de - 1.0) < eps:
            break
    q = math.exp(-x + s * math.log(x) - math.lgamma(s)) * h
    return 1.0 - q


def chi2_sf(x, df):
    """P(X > x) for chi-square with df degrees of freedom."""
    if x <= 0:
        return 1.0
    if df == 1:  # exact: chi2(1) = Z^2
        return 2.0 * norm_sf(math.sqrt(x))
    return 1.0 - _lower_gamma_reg(df / 2.0, x / 2.0)


# --------------------------------------------------------------------------
# Proportions
# --------------------------------------------------------------------------


def two_proportion_z(x1, n1, x2, n2):
    """Pooled two-sided z-test for two proportions.

    Returns (p1, p2, diff, z, p_value).
    """
    if n1 <= 0 or n2 <= 0:
        raise ValueError("group sizes must be positive")
    p1, p2 = x1 / n1, x2 / n2
    pooled = (x1 + x2) / (n1 + n2)
    se = math.sqrt(pooled * (1.0 - pooled) * (1.0 / n1 + 1.0 / n2))
    if se == 0:
        return p1, p2, p2 - p1, 0.0, 1.0
    z = (p2 - p1) / se
    return p1, p2, p2 - p1, z, 2.0 * norm_sf(abs(z))


def diff_ci(x1, n1, x2, n2, alpha=0.05):
    """Wald confidence interval on the absolute difference p2 - p1.

    Approximate. With fewer than ~10 events in a group prefer an exact method.
    """
    p1, p2 = x1 / n1, x2 / n2
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    z = norm_ppf(1.0 - alpha / 2.0)
    d = p2 - p1
    return d - z * se, d + z * se


def wilson_ci(x, n, alpha=0.05):
    """Wilson score interval for a single proportion. Well behaved at small n."""
    if n == 0:
        return (0.0, 1.0)
    z = norm_ppf(1.0 - alpha / 2.0)
    p = x / n
    denom = 1.0 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return max(0.0, centre - half), min(1.0, centre + half)


# --------------------------------------------------------------------------
# Means
# --------------------------------------------------------------------------


def welch_t(m1, s1, n1, m2, s2, n2):
    """Welch's unequal-variance t-test. Returns (t, df, p_two_sided)."""
    v1, v2 = s1 * s1 / n1, s2 * s2 / n2
    se = math.sqrt(v1 + v2)
    if se == 0:
        return 0.0, float(n1 + n2 - 2), 1.0
    t = (m2 - m1) / se
    df = (v1 + v2) ** 2 / (v1 * v1 / (n1 - 1) + v2 * v2 / (n2 - 1))
    return t, df, t_two_sided_p(t, df)


# --------------------------------------------------------------------------
# Multiple comparisons
# --------------------------------------------------------------------------


def bonferroni(pvals, alpha=0.05):
    m = len(pvals)
    return [(p, p * m <= alpha) for p in pvals]


def benjamini_hochberg(pvals, alpha=0.05):
    """Returns list of (original_index, p, adjusted_p, reject) sorted by index."""
    m = len(pvals)
    order = sorted(range(m), key=lambda i: pvals[i])
    adj = [0.0] * m
    prev = 1.0
    for rank in range(m, 0, -1):
        i = order[rank - 1]
        val = min(prev, pvals[i] * m / rank)
        adj[i] = val
        prev = val
    return [(i, pvals[i], adj[i], adj[i] <= alpha) for i in range(m)]


def fmt_p(p):
    if p < 1e-4:
        return "<0.0001"
    return "%.4f" % p
