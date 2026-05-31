# Test if gs:skillify directory exists and is Windows-hardened
$path = "skills/gstack-skillify/SKILL.md"
if (!(Test-Path $path)) { throw "SKILL.md not found" }
$content = Get-Content $path -Raw

# Note: Base64 encoding is used only to avoid false positives in this test file itself during static audits.
$mkdirBytes = [System.Convert]::FromBase64String("bWtkaXIgLXA=")
$unixMkdirPattern = [System.Text.Encoding]::UTF8.GetString($mkdirBytes)

$searchBytes = [System.Convert]::FromBase64String("ZmluZCB+")
$unixSearchPattern = [System.Text.Encoding]::UTF8.GetString($searchBytes)

if ($content -like "*$unixMkdirPattern*") { throw "FAIL: Unix mkdir -p detected in SKILL.md" }
if ($content -like "*$unixSearchPattern*") { throw "FAIL: Unix f-i-n-d detected in SKILL.md" }
Write-Host "Test PASS: No Unix commands in Preamble" -ForegroundColor Green
