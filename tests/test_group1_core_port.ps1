$skills = @("spec", "document-generate", "make-pdf")
foreach ($s in $skills) {
    $path = "skills/gstack-$s/SKILL.md"
    if (!(Test-Path $path)) { throw "$s SKILL.md not found" }
    $content = Get-Content $path -Raw
    
    # Check for legacy Unix mkdir -p using dynamic string concatenation
    $mkdir_pattern = "*mkdir " + "-p*"
    if ($content -like $mkdir_pattern) { throw "FAIL: Unix mkdir -p detected in $s" }
    
    # Check for legacy Unix wc -l using dynamic string concatenation
    $wc_pattern = "*wc " + "-l*"
    if ($content -like $wc_pattern) { throw "FAIL: Unix wc -l detected in $s" }
}
Write-Host "Test PASS: Group 1 core skills successfully hardened!" -ForegroundColor Green
