#!/usr/bin/env bash
# Build the release artifacts for handing out.
#
#   ./package.sh
#
# Produces, in dist/:
#   discovery-os-<version>.zip          the whole thing. For the installer or a manual copy
#   skills/<skill-name>.zip             one zip per skill, for platforms that take
#                                       a single skill at a time
#   CHECKSUMS.txt
#
# Attach these to a GitHub Release so the download link is stable.

set -euo pipefail
cd "$(dirname "$0")"

VERSION="$(sed -n 's/.*"version"[^"]*"\([^"]*\)".*/\1/p' .claude-plugin/plugin.json | head -1)"
OUT="dist"
rm -rf "$OUT"; mkdir -p "$OUT/skills"

echo "Discovery OS $VERSION"

# Full bundle. Excludes git, build output and OS cruft.
zip -qr "$OUT/discovery-os-$VERSION.zip" \
    .claude-plugin skills commands install.sh README.md AGENTS.md LICENSE \
    -x '*.DS_Store' -x '*__pycache__*' -x '*.pyc'
echo "  + $OUT/discovery-os-$VERSION.zip"

# One zip per skill, each containing a single top-level folder.
for d in skills/*/; do
  name="$(basename "$d")"
  ( cd skills && zip -qr "../$OUT/skills/$name.zip" "$name" \
      -x '*.DS_Store' -x '*__pycache__*' -x '*.pyc' )
  echo "  + $OUT/skills/$name.zip"
done

( cd "$OUT" && find . -name '*.zip' -print0 | sort -z | xargs -0 shasum -a 256 > CHECKSUMS.txt )
echo "  + $OUT/CHECKSUMS.txt"
echo
du -sh "$OUT"
