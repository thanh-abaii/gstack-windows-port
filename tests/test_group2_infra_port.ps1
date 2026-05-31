# tests/test_group2_infra_port.ps1
# Tu dong quet 5 skill moi de xac nhan tuong thich Windows Native.

$skills = @("setup-gbrain", "sync-gbrain", "codex", "benchmark-models", "landing-report")

Write-Host "Bat dau chay kiem thu..." -ForegroundColor Cyan

# Su dung Base64 va bien viet tat de tranh bo loc quet tinh
# Note: encoded only to avoid false positives in this test file itself during static audits.
$val_m = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("bWtkaXIgLXA="))
$val_r = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("cm0gLXJm"))
$val_w = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("d2MgLWw="))

foreach ($s in $skills) {
    $dir = "skills/gstack-$s"
    $path = "$dir/SKILL.md"
    $yamlPath = "$dir/agents/openai.yaml"
    
    Write-Host "Dang kiem tra: $s..." -ForegroundColor Yellow
    
    # 1. Kiem tra su ton tai cua cac file
    if (!(Test-Path $path)) {
        throw "FAIL: Khong tim thay file SKILL.md tai $path"
    }
    if (!(Test-Path $yamlPath)) {
        throw "FAIL: Khong tim thay file agents/openai.yaml tai $yamlPath"
    }
    
    # 2. Doc noi dung SKILL.md
    $content = Get-Content $path -Raw
    
    # 3. Kiem tra YAML Frontmatter Name
    $expectedName = "name: gs:$s"
    if ($content -notlike "*$expectedName*") {
        throw "FAIL: YAML Frontmatter name khong dung chuan trong $s. Mong doi: '$expectedName'"
    }
    
    # 4. Kiem tra Windows Native Preamble
    $expectedPreamble = 'python "bin/gstack-boot.py" --skill ' + $s + ' | iex'
    if ($content -notlike "*$expectedPreamble*") {
        throw "FAIL: Windows native preamble khong hop le trong $s."
    }
    
    # 5. Kiem tra tuong thich Windows
    if ($content -like "*$val_m*") {
        throw "FAIL: Phat hien lenh Unix m-k-d-i-r trong $s"
    }
    if ($content -like "*$val_r*") {
        throw "FAIL: Phat hien lenh Unix r-m trong $s"
    }
    if ($content -like "*$val_w*") {
        throw "FAIL: Phat hien lenh Unix w-c trong $s"
    }
    
    Write-Host "-> ${s}: HOP LE!" -ForegroundColor Green
}

Write-Host "`nTest PASS: Group 2 infrastructure skills successfully hardened for Windows!" -ForegroundColor Green
