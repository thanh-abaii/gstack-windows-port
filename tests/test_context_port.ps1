$skills = @("context-save", "context-restore")
foreach ($s in $skills) {
    $path = "skills/gstack-$s/SKILL.md"
    if (!(Test-Path $path)) { throw "$s SKILL.md not found" }
    $content = Get-Content $path -Raw
    if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detected in $s" }
}
Write-Host "Test PASS: Context skills successfully hardened!" -ForegroundColor Green
