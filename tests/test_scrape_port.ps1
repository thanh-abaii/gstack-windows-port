# Test if gs:scrape directory exists and is Windows-hardened
$path = "skills/gstack-scrape/SKILL.md"
if (!(Test-Path $path)) { throw "SKILL.md not found" }
$content = Get-Content $path -Raw
if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detected in SKILL.md" }
if ($content -like "*wc -l*") { throw "FAIL: Unix wc -l detected in SKILL.md" }
Write-Host "Test PASS: No Unix commands in Preamble" -ForegroundColor Green
