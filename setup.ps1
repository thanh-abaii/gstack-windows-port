# gstack Windows Native Port Installer
# Version: 1.1.2.1 (Added Dry-run support)

Param(
    [Parameter(Mandatory=$false)]
    [Switch]$DryRun
)

if ($DryRun) {
    Write-Host "--- [DRY-RUN MODE] ---" -ForegroundColor Yellow
    Write-Host "No changes will be made to your system.`n" -ForegroundColor Yellow
}

Write-Host "--- gstack Windows 11 Native Port Setup ---" -ForegroundColor Cyan

# 1. Check for Python 3
try {
    $pythonVer = python --version 2>$null
    if ($null -eq $pythonVer) { throw "Python not found" }
    Write-Host "[OK] Python 3 detected ($pythonVer)." -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Python 3 is required but not found in PATH." -ForegroundColor Red
    exit 1
}

# 2. Determine Skills Directory
$targetDir = Join-Path $HOME ".agents/skills"
Write-Host "[INFO] Target Directory: $targetDir" -ForegroundColor Gray

if (!(Test-Path $targetDir)) {
    if ($DryRun) {
        Write-Host "[DRY] Would create directory: $targetDir" -ForegroundColor Yellow
    } else {
        Write-Host "[INFO] Creating target directory: $targetDir"
        New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
    }
}

# 3. Copy Skills
$sourceSkills = Join-Path $PSScriptRoot "skills/*"
if ($DryRun) {
    $skillsCount = (Get-ChildItem -Path $sourceSkills -Directory).Count
    Write-Host "[DRY] Would copy $skillsCount gstack skills to $targetDir" -ForegroundColor Yellow
    Write-Host "[DRY] Actions: Copy-Item -Recurse -Force" -ForegroundColor DarkGray
} else {
    Write-Host "[INFO] Copying skills to $targetDir..." -ForegroundColor Yellow
    Copy-Item -Path $sourceSkills -Destination $targetDir -Recurse -Force
}

# 4. Final Verification
if ($DryRun) {
    Write-Host "`n--- DRY-RUN COMPLETE ---" -ForegroundColor Yellow
    Write-Host "The installation environment is ready. Run without -DryRun to install."
} else {
    Write-Host "`n--- INSTALLATION COMPLETE ---" -ForegroundColor Green
    Write-Host "You can now use gstack skills in Gemini CLI with the prefix 'gs:'."
    Write-Host "Example: /gs:health"
}

Write-Host "`nNote: This tool is for Windows only." -ForegroundColor Gray
