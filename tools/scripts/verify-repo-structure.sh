
#!/usr/bin/env bash

set -euo pipefail

required_dirs=(
".github"
".artifacts"
"apps"
"assets"
"bin"
"config"
"contracts"
"data"
"db"
"docs"
"governance"
"infra"
"ops"
"packages"
"patches"
"security"
"services"
"templates"
"tools"
)

required_files=(
".github/README.md"
".artifacts/README.md"
"apps/README.md"
"assets/README.md"
"bin/README.md"
"config/README.md"
"contracts/README.md"
"data/README.md"
"db/README.md"
"docs/README.md"
"governance/README.md"
"infra/README.md"
"ops/README.md"
"packages/README.md"
"patches/README.md"
"security/README.md"
"services/README.md"
"templates/README.md"
"tools/README.md"
"docs/project/00-foundation/REPOSITORY-STRUCTURE.md"
"docs/project/06-quality/REPO-CONTRACT.md"
"docs/adr/ADR-0005-establish-root-repository-structure.md"
"tools/scripts/verify-repo-structure.sh"
)

failures=0

for dir in "${required_dirs[@]}"; do
if [[ ! -d "$dir" ]]; then
echo "Missing required directory: $dir"
failures=$((failures + 1))
fi
done

for file in "${required_files[@]}"; do
if [[ ! -f "$file" ]]; then
echo "Missing required file: $file"
failures=$((failures + 1))
fi
done

if grep -R "[https://fie.nl.tab.digital](https://fie.nl.tab.digital)" -n docs README.md tools .github apps assets bin config contracts data db governance infra ops packages patches security services templates 2>/dev/null; then
echo "Private Nextcloud URL found in tracked documentation paths."
failures=$((failures + 1))
fi

if grep -R "appliedinnovationcorp-team.atlassian.net" -n docs README.md tools .github apps assets bin config contracts data db governance infra ops packages patches security services templates 2>/dev/null; then
echo "Private Confluence URL found in tracked documentation paths."
failures=$((failures + 1))
fi

if grep -R "appliedinnovationcorp.atlassian.net" -n docs README.md tools .github apps assets bin config contracts data db governance infra ops packages patches security services templates 2>/dev/null; then
echo "Private Jira URL found in tracked documentation paths."
failures=$((failures + 1))
fi

if [[ "$failures" -ne 0 ]]; then
echo "Repository structure verification failed with $failures failure(s)."
exit 1
fi

echo "Repository structure verification passed"
