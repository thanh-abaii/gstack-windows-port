# 🛡️ gstack Maintainer Audit Report

This automated report scans active files for Windows 11 compatibility issues, Bashisms, Unix-specific behaviors, and hardcoded security secrets.

> [!WARNING]
> **AUDIT ALERT:** Detected **2517 potential issues** in the workspace that could impact Windows 11 compatibility or repository security.

## 📊 Summary of Findings

| File Path | Bashisms | Hardcoded Unix Paths | Hardcoded Secrets | Line Endings (CRLF) | Total Issues |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `CONTRIBUTING.md` | 3 | 0 | 0 | ✅ CRLF | **3** |
| `docs\plans\2026-05-31-port-group-1-and-2-skills.md` | 4 | 0 | 0 | ✅ CRLF | **4** |
| `docs\plans\2026-05-31-port-new-gstack-skills.md` | 2 | 0 | 0 | ✅ CRLF | **2** |
| `docs\solution-architecture.md` | 1 | 1 | 0 | ✅ CRLF | **2** |
| `reports\maintainer_audit_report.md` | 1801 | 202 | 0 | ✅ CRLF | **2003** |
| `skills\gstack-autoplan\SKILL.md` | 10 | 0 | 0 | ✅ CRLF | **10** |
| `skills\gstack-benchmark\SKILL.md` | 2 | 0 | 0 | ✅ CRLF | **2** |
| `skills\gstack-browse\SKILL.md` | 2 | 2 | 0 | ✅ CRLF | **4** |
| `skills\gstack-canary\SKILL.md` | 7 | 0 | 0 | ✅ CRLF | **7** |
| `skills\gstack-careful\SKILL.md` | 5 | 1 | 0 | ✅ CRLF | **6** |
| `skills\gstack-checkpoint\SKILL.md` | 6 | 0 | 0 | ✅ CRLF | **6** |
| `skills\gstack-context-restore\SKILL.md` | 11 | 0 | 0 | ✅ CRLF | **11** |
| `skills\gstack-context-save\SKILL.md` | 10 | 0 | 0 | ✅ CRLF | **10** |
| `skills\gstack-cso\SKILL.md` | 33 | 0 | 0 | ✅ CRLF | **33** |
| `skills\gstack-design-consultation\SKILL.md` | 15 | 1 | 0 | ✅ CRLF | **16** |
| `skills\gstack-design-html\SKILL.md` | 13 | 2 | 0 | ✅ CRLF | **15** |
| `skills\gstack-design-review\SKILL.md` | 13 | 1 | 0 | ✅ CRLF | **14** |
| `skills\gstack-design-shotgun\SKILL.md` | 14 | 10 | 0 | ✅ CRLF | **24** |
| `skills\gstack-devex-review\SKILL.md` | 10 | 0 | 0 | ✅ CRLF | **10** |
| `skills\gstack-document-generate\SKILL.md` | 10 | 0 | 0 | ✅ CRLF | **10** |
| `skills\gstack-document-release\SKILL.md` | 7 | 1 | 0 | ✅ CRLF | **8** |
| `skills\gstack-freeze\SKILL.md` | 1 | 0 | 0 | ✅ CRLF | **1** |
| `skills\gstack-guard\SKILL.md` | 3 | 0 | 0 | ✅ CRLF | **3** |
| `skills\gstack-health\SKILL.md` | 10 | 0 | 0 | ✅ CRLF | **10** |
| `skills\gstack-investigate\SKILL.md` | 4 | 0 | 0 | ✅ CRLF | **4** |
| `skills\gstack-land-and-deploy\SKILL.md` | 31 | 0 | 0 | ✅ CRLF | **31** |
| `skills\gstack-learn\SKILL.md` | 5 | 0 | 0 | ✅ CRLF | **5** |
| `skills\gstack-maintainer-auditor\SKILL.md` | 2 | 0 | 0 | ✅ CRLF | **2** |
| `skills\gstack-make-pdf\SKILL.md` | 3 | 3 | 0 | ✅ CRLF | **6** |
| `skills\gstack-office-hours\SKILL.md` | 15 | 1 | 0 | ✅ CRLF | **16** |
| `skills\gstack-open-gstack-browser\SKILL.md` | 10 | 0 | 0 | ✅ CRLF | **10** |
| `skills\gstack-pair-agent\SKILL.md` | 8 | 0 | 0 | ✅ CRLF | **8** |
| `skills\gstack-plan-ceo-review\SKILL.md` | 11 | 0 | 0 | ✅ CRLF | **11** |
| `skills\gstack-plan-design-review\SKILL.md` | 9 | 1 | 0 | ✅ CRLF | **10** |
| `skills\gstack-plan-devex-review\SKILL.md` | 14 | 0 | 0 | ✅ CRLF | **14** |
| `skills\gstack-plan-eng-review\SKILL.md` | 10 | 0 | 0 | ✅ CRLF | **10** |
| `skills\gstack-plan-tune\SKILL.md` | 4 | 0 | 0 | ✅ CRLF | **4** |
| `skills\gstack-qa-only\SKILL.md` | 7 | 1 | 0 | ✅ CRLF | **8** |
| `skills\gstack-qa\SKILL.md` | 15 | 1 | 0 | ✅ CRLF | **16** |
| `skills\gstack-retro\SKILL.md` | 20 | 1 | 0 | ✅ CRLF | **21** |
| `skills\gstack-review\SKILL.md` | 11 | 0 | 0 | ✅ CRLF | **11** |
| `skills\gstack-scrape\SKILL.md` | 6 | 0 | 0 | ✅ CRLF | **6** |
| `skills\gstack-setup-browser-cookies\SKILL.md` | 3 | 0 | 0 | ✅ CRLF | **3** |
| `skills\gstack-setup-deploy\SKILL.md` | 14 | 0 | 0 | ✅ CRLF | **14** |
| `skills\gstack-ship\SKILL.md` | 39 | 0 | 0 | ✅ CRLF | **39** |
| `skills\gstack-skillify\SKILL.md` | 2 | 0 | 0 | ✅ CRLF | **2** |
| `skills\gstack-spec\SKILL.md` | 16 | 4 | 0 | ✅ CRLF | **20** |
| `skills\gstack-unfreeze\SKILL.md` | 1 | 0 | 0 | ✅ CRLF | **1** |
| `skills\gstack-upgrade\SKILL.md` | 7 | 0 | 0 | ✅ CRLF | **7** |
| `skills\gstack\SKILL.md` | 3 | 2 | 0 | ✅ CRLF | **5** |
| `skills\gstack\gstack-upgrade\SKILL.md` | 7 | 0 | 0 | ✅ CRLF | **7** |
| `skills\gstack\review\checklist.md` | 2 | 0 | 0 | ✅ CRLF | **2** |
| `skills\gstack\review\design-checklist.md` | 1 | 0 | 0 | ✅ CRLF | **1** |
| `tests\test_context_port.ps1` | 1 | 0 | 0 | ⚠️ LF only | **2** |
| `tests\test_group1_core_port.ps1` | 1 | 0 | 0 | ⚠️ LF only | **2** |
| `tests\test_group2_infra_port.ps1` | 0 | 0 | 0 | ⚠️ LF only | **1** |
| `tests\test_scrape_port.ps1` | 1 | 0 | 0 | ⚠️ LF only | **2** |
| `tests\test_skillify_port.ps1` | 1 | 0 | 0 | ⚠️ LF only | **2** |

## 🔍 Detailed Breakdown

### 📂 `CONTRIBUTING.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like `ls`, `grep`, `cat`, ` | Unix force-remove command (use PowerShell equivalent) |
| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like `ls`, `grep`, `cat`, ` | Unix text processing utilities (use PowerShell or Python) |
| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like `ls`, `grep`, `cat`, ` | Unix command (use PowerShell equivalent) |

---

### 📂 `docs\plans\2026-05-31-port-group-1-and-2-skills.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L82` | `Also, sanitize any Unix commands (like `mkdir -p` or `find`) in their instructio` | Unix nested directory creation (use PowerShell equivalent) |
| `L92` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detected in $s" }` | Unix nested directory creation (use PowerShell equivalent) |
| `L155` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detected in $s" }` | Unix nested directory creation (use PowerShell equivalent) |
| `L208` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detected in $s" }` | Unix nested directory creation (use PowerShell equivalent) |

---

### 📂 `docs\plans\2026-05-31-port-new-gstack-skills.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L76` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detected in SKILL.` | Unix nested directory creation (use PowerShell equivalent) |
| `L150` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detected in SKILL.` | Unix nested directory creation (use PowerShell equivalent) |

---

### 📂 `docs\solution-architecture.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L22` | `37 kỹ năng gốc của hệ sinh thái `gstack` được thiết kế cho môi trường Unix (Bash` | Unix text processing utilities (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L22` | `37 kỹ năng gốc của hệ sinh thái `gstack` được thiết kế cho môi trường Unix (Bash` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `reports\maintainer_audit_report.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L76` | `| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like `ls`, `gre` | Unix text processing utilities (use PowerShell or Python) |
| `L76` | `| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like `ls`, `gre` | Unix command (use PowerShell equivalent) |
| `L77` | `| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like `ls`, `gre` | Unix text processing utilities (use PowerShell or Python) |
| `L77` | `| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like `ls`, `gre` | Unix command (use PowerShell equivalent) |
| `L78` | `| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like `ls`, `gre` | Unix text processing utilities (use PowerShell or Python) |
| `L78` | `| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like `ls`, `gre` | Unix command (use PowerShell equivalent) |
| `L86` | `| `L76` | `| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like` | Unix command (use PowerShell equivalent) |
| `L87` | `| `L76` | `| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like` | Unix command (use PowerShell equivalent) |
| `L88` | `| `L77` | `| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like` | Unix command (use PowerShell equivalent) |
| `L89` | `| `L77` | `| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like` | Unix command (use PowerShell equivalent) |
| `L90` | `| `L78` | `| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like` | Unix command (use PowerShell equivalent) |
| `L91` | `| `L78` | `| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like` | Unix command (use PowerShell equivalent) |
| `L98` | `| `L98` | `| `L83` | `| `L85` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L99` | `| `L99` | `| `L84` | `| `L86` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\` | Unix text processing utilities (use PowerShell or Python) |
| `L100` | `| `L101` | `| `L86` | `| `L89` | `| `L759` | `DESIGN=$(ls -t ~/.gstack/projects/` | Unix command (use PowerShell equivalent) |
| `L101` | `| `L102` | `| `L87` | `| `L90` | `| `L760` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ` | Unix command (use PowerShell equivalent) |
| `L102` | `| `L103` | `| `L88` | `| `L91` | `| `L922` | `- Discover design docs: `ls -t ~/.` | Unix command (use PowerShell equivalent) |
| `L103` | `| `L104` | `| `L89` | `| `L92` | `| `L923` | `- Detect UI scope: grep the plan f` | Unix text processing utilities (use PowerShell or Python) |
| `L104` | `| `L105` | `| `L90` | `| `L93` | `| `L926` | `- Detect DX scope: grep the plan f` | Unix text processing utilities (use PowerShell or Python) |
| `L105` | `| `L106` | `| `L91` | `| `L101` | `| `L410` | `curl -fsSL "https://bun.sh/instal` | Unix network tools (use PowerShell or Python) |
| `L106` | `| `L107` | `| `L92` | `| `L102` | `| `L411` | `actual_sha=$(shasum -a 256 "$tmpf` | Unix text processing utilities (use PowerShell or Python) |
| `L107` | `| `L108` | `| `L93` | `| `L110` | `| `L412` | `curl -fsSL "https://bun.sh/instal` | Unix network tools (use PowerShell or Python) |
| `L108` | `| `L109` | `| `L94` | `| `L111` | `| `L413` | `actual_sha=$(shasum -a 256 "$tmpf` | Unix text processing utilities (use PowerShell or Python) |
| `L109` | `| `L110` | `| `L95` | `| `L126` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BRA` | Unix text processing utilities (use PowerShell or Python) |
| `L110` | `| `L111` | `| `L96` | `| `L127` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\"` | Unix text processing utilities (use PowerShell or Python) |
| `L111` | `| `L112` | `| `L97` | `| `L129` | `| `L666` | `curl -fsSL "https://bun.sh/instal` | Unix network tools (use PowerShell or Python) |
| `L112` | `| `L113` | `| `L98` | `| `L130` | `| `L667` | `actual_sha=$(shasum -a 256 "$tmpf` | Unix text processing utilities (use PowerShell or Python) |
| `L113` | `| `L116` | `| `L101` | `| `L141` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L114` | `| `L117` | `| `L102` | `| `L142` | `| `L60` | `| `docker rm -f` / `docker system` | Unix force-remove command (use PowerShell equivalent) |
| `L115` | `| `L118` | `| `L103` | `| `L143` | `| `L65` | `- `rm -rf node_modules` / `.next`` | Unix force-remove command (use PowerShell equivalent) |
| `L116` | `| `L119` | `| `L104` | `| `L148` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L117` | `| `L120` | `| `L105` | `| `L157` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L118` | `| `L121` | `| `L106` | `| `L158` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L119` | `| `L122` | `| `L109` | `| `L170` | `| `L294` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L120` | `| `L123` | `| `L110` | `| `L171` | `| `L297` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L121` | `| `L124` | `| `L111` | `| `L174` | `| `L700` | `ls package.json tsconfig.json | ` | Unix command (use PowerShell equivalent) |
| `L122` | `| `L125` | `| `L112` | `| `L175` | `| `L701` | `ls Gemfile | Out-Null ; echo "ST` | Unix command (use PowerShell equivalent) |
| `L123` | `| `L126` | `| `L113` | `| `L176` | `| `L702` | `ls requirements.txt pyproject.to` | Unix command (use PowerShell equivalent) |
| `L124` | `| `L127` | `| `L114` | `| `L177` | `| `L703` | `ls go.mod | Out-Null ; echo "STA` | Unix command (use PowerShell equivalent) |
| `L125` | `| `L128` | `| `L115` | `| `L178` | `| `L704` | `ls Cargo.toml | Out-Null ; echo ` | Unix command (use PowerShell equivalent) |
| `L126` | `| `L129` | `| `L116` | `| `L179` | `| `L705` | `ls pom.xml build.gradle | Out-Nu` | Unix command (use PowerShell equivalent) |
| `L127` | `| `L130` | `| `L117` | `| `L180` | `| `L706` | `ls composer.json | Out-Null ; ec` | Unix command (use PowerShell equivalent) |
| `L128` | `| `L131` | `| `L119` | `| `L182` | `| `L712` | `grep -q "next" package.json | Ou` | Unix text processing utilities (use PowerShell or Python) |
| `L129` | `| `L132` | `| `L120` | `| `L183` | `| `L713` | `grep -q "express" package.json |` | Unix text processing utilities (use PowerShell or Python) |
| `L130` | `| `L133` | `| `L121` | `| `L184` | `| `L714` | `grep -q "fastify" package.json |` | Unix text processing utilities (use PowerShell or Python) |
| `L131` | `| `L134` | `| `L122` | `| `L185` | `| `L715` | `grep -q "hono" package.json | Ou` | Unix text processing utilities (use PowerShell or Python) |
| `L132` | `| `L135` | `| `L123` | `| `L186` | `| `L716` | `grep -q "django" requirements.tx` | Unix text processing utilities (use PowerShell or Python) |
| `L133` | `| `L136` | `| `L124` | `| `L187` | `| `L717` | `grep -q "fastapi" requirements.t` | Unix text processing utilities (use PowerShell or Python) |
| `L134` | `| `L137` | `| `L125` | `| `L188` | `| `L718` | `grep -q "flask" requirements.txt` | Unix text processing utilities (use PowerShell or Python) |
| `L135` | `| `L138` | `| `L126` | `| `L189` | `| `L719` | `grep -q "rails" Gemfile | Out-Nu` | Unix text processing utilities (use PowerShell or Python) |
| `L136` | `| `L139` | `| `L127` | `| `L190` | `| `L720` | `grep -q "gin-gonic" go.mod | Out` | Unix text processing utilities (use PowerShell or Python) |
| `L137` | `| `L140` | `| `L128` | `| `L191` | `| `L721` | `grep -q "spring-boot" pom.xml bu` | Unix text processing utilities (use PowerShell or Python) |
| `L138` | `| `L141` | `| `L129` | `| `L192` | `| `L722` | `grep -q "laravel" composer.json ` | Unix text processing utilities (use PowerShell or Python) |
| `L139` | `| `L142` | `| `L130` | `| `L193` | `| `L759` | `ls .env .env.* | Out-Null` | Uni` | Unix command (use PowerShell equivalent) |
| `L140` | `| `L143` | `| `L131` | `| `L194` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L141` | `| `L143` | `| `L131` | `| `L194` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L142` | `| `L144` | `| `L131` | `| `L194` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L143` | `| `L144` | `| `L131` | `| `L194` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L144` | `| `L145` | `| `L132` | `| `L194` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L145` | `| `L145` | `| `L132` | `| `L194` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L146` | `| `L146` | `| `L132` | `| `L194` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L147` | `| `L146` | `| `L132` | `| `L194` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L148` | `| `L147` | `| `L133` | `| `L195` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L149` | `| `L147` | `| `L133` | `| `L195` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L150` | `| `L148` | `| `L133` | `| `L195` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L151` | `| `L148` | `| `L133` | `| `L195` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L152` | `| `L149` | `| `L134` | `| `L195` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L153` | `| `L149` | `| `L134` | `| `L195` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L154` | `| `L150` | `| `L134` | `| `L195` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L155` | `| `L150` | `| `L134` | `| `L195` | `| `L800` | `git ls-files '*.env' '.env.*' | ` | Unix command (use PowerShell equivalent) |
| `L156` | `| `L151` | `| `L135` | `| `L196` | `| `L801` | `grep -q "^\.env$\|^\.env\.\*" .g` | Unix text processing utilities (use PowerShell or Python) |
| `L157` | `| `L152` | `| `L136` | `| `L197` | `| `L807` | `[ -f "$f" ] ; grep -n "password:` | Unix text processing utilities (use PowerShell or Python) |
| `L158` | `| `L153` | `| `L137` | `| `L198` | `| `L896` | `**Key checks (beyond grep):**` |` | Unix text processing utilities (use PowerShell or Python) |
| `L159` | `| `L154` | `| `L138` | `| `L199` | `| `L914` | `ls -la .agents/skills/ | Out-Nul` | Unix command (use PowerShell equivalent) |
| `L160` | `| `L155` | `| `L139` | `| `L200` | `| `L918` | `- `curl`, `wget`, `fetch`, `http` | Unix network tools (use PowerShell or Python) |
| `L161` | `| `L156` | `| `L140` | `| `L210` | `| `L288` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L162` | `| `L157` | `| `L141` | `| `L211` | `| `L291` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L163` | `| `L158` | `| `L142` | `| `L213` | `| `L679` | `ls DESIGN.md design-system.md | ` | Unix command (use PowerShell equivalent) |
| `L164` | `| `L159` | `| `L143` | `| `L214` | `| `L688` | `cat README.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L165` | `| `L160` | `| `L144` | `| `L215` | `| `L689` | `cat package.json | Out-Null | he` | Unix command (use PowerShell equivalent) |
| `L166` | `| `L161` | `| `L145` | `| `L216` | `| `L690` | `ls src/ app/ pages/ components/ ` | Unix command (use PowerShell equivalent) |
| `L167` | `| `L162` | `| `L146` | `| `L217` | `| `L698` | `ls ~/.gstack/projects/$SLUG/*off` | Unix command (use PowerShell equivalent) |
| `L168` | `| `L163` | `| `L147` | `| `L218` | `| `L699` | `ls .context/*office-hours* .cont` | Unix command (use PowerShell equivalent) |
| `L169` | `| `L164` | `| `L148` | `| `L219` | `| `L731` | `curl -fsSL "https://bun.sh/insta` | Unix network tools (use PowerShell or Python) |
| `L170` | `| `L165` | `| `L149` | `| `L220` | `| `L732` | `actual_sha=$(shasum -a 256 "$tmp` | Unix text processing utilities (use PowerShell or Python) |
| `L171` | `| `L166` | `| `L150` | `| `L221` | `| `L1045` | `cat "$_DESIGN_DIR/feedback.json` | Unix command (use PowerShell equivalent) |
| `L172` | `| `L167` | `| `L151` | `| `L222` | `| `L1048` | `cat "$_DESIGN_DIR/feedback-pend` | Unix command (use PowerShell equivalent) |
| `L173` | `| `L168` | `| `L152` | `| `L223` | `| `L1077` | ``curl -s -X POST http://127.0.0` | Unix network tools (use PowerShell or Python) |
| `L174` | `| `L169` | `| `L153` | `| `L237` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L175` | `| `L170` | `| `L154` | `| `L238` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L176` | `| `L171` | `| `L155` | `| `L240` | `| `L811` | `curl -fsSL "https://bun.sh/insta` | Unix network tools (use PowerShell or Python) |
| `L177` | `| `L172` | `| `L156` | `| `L241` | `| `L812` | `actual_sha=$(shasum -a 256 "$tmp` | Unix text processing utilities (use PowerShell or Python) |
| `L178` | `| `L173` | `| `L157` | `| `L242` | `| `L836` | `_CEO=$(ls -t ~/.gstack/projects/` | Unix command (use PowerShell equivalent) |
| `L179` | `| `L174` | `| `L158` | `| `L243` | `| `L842` | `_APPROVED=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L180` | `| `L175` | `| `L159` | `| `L244` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L181` | `| `L176` | `| `L160` | `| `L245` | `| `L854` | `_FINALIZED=$(ls -t ~/.gstack/pro` | Unix command (use PowerShell equivalent) |
| `L182` | `| `L177` | `| `L161` | `| `L246` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L183` | `| `L177` | `| `L161` | `| `L246` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L184` | `| `L178` | `| `L161` | `| `L246` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L185` | `| `L178` | `| `L161` | `| `L246` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L186` | `| `L179` | `| `L162` | `| `L246` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L187` | `| `L179` | `| `L162` | `| `L246` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L188` | `| `L180` | `| `L162` | `| `L246` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L189` | `| `L180` | `| `L162` | `| `L246` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L190` | `| `L181` | `| `L163` | `| `L247` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L191` | `| `L181` | `| `L163` | `| `L247` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L192` | `| `L182` | `| `L163` | `| `L247` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L193` | `| `L182` | `| `L163` | `| `L247` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L194` | `| `L183` | `| `L164` | `| `L247` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L195` | `| `L183` | `| `L164` | `| `L247` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L196` | `| `L184` | `| `L164` | `| `L247` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L197` | `| `L184` | `| `L164` | `| `L247` | `| `L979` | `[ -f package.json ] ; cat packag` | Unix command (use PowerShell equivalent) |
| `L198` | `| `L185` | `| `L165` | `| `L248` | `| `L1226` | `_PORT=$(lsof -i -P -n | grep "$` | Unix text processing utilities (use PowerShell or Python) |
| `L199` | `| `L186` | `| `L166` | `| `L254` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L200` | `| `L187` | `| `L167` | `| `L263` | `| `L288` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L201` | `| `L188` | `| `L168` | `| `L264` | `| `L291` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L202` | `| `L189` | `| `L169` | `| `L266` | `| `L689` | `$B status | Out-Null | grep -q "` | Unix text processing utilities (use PowerShell or Python) |
| `L203` | `| `L190` | `| `L170` | `| `L267` | `| `L740` | `curl -fsSL "https://bun.sh/insta` | Unix network tools (use PowerShell or Python) |
| `L204` | `| `L191` | `| `L171` | `| `L268` | `| `L741` | `actual_sha=$(shasum -a 256 "$tmp` | Unix text processing utilities (use PowerShell or Python) |
| `L205` | `| `L192` | `| `L172` | `| `L269` | `| `L770` | `[ -f Gemfile ] ; grep -q "rails"` | Unix text processing utilities (use PowerShell or Python) |
| `L206` | `| `L193` | `| `L173` | `| `L270` | `| `L771` | `[ -f package.json ] ; grep -q '"` | Unix text processing utilities (use PowerShell or Python) |
| `L207` | `| `L194` | `| `L174` | `| `L271` | `| `L773` | `ls jest.config.* vitest.config.*` | Unix command (use PowerShell equivalent) |
| `L208` | `| `L195` | `| `L175` | `| `L272` | `| `L774` | `ls -d test/ tests/ spec/ __tests` | Unix command (use PowerShell equivalent) |
| `L209` | `| `L196` | `| `L176` | `| `L273` | `| `L859` | `ls -d .github/ | Out-Null ; echo` | Unix command (use PowerShell equivalent) |
| `L210` | `| `L197` | `| `L177` | `| `L274` | `| `L860` | `ls .gitlab-ci.yml .circleci/ bit` | Unix command (use PowerShell equivalent) |
| `L211` | `| `L198` | `| `L178` | `| `L288` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L212` | `| `L199` | `| `L179` | `| `L289` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L213` | `| `L200` | `| `L180` | `| `L291` | `| `L829` | `cat DESIGN.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L214` | `| `L201` | `| `L181` | `| `L292` | `| `L833` | `ls src/ app/ pages/ components/ ` | Unix command (use PowerShell equivalent) |
| `L215` | `| `L202` | `| `L182` | `| `L293` | `| `L838` | `ls ~/.gstack/projects/$SLUG/*off` | Unix command (use PowerShell equivalent) |
| `L216` | `| `L203` | `| `L183` | `| `L294` | `| `L848` | `curl -s -o $null -w "%{http_code` | Unix network tools (use PowerShell or Python) |
| `L217` | `| `L204` | `| `L184` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L218` | `| `L205` | `| `L185` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L219` | `| `L206` | `| `L186` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L220` | `| `L207` | `| `L187` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L221` | `| `L208` | `| `L188` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L222` | `| `L209` | `| `L189` | `| `L298` | `| `L1043` | `cat "$_DESIGN_DIR/feedback.json` | Unix command (use PowerShell equivalent) |
| `L223` | `| `L210` | `| `L190` | `| `L299` | `| `L1046` | `cat "$_DESIGN_DIR/feedback-pend` | Unix command (use PowerShell equivalent) |
| `L224` | `| `L211` | `| `L191` | `| `L300` | `| `L1075` | ``curl -s -X POST http://127.0.0` | Unix network tools (use PowerShell or Python) |
| `L225` | `| `L212` | `| `L192` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L226` | `| `L213` | `| `L193` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L227` | `| `L214` | `| `L194` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L228` | `| `L215` | `| `L195` | `| `L323` | `| `L292` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L229` | `| `L216` | `| `L196` | `| `L324` | `| `L295` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L230` | `| `L218` | `| `L198` | `| `L327` | `| `L732` | `curl -fsSL "https://bun.sh/insta` | Unix network tools (use PowerShell or Python) |
| `L231` | `| `L219` | `| `L199` | `| `L328` | `| `L733` | `actual_sha=$(shasum -a 256 "$tmp` | Unix text processing utilities (use PowerShell or Python) |
| `L233` | `| `L221` | `| `L201` | `| `L331` | `| `L903` | `- Deprecation warnings in code (` | Unix text processing utilities (use PowerShell or Python) |
| `L234` | `| `L222` | `| `L202` | `| `L340` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L235` | `| `L223` | `| `L203` | `| `L341` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L236` | `| `L225` | `| `L205` | `| `L344` | `| `L939` | `git commit -m "$(cat <<'EOF'` | ` | Unix command (use PowerShell equivalent) |
| `L237` | `| `L226` | `| `L206` | `| `L345` | `| `L984` | `glab mr update -d "$(cat <<'MRBO` | Unix command (use PowerShell equivalent) |
| `L238` | `| `L227` | `| `L207` | `| `L366` | `| `L6` | `Combines /gs:careful (warns before` | Unix force-remove command (use PowerShell equivalent) |
| `L240` | `| `L229` | `| `L209` | `| `L377` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L241` | `| `L230` | `| `L210` | `| `L378` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L242` | `| `L231` | `| `L211` | `| `L380` | `| `L675` | `ls eslint.config.* .eslintrc.* .` | Unix command (use PowerShell equivalent) |
| `L244` | `| `L233` | `| `L213` | `| `L382` | `| `L679` | `[ -f package.json ] ; grep -q '"` | Unix text processing utilities (use PowerShell or Python) |
| `L245` | `| `L234` | `| `L214` | `| `L383` | `| `L680` | `[ -f pyproject.toml ] ; grep -q ` | Unix text processing utilities (use PowerShell or Python) |
| `L246` | `| `L235` | `| `L215` | `| `L384` | `| `L686` | `[ -f package.json ] ; grep -q '"` | Unix text processing utilities (use PowerShell or Python) |
| `L247` | `| `L236` | `| `L216` | `| `L385` | `| `L689` | `command -v shellcheck | Out-Null` | Unix command (use PowerShell equivalent) |
| `L248` | `| `L237` | `| `L217` | `| `L394` | `| `L304` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L249` | `| `L238` | `| `L218` | `| `L395` | `| `L307` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L250` | `| `L239` | `| `L219` | `| `L405` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L251` | `| `L240` | `| `L220` | `| `L406` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L252` | `| `L241` | `| `L221` | `| `L408` | `| `L684` | `curl -fsSL "https://bun.sh/insta` | Unix network tools (use PowerShell or Python) |
| `L253` | `| `L242` | `| `L222` | `| `L409` | `| `L685` | `actual_sha=$(shasum -a 256 "$tmp` | Unix text processing utilities (use PowerShell or Python) |
| `L254` | `| `L244` | `| `L224` | `| `L411` | `| `L825` | `SAVED_HASH=$(cat ~/.gstack/proje` | Unix command (use PowerShell equivalent) |
| `L255` | `| `L245` | `| `L225` | `| `L412` | `| `L826` | `CURRENT_HASH=$(sed -n '/## Deplo` | Unix text processing utilities (use PowerShell or Python) |
| `L256` | `| `L246` | `| `L226` | `| `L414` | `| `L865` | `DEPLOY_CONFIG=$(grep -A 20 "## D` | Unix text processing utilities (use PowerShell or Python) |
| `L257` | `| `L247` | `| `L227` | `| `L415` | `| `L870` | `PROD_URL=$(echo "$DEPLOY_CONFIG"` | Unix text processing utilities (use PowerShell or Python) |
| `L258` | `| `L248` | `| `L228` | `| `L416` | `| `L871` | `PLATFORM=$(echo "$DEPLOY_CONFIG"` | Unix text processing utilities (use PowerShell or Python) |
| `L259` | `| `L249` | `| `L229` | `| `L417` | `| `L886` | `[ -f "$f" ] ; grep -qiE "deploy|` | Unix text processing utilities (use PowerShell or Python) |
| `L260` | `| `L250` | `| `L230` | `| `L418` | `| `L887` | `[ -f "$f" ] ; grep -qiE "staging` | Unix text processing utilities (use PowerShell or Python) |
| `L261` | `| `L251` | `| `L231` | `| `L419` | `| `L932` | `║  ├─ curl prod URL:      ✓ PASS` | Unix network tools (use PowerShell or Python) |
| `L262` | `| `L252` | `| `L232` | `| `L420` | `| `L953` | `failed at Step 1). If `curl` fai` | Unix network tools (use PowerShell or Python) |
| `L263` | `| `L253` | `| `L233` | `| `L421` | `| `L966` | `grep -i "staging" CLAUDE.md | Ou` | Unix text processing utilities (use PowerShell or Python) |
| `L264` | `| `L254` | `| `L234` | `| `L422` | `| `L972` | `[ -f "$f" ] ; grep -qiE "staging` | Unix text processing utilities (use PowerShell or Python) |
| `L265` | `| `L255` | `| `L235` | `| `L423` | `| `L1020` | `CURRENT_HASH=$(sed -n '/## Depl` | Unix text processing utilities (use PowerShell or Python) |
| `L266` | `| `L256` | `| `L236` | `| `L425` | `| `L1130` | `cat $GSTACK_ROOT/review/checkli` | Unix command (use PowerShell equivalent) |
| `L267` | `| `L257` | `| `L237` | `| `L426` | `| `L1164` | `ls -t ~/.gstack-dev/evals/*-e2e` | Unix command (use PowerShell equivalent) |
| `L268` | `| `L258` | `| `L238` | `| `L427` | `| `L1180` | `ls -t ~/.gstack-dev/evals/*-llm` | Unix command (use PowerShell equivalent) |
| `L269` | `| `L259` | `| `L239` | `| `L428` | `| `L1210` | `git log --oneline --all-match -` | Unix text processing utilities (use PowerShell or Python) |
| `L270` | `| `L260` | `| `L240` | `| `L429` | `| `L1365` | `DEPLOY_CONFIG=$(grep -A 20 "## ` | Unix text processing utilities (use PowerShell or Python) |
| `L271` | `| `L261` | `| `L241` | `| `L430` | `| `L1370` | `PROD_URL=$(echo "$DEPLOY_CONFIG` | Unix text processing utilities (use PowerShell or Python) |
| `L272` | `| `L262` | `| `L242` | `| `L431` | `| `L1371` | `PLATFORM=$(echo "$DEPLOY_CONFIG` | Unix text processing utilities (use PowerShell or Python) |
| `L273` | `| `L263` | `| `L243` | `| `L432` | `| `L1386` | `[ -f "$f" ] ; grep -qiE "deploy` | Unix text processing utilities (use PowerShell or Python) |
| `L274` | `| `L264` | `| `L244` | `| `L433` | `| `L1387` | `[ -f "$f" ] ; grep -qiE "stagin` | Unix text processing utilities (use PowerShell or Python) |
| `L275` | `| `L265` | `| `L245` | `| `L434` | `| `L1486` | `curl -sf {production-url} -o $n` | Unix network tools (use PowerShell or Python) |
| `L276` | `| `L266` | `| `L246` | `| `L443` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L277` | `| `L267` | `| `L247` | `| `L444` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L278` | `| `L268` | `| `L248` | `| `L446` | `| `L768` | `cat "$LEARN_FILE" | bun -e "` | ` | Unix command (use PowerShell equivalent) |
| `L279` | `| `L269` | `| `L249` | `| `L464` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L280` | `| `L270` | `| `L250` | `| `L465` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L281` | `| `L271` | `| `L251` | `| `L467` | `| `L694` | `curl -fsSL "https://bun.sh/insta` | Unix network tools (use PowerShell or Python) |
| `L282` | `| `L272` | `| `L252` | `| `L468` | `| `L695` | `actual_sha=$(shasum -a 256 "$tmp` | Unix text processing utilities (use PowerShell or Python) |
| `L283` | `| `L273` | `| `L253` | `| `L469` | `| `L731` | `ls -t ~/.gstack/projects/$SLUG/*` | Unix command (use PowerShell equivalent) |
| `L284` | `| `L274` | `| `L255` | `| `L471` | `| `L989` | `grep -li "<keyword1>\|<keyword2>` | Unix text processing utilities (use PowerShell or Python) |
| `L286` | `| `L278` | `| `L259` | `| `L475` | `| `L1321` | `PRIOR=$(ls -t ~/.gstack/project` | Unix command (use PowerShell equivalent) |
| `L287` | `| `L279` | `| `L260` | `| `L476` | `| `L1532` | `SESSION_TIER=$(echo "$PROFILE" ` | Unix text processing utilities (use PowerShell or Python) |
| `L288` | `| `L280` | `| `L261` | `| `L477` | `| `L1533` | `SESSION_COUNT=$(echo "$PROFILE"` | Unix text processing utilities (use PowerShell or Python) |
| `L289` | `| `L281` | `| `L262` | `| `L491` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L290` | `| `L282` | `| `L263` | `| `L492` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L291` | `| `L283` | `| `L264` | `| `L494` | `| `L689` | `curl -fsSL "https://bun.sh/insta` | Unix network tools (use PowerShell or Python) |
| `L292` | `| `L284` | `| `L265` | `| `L495` | `| `L690` | `actual_sha=$(shasum -a 256 "$tmp` | Unix text processing utilities (use PowerShell or Python) |
| `L293` | `| `L285` | `| `L266` | `| `L496` | `| `L711` | `_OLD_PID=$(cat "$(git rev-parse ` | Unix command (use PowerShell equivalent) |
| `L294` | `| `L286` | `| `L267` | `| `L497` | `| `L711` | `_OLD_PID=$(cat "$(git rev-parse ` | Unix command (use PowerShell equivalent) |
| `L295` | `| `L287` | `| `L268` | `| `L498` | `| `L756` | `cat "$(git rev-parse --show-topl` | Unix command (use PowerShell equivalent) |
| `L296` | `| `L288` | `| `L269` | `| `L499` | `| `L756` | `cat "$(git rev-parse --show-topl` | Unix command (use PowerShell equivalent) |
| `L297` | `| `L289` | `| `L270` | `| `L508` | `| `L287` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L298` | `| `L290` | `| `L271` | `| `L509` | `| `L290` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L299` | `| `L291` | `| `L272` | `| `L511` | `| `L711` | `curl -fsSL "https://bun.sh/insta` | Unix network tools (use PowerShell or Python) |
| `L300` | `| `L292` | `| `L273` | `| `L512` | `| `L712` | `actual_sha=$(shasum -a 256 "$tmp` | Unix text processing utilities (use PowerShell or Python) |
| `L301` | `| `L293` | `| `L274` | `| `L513` | `| `L908` | ``exec curl` syntax which OpenCla` | Unix network tools (use PowerShell or Python) |
| `L302` | `| `L294` | `| `L275` | `| `L514` | `| `L915` | `curl commands work directly. Whe` | Unix network tools (use PowerShell or Python) |
| `L303` | `| `L295` | `| `L276` | `| `L523` | `| `L289` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L304` | `| `L296` | `| `L277` | `| `L524` | `| `L292` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L305` | `| `L298` | `| `L279` | `| `L527` | `| `L779` | `grep -r "TODO\|FIXME\|HACK\|XXX"` | Unix text processing utilities (use PowerShell or Python) |
| `L306` | `| `L299` | `| `L280` | `| `L528` | `| `L789` | `DESIGN=$(ls -t ~/.gstack/project` | Unix command (use PowerShell equivalent) |
| `L307` | `| `L300` | `| `L281` | `| `L529` | `| `L790` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -` | Unix command (use PowerShell equivalent) |
| `L308` | `| `L301` | `| `L282` | `| `L530` | `| `L798` | `HANDOFF=$(ls -t ~/.gstack/projec` | Unix command (use PowerShell equivalent) |
| `L309` | `| `L302` | `| `L283` | `| `L531` | `| `L860` | `DESIGN=$(ls -t ~/.gstack/project` | Unix command (use PowerShell equivalent) |
| `L310` | `| `L303` | `| `L284` | `| `L532` | `| `L861` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -` | Unix command (use PowerShell equivalent) |
| `L311` | `| `L304` | `| `L285` | `| `L541` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L312` | `| `L305` | `| `L286` | `| `L542` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L313` | `| `L307` | `| `L288` | `| `L545` | `| `L980` | `- `mkdir -p ~/.gstack/projects/$` | Unix nested directory creation (use PowerShell equivalent) |
| `L314` | `| `L308` | `| `L289` | `| `L546` | `| `L1057` | `cat "$_DESIGN_DIR/feedback.json` | Unix command (use PowerShell equivalent) |
| `L315` | `| `L309` | `| `L290` | `| `L547` | `| `L1060` | `cat "$_DESIGN_DIR/feedback-pend` | Unix command (use PowerShell equivalent) |
| `L316` | `| `L310` | `| `L291` | `| `L548` | `| `L1089` | ``curl -s -X POST http://127.0.0` | Unix network tools (use PowerShell or Python) |
| `L317` | `| `L311` | `| `L292` | `| `L562` | `| `L296` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L318` | `| `L312` | `| `L293` | `| `L563` | `| `L299` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L319` | `| `L314` | `| `L295` | `| `L567` | `| `L832` | `- Getting started guides (grep R` | Unix text processing utilities (use PowerShell or Python) |
| `L320` | `| `L315` | `| `L296` | `| `L568` | `| `L833` | `- CLI help text (grep for `--hel` | Unix text processing utilities (use PowerShell or Python) |
| `L321` | `| `L316` | `| `L297` | `| `L569` | `| `L834` | `- Error message patterns (grep f` | Unix text processing utilities (use PowerShell or Python) |
| `L322` | `| `L317` | `| `L298` | `| `L570` | `| `L842` | `DESIGN=$(ls -t ~/.gstack/project` | Unix command (use PowerShell equivalent) |
| `L323` | `| `L318` | `| `L299` | `| `L571` | `| `L843` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -` | Unix command (use PowerShell equivalent) |
| `L324` | `| `L319` | `| `L300` | `| `L572` | `| `L902` | `DESIGN=$(ls -t ~/.gstack/project` | Unix command (use PowerShell equivalent) |
| `L325` | `| `L320` | `| `L301` | `| `L573` | `| `L903` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -` | Unix command (use PowerShell equivalent) |
| `L327` | `| `L322` | `| `L303` | `| `L583` | `| `L291` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L328` | `| `L323` | `| `L304` | `| `L584` | `| `L294` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L329` | `| `L324` | `| `L305` | `| `L586` | `| `L720` | `DESIGN=$(ls -t ~/.gstack/project` | Unix command (use PowerShell equivalent) |
| `L330` | `| `L325` | `| `L306` | `| `L587` | `| `L721` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -` | Unix command (use PowerShell equivalent) |
| `L331` | `| `L326` | `| `L307` | `| `L588` | `| `L775` | `DESIGN=$(ls -t ~/.gstack/project` | Unix command (use PowerShell equivalent) |
| `L332` | `| `L327` | `| `L308` | `| `L589` | `| `L776` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -` | Unix command (use PowerShell equivalent) |
| `L333` | `| `L328` | `| `L309` | `| `L590` | `| `L896` | `ls jest.config.* vitest.config.*` | Unix command (use PowerShell equivalent) |
| `L334` | `| `L329` | `| `L310` | `| `L591` | `| `L897` | `ls -d test/ tests/ spec/ __tests` | Unix command (use PowerShell equivalent) |
| `L335` | `| `L330` | `| `L311` | `| `L600` | `| `L296` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L336` | `| `L331` | `| `L312` | `| `L601` | `| `L299` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L337` | `| `L332` | `| `L313` | `| `L611` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L338` | `| `L333` | `| `L314` | `| `L612` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L339` | `| `L334` | `| `L315` | `| `L614` | `| `L707` | `curl -fsSL "https://bun.sh/insta` | Unix network tools (use PowerShell or Python) |
| `L340` | `| `L335` | `| `L316` | `| `L615` | `| `L708` | `actual_sha=$(shasum -a 256 "$tmp` | Unix text processing utilities (use PowerShell or Python) |
| `L341` | `| `L336` | `| `L317` | `| `L616` | `| `L748` | `ls -t ~/.gstack/projects/$SLUG/*` | Unix command (use PowerShell equivalent) |
| `L342` | `| `L337` | `| `L318` | `| `L630` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L343` | `| `L338` | `| `L319` | `| `L631` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L344` | `| `L340` | `| `L321` | `| `L634` | `| `L738` | `$B status | Out-Null | grep -q "` | Unix text processing utilities (use PowerShell or Python) |
| `L345` | `| `L341` | `| `L322` | `| `L635` | `| `L785` | `curl -fsSL "https://bun.sh/insta` | Unix network tools (use PowerShell or Python) |
| `L346` | `| `L342` | `| `L323` | `| `L636` | `| `L786` | `actual_sha=$(shasum -a 256 "$tmp` | Unix text processing utilities (use PowerShell or Python) |
| `L347` | `| `L343` | `| `L324` | `| `L637` | `| `L815` | `[ -f Gemfile ] ; grep -q "rails"` | Unix text processing utilities (use PowerShell or Python) |
| `L348` | `| `L344` | `| `L325` | `| `L638` | `| `L816` | `[ -f package.json ] ; grep -q '"` | Unix text processing utilities (use PowerShell or Python) |
| `L349` | `| `L345` | `| `L326` | `| `L639` | `| `L818` | `ls jest.config.* vitest.config.*` | Unix command (use PowerShell equivalent) |
| `L350` | `| `L346` | `| `L327` | `| `L640` | `| `L819` | `ls -d test/ tests/ spec/ __tests` | Unix command (use PowerShell equivalent) |
| `L351` | `| `L347` | `| `L328` | `| `L641` | `| `L904` | `ls -d .github/ | Out-Null ; echo` | Unix command (use PowerShell equivalent) |
| `L352` | `| `L348` | `| `L329` | `| `L642` | `| `L905` | `ls .gitlab-ci.yml .circleci/ bit` | Unix command (use PowerShell equivalent) |
| `L353` | `| `L349` | `| `L330` | `| `L643` | `| `L981` | `ls -t ~/.gstack/projects/$SLUG/*` | Unix command (use PowerShell equivalent) |
| `L354` | `| `L350` | `| `L331` | `| `L657` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L355` | `| `L351` | `| `L332` | `| `L658` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L356` | `| `L354` | `| `L336` | `| `L663` | `| `L782` | `cat ~/.gstack/greptile-history.m` | Unix command (use PowerShell equivalent) |
| `L357` | `| `L355` | `| `L337` | `| `L664` | `| `L785` | `cat TODOS.md | Out-Null ; true` ` | Unix command (use PowerShell equivalent) |
| `L358` | `| `L357` | `| `L339` | `| `L667` | `| `L794` | `cat ~/.gstack/analytics/skill-us` | Unix command (use PowerShell equivalent) |
| `L359` | `| `L358` | `| `L341` | `| `L669` | `| `L1029` | `ls -t .context/retros/*.json | ` | Unix command (use PowerShell equivalent) |
| `L360` | `| `L359` | `| `L342` | `| `L670` | `| `L1058` | `existing=$(ls .context/retros/$` | Unix command (use PowerShell equivalent) |
| `L361` | `| `L360` | `| `L343` | `| `L671` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-` | Unix command (use PowerShell equivalent) |
| `L362` | `| `L361` | `| `L343` | `| `L671` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-` | Unix command (use PowerShell equivalent) |
| `L363` | `| `L362` | `| `L344` | `| `L671` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-` | Unix command (use PowerShell equivalent) |
| `L364` | `| `L363` | `| `L344` | `| `L671` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-` | Unix command (use PowerShell equivalent) |
| `L365` | `| `L364` | `| `L345` | `| `L672` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-` | Unix command (use PowerShell equivalent) |
| `L366` | `| `L365` | `| `L345` | `| `L672` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-` | Unix command (use PowerShell equivalent) |
| `L367` | `| `L366` | `| `L346` | `| `L672` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-` | Unix command (use PowerShell equivalent) |
| `L368` | `| `L367` | `| `L346` | `| `L672` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-` | Unix command (use PowerShell equivalent) |
| `L369` | `| `L368` | `| `L347` | `| `L674` | `| `L1482` | `ls -t ~/.gstack/retros/global-*` | Unix command (use PowerShell equivalent) |
| `L370` | `| `L369` | `| `L348` | `| `L675` | `| `L1501` | `existing=$(ls ~/.gstack/retros/` | Unix command (use PowerShell equivalent) |
| `L371` | `| `L370` | `| `L349` | `| `L689` | `| `L287` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L372` | `| `L371` | `| `L350` | `| `L690` | `| `L290` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L374` | `| `L374` | `| `L353` | `| `L694` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L375` | `| `L374` | `| `L353` | `| `L694` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L376` | `| `L375` | `| `L353` | `| `L694` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L377` | `| `L375` | `| `L353` | `| `L694` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L378` | `| `L376` | `| `L354` | `| `L694` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L379` | `| `L376` | `| `L354` | `| `L694` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L380` | `| `L377` | `| `L354` | `| `L694` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L381` | `| `L377` | `| `L354` | `| `L694` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L382` | `| `L378` | `| `L355` | `| `L695` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L383` | `| `L378` | `| `L355` | `| `L695` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L384` | `| `L379` | `| `L355` | `| `L695` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L385` | `| `L379` | `| `L355` | `| `L695` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L386` | `| `L380` | `| `L356` | `| `L695` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L387` | `| `L380` | `| `L356` | `| `L695` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L388` | `| `L381` | `| `L356` | `| `L695` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L389` | `| `L381` | `| `L356` | `| `L695` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | ` | Unix command (use PowerShell equivalent) |
| `L390` | `| `L382` | `| `L357` | `| `L696` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$` | Unix command (use PowerShell equivalent) |
| `L391` | `| `L383` | `| `L358` | `| `L696` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$` | Unix command (use PowerShell equivalent) |
| `L392` | `| `L384` | `| `L359` | `| `L697` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$` | Unix command (use PowerShell equivalent) |
| `L393` | `| `L385` | `| `L360` | `| `L697` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$` | Unix command (use PowerShell equivalent) |
| `L394` | `| `L386` | `| `L361` | `| `L706` | `| `L389` | `$B status | Out-Null | grep -q "` | Unix text processing utilities (use PowerShell or Python) |
| `L395` | `| `L387` | `| `L362` | `| `L707` | `| `L427` | `curl -fsSL "https://bun.sh/insta` | Unix network tools (use PowerShell or Python) |
| `L396` | `| `L388` | `| `L363` | `| `L708` | `| `L428` | `actual_sha=$(shasum -a 256 "$tmp` | Unix text processing utilities (use PowerShell or Python) |
| `L397` | `| `L389` | `| `L364` | `| `L717` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L398` | `| `L390` | `| `L365` | `| `L718` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L399` | `| `L391` | `| `L366` | `| `L720` | `| `L662` | `grep -A 20 "## Deploy Configurat` | Unix text processing utilities (use PowerShell or Python) |
| `L400` | `| `L392` | `| `L367` | `| `L721` | `| `L681` | `[ -f fly.toml ] ; echo "PLATFORM` | Unix command (use PowerShell equivalent) |
| `L403` | `| `L395` | `| `L370` | `| `L724` | `| `L690` | `[ -f "$f" ] ; grep -qiE "deploy|` | Unix text processing utilities (use PowerShell or Python) |
| `L404` | `| `L396` | `| `L371` | `| `L725` | `| `L694` | `[ -f package.json ] ; grep -q '"` | Unix text processing utilities (use PowerShell or Python) |
| `L406` | `| `L398` | `| `L373` | `| `L727` | `| `L706` | `1. Extract app name: `grep -m1 "` | Unix text processing utilities (use PowerShell or Python) |
| `L407` | `| `L399` | `| `L374` | `| `L728` | `| `L734` | `2. If installed: `vercel ls --pr` | Unix command (use PowerShell equivalent) |
| `L408` | `| `L400` | `| `L375` | `| `L729` | `| `L807` | `curl -sf "{health-check-url}" -o` | Unix network tools (use PowerShell or Python) |
| `L409` | `| `L401` | `| `L376` | `| `L738` | `| `L289` | `_LAST=$(grep "\"branch\":\"${_BR` | Unix text processing utilities (use PowerShell or Python) |
| `L410` | `| `L402` | `| `L377` | `| `L739` | `| `L292` | `_RECENT_SKILLS=$(grep "\"branch\` | Unix text processing utilities (use PowerShell or Python) |
| `L411` | `| `L404` | `| `L379` | `| `L742` | `| `L829` | `git diff origin/<base> --name-on` | Unix text processing utilities (use PowerShell or Python) |
| `L412` | `| `L405` | `| `L380` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L412` | `| `L405` | `| `L380` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L413` | `| `L405` | `| `L380` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L413` | `| `L405` | `| `L380` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L414` | `| `L406` | `| `L380` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L414` | `| `L406` | `| `L380` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L415` | `| `L406` | `| `L380` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L415` | `| `L406` | `| `L380` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L416` | `| `L407` | `| `L381` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L416` | `| `L407` | `| `L381` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L417` | `| `L407` | `| `L381` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L417` | `| `L407` | `| `L381` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L418` | `| `L408` | `| `L381` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L418` | `| `L408` | `| `L381` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L419` | `| `L408` | `| `L381` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L419` | `| `L408` | `| `L381` | `| `L743` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L420` | `| `L409` | `| `L382` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L420` | `| `L409` | `| `L382` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L421` | `| `L409` | `| `L382` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L421` | `| `L409` | `| `L382` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L422` | `| `L410` | `| `L382` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L422` | `| `L410` | `| `L382` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L423` | `| `L410` | `| `L382` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L423` | `| `L410` | `| `L382` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L424` | `| `L411` | `| `L383` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L424` | `| `L411` | `| `L383` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L425` | `| `L411` | `| `L383` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L425` | `| `L411` | `| `L383` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L426` | `| `L412` | `| `L383` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L426` | `| `L412` | `| `L383` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L427` | `| `L412` | `| `L383` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L427` | `| `L412` | `| `L383` | `| `L744` | `| `L834` | `ls .github/workflows/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L428` | `| `L413` | `| `L384` | `| `L745` | `| `L835` | `grep -qE 'release|publish|deploy` | Unix text processing utilities (use PowerShell or Python) |
| `L429` | `| `L414` | `| `L385` | `| `L746` | `| `L881` | `[ -f Gemfile ] ; grep -q "rails"` | Unix text processing utilities (use PowerShell or Python) |
| `L430` | `| `L415` | `| `L386` | `| `L747` | `| `L882` | `[ -f package.json ] ; grep -q '"` | Unix text processing utilities (use PowerShell or Python) |
| `L431` | `| `L416` | `| `L387` | `| `L748` | `| `L884` | `ls jest.config.* vitest.config.*` | Unix command (use PowerShell equivalent) |
| `L432` | `| `L417` | `| `L388` | `| `L749` | `| `L885` | `ls -d test/ tests/ spec/ __tests` | Unix command (use PowerShell equivalent) |
| `L433` | `| `L418` | `| `L389` | `| `L750` | `| `L970` | `ls -d .github/ | Out-Null ; echo` | Unix command (use PowerShell equivalent) |
| `L434` | `| `L419` | `| `L390` | `| `L751` | `| `L971` | `ls .gitlab-ci.yml .circleci/ bit` | Unix command (use PowerShell equivalent) |
| `L435` | `| `L420` | `| `L391` | `| `L752` | `| `L1176` | `grep -l "changed_file_basename"` | Unix text processing utilities (use PowerShell or Python) |
| `L437` | `| `L422` | `| `L393` | `| `L754` | `| `L1238` | `ls jest.config.* vitest.config.` | Unix command (use PowerShell equivalent) |
| `L438` | `| `L423` | `| `L394` | `| `L755` | `| `L1239` | `ls -d test/ tests/ spec/ __test` | Unix command (use PowerShell equivalent) |
| `L440` | `| `L425` | `| `L396` | `| `L759` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L441` | `| `L425` | `| `L396` | `| `L759` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L442` | `| `L426` | `| `L396` | `| `L759` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L443` | `| `L426` | `| `L396` | `| `L759` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L444` | `| `L427` | `| `L397` | `| `L759` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L445` | `| `L427` | `| `L397` | `| `L759` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L446` | `| `L428` | `| `L397` | `| `L759` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L447` | `| `L428` | `| `L397` | `| `L759` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L448` | `| `L429` | `| `L398` | `| `L760` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L449` | `| `L429` | `| `L398` | `| `L760` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L450` | `| `L430` | `| `L398` | `| `L760` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L451` | `| `L430` | `| `L398` | `| `L760` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L452` | `| `L431` | `| `L399` | `| `L760` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L453` | `| `L431` | `| `L399` | `| `L760` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L454` | `| `L432` | `| `L399` | `| `L760` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L455` | `| `L432` | `| `L399` | `| `L760` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md |` | Unix command (use PowerShell equivalent) |
| `L456` | `| `L433` | `| `L400` | `| `L761` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "` | Unix command (use PowerShell equivalent) |
| `L457` | `| `L434` | `| `L401` | `| `L761` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "` | Unix command (use PowerShell equivalent) |
| `L458` | `| `L435` | `| `L402` | `| `L762` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "` | Unix command (use PowerShell equivalent) |
| `L459` | `| `L436` | `| `L403` | `| `L762` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "` | Unix command (use PowerShell equivalent) |
| `L460` | `| `L437` | `| `L404` | `| `L764` | `| `L1647` | `curl -s -o $null -w '%{http_cod` | Unix network tools (use PowerShell or Python) |
| `L461` | `| `L438` | `| `L405` | `| `L765` | `| `L1648` | `curl -s -o $null -w '%{http_cod` | Unix network tools (use PowerShell or Python) |
| `L462` | `| `L439` | `| `L406` | `| `L766` | `| `L1649` | `curl -s -o $null -w '%{http_cod` | Unix network tools (use PowerShell or Python) |
| `L463` | `| `L440` | `| `L407` | `| `L767` | `| `L1650` | `curl -s -o $null -w '%{http_cod` | Unix network tools (use PowerShell or Python) |
| `L464` | `| `L441` | `| `L408` | `| `L768` | `| `L1660` | `cat ${CLAUDE_SKILL_DIR}/../qa-o` | Unix command (use PowerShell equivalent) |
| `L465` | `| `L442` | `| `L409` | `| `L769` | `| `L1964` | `CURRENT_VERSION=$(cat VERSION |` | Unix command (use PowerShell equivalent) |
| `L466` | `| `L443` | `| `L410` | `| `L770` | `| `L2029` | `if ! printf '%s' "$NEW_VERSION"` | Unix text processing utilities (use PowerShell or Python) |
| `L467` | `| `L444` | `| `L411` | `| `L771` | `| `L2055` | `REPAIR_VERSION=$(cat VERSION | ` | Unix command (use PowerShell equivalent) |
| `L468` | `| `L445` | `| `L412` | `| `L772` | `| `L2056` | `if ! printf '%s' "$REPAIR_VERSI` | Unix text processing utilities (use PowerShell or Python) |
| `L469` | `| `L446` | `| `L413` | `| `L773` | `| `L2203` | `git commit -m "$(cat <<'EOF'` |` | Unix command (use PowerShell equivalent) |
| `L470` | `| `L448` | `| `L416` | `| `L783` | `| `L42` | `PREV=$(cat "$STATE_DIR/freeze-dir` | Unix command (use PowerShell equivalent) |
| `L471` | `| `L449` | `| `L417` | `| `L791` | `| `L71` | `_SNOOZED_VER=$(awk '{print $1}' "` | Unix text processing utilities (use PowerShell or Python) |
| `L472` | `| `L450` | `| `L418` | `| `L792` | `| `L73` | `_CUR_LEVEL=$(awk '{print $2}' "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L473` | `| `L451` | `| `L419` | `| `L793` | `| `L127` | `OLD_VERSION=$(cat "$INSTALL_DIR/` | Unix command (use PowerShell equivalent) |
| `L474` | `| `L452` | `| `L420` | `| `L794` | `| `L179` | `if ! grep -qF '.agents/skills/gs` | Unix text processing utilities (use PowerShell or Python) |
| `L475` | `| `L453` | `| `L421` | `| `L795` | `| `L214` | `m_ver="$(basename "$migration" .` | Unix text processing utilities (use PowerShell or Python) |
| `L476` | `| `L454` | `| `L422` | `| `L796` | `| `L283` | `PRIMARY_VER=$(cat "$INSTALL_DIR/` | Unix command (use PowerShell equivalent) |
| `L477` | `| `L455` | `| `L423` | `| `L797` | `| `L284` | `LOCAL_VER=$(cat "$LOCAL_GSTACK/V` | Unix command (use PowerShell equivalent) |
| `L478` | `| `L456` | `| `L424` | `| `L805` | `| `L446` | `curl -fsSL "https://bun.sh/insta` | Unix network tools (use PowerShell or Python) |
| `L479` | `| `L457` | `| `L425` | `| `L806` | `| `L447` | `actual_sha=$(shasum -a 256 "$tmp` | Unix text processing utilities (use PowerShell or Python) |
| `L481` | `| `L459` | `| `L427` | `| `L821` | `| `L64` | `_SNOOZED_VER=$(awk '{print $1}' "` | Unix text processing utilities (use PowerShell or Python) |
| `L482` | `| `L460` | `| `L428` | `| `L822` | `| `L66` | `_CUR_LEVEL=$(awk '{print $2}' "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L483` | `| `L461` | `| `L429` | `| `L823` | `| `L120` | `OLD_VERSION=$(cat "$INSTALL_DIR/` | Unix command (use PowerShell equivalent) |
| `L484` | `| `L462` | `| `L430` | `| `L824` | `| `L172` | `if ! grep -qF '.agents/skills/gs` | Unix text processing utilities (use PowerShell or Python) |
| `L485` | `| `L463` | `| `L431` | `| `L825` | `| `L207` | `m_ver="$(basename "$migration" .` | Unix text processing utilities (use PowerShell or Python) |
| `L486` | `| `L464` | `| `L432` | `| `L826` | `| `L276` | `PRIMARY_VER=$(cat "$INSTALL_DIR/` | Unix command (use PowerShell equivalent) |
| `L487` | `| `L465` | `| `L433` | `| `L827` | `| `L277` | `LOCAL_VER=$(cat "$LOCAL_GSTACK/V` | Unix command (use PowerShell equivalent) |
| `L488` | `| `L467` | `| `L436` | `| `L844` | `| `L25` | `- **[HIGH]** — Reliably detectabl` | Unix text processing utilities (use PowerShell or Python) |
| `L489` | `| `L468` | `| `L442` | `| `L141` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L490` | `| `L469` | `| `L443` | `| `L148` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L491` | `| `L470` | `| `L445` | `| `L244` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L492` | `| `L471` | `| `L447` | `| `L254` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L493` | `| `L472` | `| `L449` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L494` | `| `L473` | `| `L450` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L495` | `| `L474` | `| `L451` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L496` | `| `L475` | `| `L456` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L497` | `| `L476` | `| `L460` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L498` | `| `L477` | `| `L476` | `| `L76` | `if ($content -like "*mkdir -p*") { throw "FAI` | Unix nested directory creation (use PowerShell equivalent) |
| `L499` | `| `L478` | `| `L477` | `| `L150` | `if ($content -like "*mkdir -p*") { throw "FA` | Unix nested directory creation (use PowerShell equivalent) |
| `L500` | `| `L479` | `| `L499` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L501` | `| `L480` | `| `L500` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L503` | `| `L482` | `| `L503` | `| `L759` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$B` | Unix command (use PowerShell equivalent) |
| `L504` | `| `L483` | `| `L504` | `| `L760` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/` | Unix command (use PowerShell equivalent) |
| `L505` | `| `L484` | `| `L505` | `| `L922` | `- Discover design docs: `ls -t ~/.gstack/pro` | Unix command (use PowerShell equivalent) |
| `L506` | `| `L485` | `| `L506` | `| `L923` | `- Detect UI scope: grep the plan for view/re` | Unix text processing utilities (use PowerShell or Python) |
| `L507` | `| `L486` | `| `L507` | `| `L926` | `- Detect DX scope: grep the plan for develop` | Unix text processing utilities (use PowerShell or Python) |
| `L508` | `| `L487` | `| `L515` | `| `L410` | `curl -fsSL "https://bun.sh/install" -o "$tmp` | Unix network tools (use PowerShell or Python) |
| `L509` | `| `L488` | `| `L516` | `| `L411` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk ` | Unix text processing utilities (use PowerShell or Python) |
| `L510` | `| `L489` | `| `L524` | `| `L412` | `curl -fsSL "https://bun.sh/install" -o "$tmp` | Unix network tools (use PowerShell or Python) |
| `L511` | `| `L490` | `| `L525` | `| `L413` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk ` | Unix text processing utilities (use PowerShell or Python) |
| `L512` | `| `L491` | `| `L540` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L513` | `| `L492` | `| `L541` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L514` | `| `L493` | `| `L543` | `| `L666` | `curl -fsSL "https://bun.sh/install" -o "$tmp` | Unix network tools (use PowerShell or Python) |
| `L515` | `| `L494` | `| `L544` | `| `L667` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk ` | Unix text processing utilities (use PowerShell or Python) |
| `L518` | `| `L497` | `| `L555` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Unix force-remove command (use PowerShell equivalent) |
| `L519` | `| `L498` | `| `L556` | `| `L60` | `| `docker rm -f` / `docker system prune` | `d` | Unix force-remove command (use PowerShell equivalent) |
| `L520` | `| `L499` | `| `L557` | `| `L65` | `- `rm -rf node_modules` / `.next` / `dist` / ` | Unix force-remove command (use PowerShell equivalent) |
| `L521` | `| `L500` | `| `L562` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Unix force-remove command (use PowerShell equivalent) |
| `L522` | `| `L501` | `| `L571` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L523` | `| `L502` | `| `L572` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L524` | `| `L505` | `| `L584` | `| `L294` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L525` | `| `L506` | `| `L585` | `| `L297` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L526` | `| `L507` | `| `L588` | `| `L700` | `ls package.json tsconfig.json | Out-Null ; e` | Unix command (use PowerShell equivalent) |
| `L527` | `| `L508` | `| `L589` | `| `L701` | `ls Gemfile | Out-Null ; echo "STACK: Ruby"` ` | Unix command (use PowerShell equivalent) |
| `L528` | `| `L509` | `| `L590` | `| `L702` | `ls requirements.txt pyproject.toml setup.py ` | Unix command (use PowerShell equivalent) |
| `L529` | `| `L510` | `| `L591` | `| `L703` | `ls go.mod | Out-Null ; echo "STACK: Go"` | U` | Unix command (use PowerShell equivalent) |
| `L530` | `| `L511` | `| `L592` | `| `L704` | `ls Cargo.toml | Out-Null ; echo "STACK: Rust` | Unix command (use PowerShell equivalent) |
| `L531` | `| `L512` | `| `L593` | `| `L705` | `ls pom.xml build.gradle | Out-Null ; echo "S` | Unix command (use PowerShell equivalent) |
| `L532` | `| `L513` | `| `L594` | `| `L706` | `ls composer.json | Out-Null ; echo "STACK: P` | Unix command (use PowerShell equivalent) |
| `L533` | `| `L515` | `| `L596` | `| `L712` | `grep -q "next" package.json | Out-Null ; ech` | Unix text processing utilities (use PowerShell or Python) |
| `L534` | `| `L516` | `| `L597` | `| `L713` | `grep -q "express" package.json | Out-Null ; ` | Unix text processing utilities (use PowerShell or Python) |
| `L535` | `| `L517` | `| `L598` | `| `L714` | `grep -q "fastify" package.json | Out-Null ; ` | Unix text processing utilities (use PowerShell or Python) |
| `L536` | `| `L518` | `| `L599` | `| `L715` | `grep -q "hono" package.json | Out-Null ; ech` | Unix text processing utilities (use PowerShell or Python) |
| `L537` | `| `L519` | `| `L600` | `| `L716` | `grep -q "django" requirements.txt pyproject.` | Unix text processing utilities (use PowerShell or Python) |
| `L538` | `| `L520` | `| `L601` | `| `L717` | `grep -q "fastapi" requirements.txt pyproject` | Unix text processing utilities (use PowerShell or Python) |
| `L539` | `| `L521` | `| `L602` | `| `L718` | `grep -q "flask" requirements.txt pyproject.t` | Unix text processing utilities (use PowerShell or Python) |
| `L540` | `| `L522` | `| `L603` | `| `L719` | `grep -q "rails" Gemfile | Out-Null ; echo "F` | Unix text processing utilities (use PowerShell or Python) |
| `L541` | `| `L523` | `| `L604` | `| `L720` | `grep -q "gin-gonic" go.mod | Out-Null ; echo` | Unix text processing utilities (use PowerShell or Python) |
| `L542` | `| `L524` | `| `L605` | `| `L721` | `grep -q "spring-boot" pom.xml build.gradle |` | Unix text processing utilities (use PowerShell or Python) |
| `L543` | `| `L525` | `| `L606` | `| `L722` | `grep -q "laravel" composer.json | Out-Null ;` | Unix text processing utilities (use PowerShell or Python) |
| `L544` | `| `L526` | `| `L607` | `| `L759` | `ls .env .env.* | Out-Null` | Unix command (u` | Unix command (use PowerShell equivalent) |
| `L545` | `| `L527` | `| `L608` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix text processing utilities (use PowerShell or Python) |
| `L545` | `| `L527` | `| `L608` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix command (use PowerShell equivalent) |
| `L546` | `| `L527` | `| `L608` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix text processing utilities (use PowerShell or Python) |
| `L546` | `| `L527` | `| `L608` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix command (use PowerShell equivalent) |
| `L547` | `| `L528` | `| `L608` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix text processing utilities (use PowerShell or Python) |
| `L547` | `| `L528` | `| `L608` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix command (use PowerShell equivalent) |
| `L548` | `| `L528` | `| `L608` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix text processing utilities (use PowerShell or Python) |
| `L548` | `| `L528` | `| `L608` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix command (use PowerShell equivalent) |
| `L549` | `| `L529` | `| `L609` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix text processing utilities (use PowerShell or Python) |
| `L549` | `| `L529` | `| `L609` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix command (use PowerShell equivalent) |
| `L550` | `| `L529` | `| `L609` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix text processing utilities (use PowerShell or Python) |
| `L550` | `| `L529` | `| `L609` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix command (use PowerShell equivalent) |
| `L551` | `| `L530` | `| `L609` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix text processing utilities (use PowerShell or Python) |
| `L551` | `| `L530` | `| `L609` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix command (use PowerShell equivalent) |
| `L552` | `| `L530` | `| `L609` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix text processing utilities (use PowerShell or Python) |
| `L552` | `| `L530` | `| `L609` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | g` | Unix command (use PowerShell equivalent) |
| `L553` | `| `L531` | `| `L610` | `| `L801` | `grep -q "^\.env$\|^\.env\.\*" .gitignore | O` | Unix text processing utilities (use PowerShell or Python) |
| `L554` | `| `L532` | `| `L611` | `| `L807` | `[ -f "$f" ] ; grep -n "password:\|token:\|se` | Unix text processing utilities (use PowerShell or Python) |
| `L555` | `| `L533` | `| `L612` | `| `L896` | `**Key checks (beyond grep):**` | Unix text p` | Unix text processing utilities (use PowerShell or Python) |
| `L556` | `| `L534` | `| `L613` | `| `L914` | `ls -la .agents/skills/ | Out-Null` | Unix co` | Unix command (use PowerShell equivalent) |
| `L557` | `| `L535` | `| `L614` | `| `L918` | `- `curl`, `wget`, `fetch`, `http`, `exfiltra` | Unix network tools (use PowerShell or Python) |
| `L558` | `| `L536` | `| `L624` | `| `L288` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L559` | `| `L537` | `| `L625` | `| `L291` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L560` | `| `L538` | `| `L627` | `| `L679` | `ls DESIGN.md design-system.md | Out-Null ; e` | Unix command (use PowerShell equivalent) |
| `L561` | `| `L539` | `| `L628` | `| `L688` | `cat README.md | Out-Null | head -50` | Unix ` | Unix command (use PowerShell equivalent) |
| `L562` | `| `L540` | `| `L629` | `| `L689` | `cat package.json | Out-Null | head -20` | Un` | Unix command (use PowerShell equivalent) |
| `L563` | `| `L541` | `| `L630` | `| `L690` | `ls src/ app/ pages/ components/ | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L564` | `| `L542` | `| `L631` | `| `L698` | `ls ~/.gstack/projects/$SLUG/*office-hours* |` | Unix command (use PowerShell equivalent) |
| `L565` | `| `L543` | `| `L632` | `| `L699` | `ls .context/*office-hours* .context/attachme` | Unix command (use PowerShell equivalent) |
| `L566` | `| `L544` | `| `L633` | `| `L731` | `curl -fsSL "https://bun.sh/install" -o "$tmp` | Unix network tools (use PowerShell or Python) |
| `L567` | `| `L545` | `| `L634` | `| `L732` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk ` | Unix text processing utilities (use PowerShell or Python) |
| `L568` | `| `L546` | `| `L635` | `| `L1045` | `cat "$_DESIGN_DIR/feedback.json"` | Unix co` | Unix command (use PowerShell equivalent) |
| `L569` | `| `L547` | `| `L636` | `| `L1048` | `cat "$_DESIGN_DIR/feedback-pending.json"` |` | Unix command (use PowerShell equivalent) |
| `L570` | `| `L548` | `| `L637` | `| `L1077` | ``curl -s -X POST http://127.0.0.1:PORT/api/` | Unix network tools (use PowerShell or Python) |
| `L571` | `| `L549` | `| `L651` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L572` | `| `L550` | `| `L652` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L573` | `| `L551` | `| `L654` | `| `L811` | `curl -fsSL "https://bun.sh/install" -o "$tmp` | Unix network tools (use PowerShell or Python) |
| `L574` | `| `L552` | `| `L655` | `| `L812` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk ` | Unix text processing utilities (use PowerShell or Python) |
| `L575` | `| `L553` | `| `L656` | `| `L836` | `_CEO=$(ls -t ~/.gstack/projects/$SLUG/ceo-pl` | Unix command (use PowerShell equivalent) |
| `L576` | `| `L554` | `| `L657` | `| `L842` | `_APPROVED=$(ls -t ~/.gstack/projects/$SLUG/d` | Unix command (use PowerShell equivalent) |
| `L577` | `| `L555` | `| `L658` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Unix command (use PowerShell equivalent) |
| `L578` | `| `L556` | `| `L659` | `| `L854` | `_FINALIZED=$(ls -t ~/.gstack/projects/$SLUG/` | Unix command (use PowerShell equivalent) |
| `L579` | `| `L557` | `| `L660` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L579` | `| `L557` | `| `L660` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix command (use PowerShell equivalent) |
| `L580` | `| `L557` | `| `L660` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L580` | `| `L557` | `| `L660` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix command (use PowerShell equivalent) |
| `L581` | `| `L558` | `| `L660` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L581` | `| `L558` | `| `L660` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix command (use PowerShell equivalent) |
| `L582` | `| `L558` | `| `L660` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L582` | `| `L558` | `| `L660` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix command (use PowerShell equivalent) |
| `L583` | `| `L559` | `| `L661` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L583` | `| `L559` | `| `L661` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix command (use PowerShell equivalent) |
| `L584` | `| `L559` | `| `L661` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L584` | `| `L559` | `| `L661` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix command (use PowerShell equivalent) |
| `L585` | `| `L560` | `| `L661` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L585` | `| `L560` | `| `L661` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix command (use PowerShell equivalent) |
| `L586` | `| `L560` | `| `L661` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L586` | `| `L560` | `| `L661` | `| `L979` | `[ -f package.json ] ; cat package.json | gre` | Unix command (use PowerShell equivalent) |
| `L587` | `| `L561` | `| `L662` | `| `L1226` | `_PORT=$(lsof -i -P -n | grep "$_SERVER_PID"` | Unix text processing utilities (use PowerShell or Python) |
| `L588` | `| `L562` | `| `L668` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Unix command (use PowerShell equivalent) |
| `L589` | `| `L563` | `| `L677` | `| `L288` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L590` | `| `L564` | `| `L678` | `| `L291` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L591` | `| `L565` | `| `L680` | `| `L689` | `$B status | Out-Null | grep -q "Mode: cdp" ;` | Unix text processing utilities (use PowerShell or Python) |
| `L592` | `| `L566` | `| `L681` | `| `L740` | `curl -fsSL "https://bun.sh/install" -o "$tmp` | Unix network tools (use PowerShell or Python) |
| `L593` | `| `L567` | `| `L682` | `| `L741` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk ` | Unix text processing utilities (use PowerShell or Python) |
| `L594` | `| `L568` | `| `L683` | `| `L770` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | O` | Unix text processing utilities (use PowerShell or Python) |
| `L595` | `| `L569` | `| `L684` | `| `L771` | `[ -f package.json ] ; grep -q '"next"' packa` | Unix text processing utilities (use PowerShell or Python) |
| `L596` | `| `L570` | `| `L685` | `| `L773` | `ls jest.config.* vitest.config.* playwright.` | Unix command (use PowerShell equivalent) |
| `L597` | `| `L571` | `| `L686` | `| `L774` | `ls -d test/ tests/ spec/ __tests__/ cypress/` | Unix command (use PowerShell equivalent) |
| `L598` | `| `L572` | `| `L687` | `| `L859` | `ls -d .github/ | Out-Null ; echo "CI:github"` | Unix command (use PowerShell equivalent) |
| `L599` | `| `L573` | `| `L688` | `| `L860` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | O` | Unix command (use PowerShell equivalent) |
| `L600` | `| `L574` | `| `L702` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L601` | `| `L575` | `| `L703` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L602` | `| `L576` | `| `L705` | `| `L829` | `cat DESIGN.md | Out-Null | head -80 ; echo "` | Unix command (use PowerShell equivalent) |
| `L603` | `| `L577` | `| `L706` | `| `L833` | `ls src/ app/ pages/ components/ | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L604` | `| `L578` | `| `L707` | `| `L838` | `ls ~/.gstack/projects/$SLUG/*office-hours* |` | Unix command (use PowerShell equivalent) |
| `L605` | `| `L579` | `| `L708` | `| `L848` | `curl -s -o $null -w "%{http_code}" http://lo` | Unix network tools (use PowerShell or Python) |
| `L606` | `| `L580` | `| `L709` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Unix command (use PowerShell equivalent) |
| `L607` | `| `L581` | `| `L710` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L608` | `| `L582` | `| `L710` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L609` | `| `L583` | `| `L711` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L610` | `| `L584` | `| `L711` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L611` | `| `L585` | `| `L712` | `| `L1043` | `cat "$_DESIGN_DIR/feedback.json"` | Unix co` | Unix command (use PowerShell equivalent) |
| `L612` | `| `L586` | `| `L713` | `| `L1046` | `cat "$_DESIGN_DIR/feedback-pending.json"` |` | Unix command (use PowerShell equivalent) |
| `L613` | `| `L587` | `| `L714` | `| `L1075` | ``curl -s -X POST http://127.0.0.1:PORT/api/` | Unix network tools (use PowerShell or Python) |
| `L614` | `| `L588` | `| `L723` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Unix command (use PowerShell equivalent) |
| `L615` | `| `L589` | `| `L727` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L616` | `| `L590` | `| `L727` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L617` | `| `L591` | `| `L737` | `| `L292` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L618` | `| `L592` | `| `L738` | `| `L295` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L620` | `| `L594` | `| `L741` | `| `L732` | `curl -fsSL "https://bun.sh/install" -o "$tmp` | Unix network tools (use PowerShell or Python) |
| `L621` | `| `L595` | `| `L742` | `| `L733` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk ` | Unix text processing utilities (use PowerShell or Python) |
| `L622` | `| `L596` | `| `L744` | `| `L849` | `$GSTACK_ROOT/bin/gstack-review-read | Out-Nu` | Unix text processing utilities (use PowerShell or Python) |
| `L623` | `| `L597` | `| `L745` | `| `L903` | `- Deprecation warnings in code (grep for dep` | Unix text processing utilities (use PowerShell or Python) |
| `L624` | `| `L598` | `| `L754` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L625` | `| `L599` | `| `L755` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L627` | `| `L601` | `| `L758` | `| `L939` | `git commit -m "$(cat <<'EOF'` | Unix command` | Unix command (use PowerShell equivalent) |
| `L628` | `| `L602` | `| `L759` | `| `L984` | `glab mr update -d "$(cat <<'MRBODY'` | Unix ` | Unix command (use PowerShell equivalent) |
| `L629` | `| `L603` | `| `L780` | `| `L6` | `Combines /gs:careful (warns before rm -rf, DRO` | Unix force-remove command (use PowerShell equivalent) |
| `L630` | `| `L604` | `| `L782` | `| `L89` | `- "1. **Destructive command warnings** — rm -` | Unix force-remove command (use PowerShell equivalent) |
| `L631` | `| `L605` | `| `L791` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L632` | `| `L606` | `| `L792` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L633` | `| `L607` | `| `L794` | `| `L675` | `ls eslint.config.* .eslintrc.* .eslintrc | O` | Unix command (use PowerShell equivalent) |
| `L634` | `| `L608` | `| `L795` | `| `L676` | `[ -f .pylintrc ] ; [ -f pyproject.toml ] ; g` | Unix text processing utilities (use PowerShell or Python) |
| `L635` | `| `L609` | `| `L796` | `| `L679` | `[ -f package.json ] ; grep -q '"test"' packa` | Unix text processing utilities (use PowerShell or Python) |
| `L636` | `| `L610` | `| `L797` | `| `L680` | `[ -f pyproject.toml ] ; grep -q "pytest" pyp` | Unix text processing utilities (use PowerShell or Python) |
| `L637` | `| `L611` | `| `L798` | `| `L686` | `[ -f package.json ] ; grep -q '"knip"' packa` | Unix text processing utilities (use PowerShell or Python) |
| `L638` | `| `L612` | `| `L799` | `| `L689` | `command -v shellcheck | Out-Null 2>&1 ; ls *` | Unix command (use PowerShell equivalent) |
| `L639` | `| `L613` | `| `L808` | `| `L304` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L640` | `| `L614` | `| `L809` | `| `L307` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L641` | `| `L615` | `| `L819` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L642` | `| `L616` | `| `L820` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L643` | `| `L617` | `| `L822` | `| `L684` | `curl -fsSL "https://bun.sh/install" -o "$tmp` | Unix network tools (use PowerShell or Python) |
| `L644` | `| `L618` | `| `L823` | `| `L685` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk ` | Unix text processing utilities (use PowerShell or Python) |
| `L646` | `| `L620` | `| `L825` | `| `L825` | `SAVED_HASH=$(cat ~/.gstack/projects/$SLUG/la` | Unix command (use PowerShell equivalent) |
| `L647` | `| `L621` | `| `L826` | `| `L826` | `CURRENT_HASH=$(sed -n '/## Deploy Configurat` | Unix text processing utilities (use PowerShell or Python) |
| `L648` | `| `L622` | `| `L828` | `| `L865` | `DEPLOY_CONFIG=$(grep -A 20 "## Deploy Config` | Unix text processing utilities (use PowerShell or Python) |
| `L649` | `| `L623` | `| `L829` | `| `L870` | `PROD_URL=$(echo "$DEPLOY_CONFIG" | grep -i "` | Unix text processing utilities (use PowerShell or Python) |
| `L650` | `| `L624` | `| `L830` | `| `L871` | `PLATFORM=$(echo "$DEPLOY_CONFIG" | grep -i "` | Unix text processing utilities (use PowerShell or Python) |
| `L651` | `| `L625` | `| `L831` | `| `L886` | `[ -f "$f" ] ; grep -qiE "deploy|release|prod` | Unix text processing utilities (use PowerShell or Python) |
| `L652` | `| `L626` | `| `L832` | `| `L887` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Out` | Unix text processing utilities (use PowerShell or Python) |
| `L653` | `| `L627` | `| `L833` | `| `L932` | `║  ├─ curl prod URL:      ✓ PASS (200 OK) / ` | Unix network tools (use PowerShell or Python) |
| `L654` | `| `L628` | `| `L834` | `| `L953` | `failed at Step 1). If `curl` fails, note "I ` | Unix network tools (use PowerShell or Python) |
| `L655` | `| `L629` | `| `L835` | `| `L966` | `grep -i "staging" CLAUDE.md | Out-Null | hea` | Unix text processing utilities (use PowerShell or Python) |
| `L656` | `| `L630` | `| `L836` | `| `L972` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Out` | Unix text processing utilities (use PowerShell or Python) |
| `L657` | `| `L631` | `| `L837` | `| `L1020` | `CURRENT_HASH=$(sed -n '/## Deploy Configura` | Unix text processing utilities (use PowerShell or Python) |
| `L658` | `| `L632` | `| `L839` | `| `L1130` | `cat $GSTACK_ROOT/review/checklist.md | Out-` | Unix command (use PowerShell equivalent) |
| `L659` | `| `L633` | `| `L840` | `| `L1164` | `ls -t ~/.gstack-dev/evals/*-e2e-*-$(date +%` | Unix command (use PowerShell equivalent) |
| `L660` | `| `L634` | `| `L841` | `| `L1180` | `ls -t ~/.gstack-dev/evals/*-llm-judge-*-$(d` | Unix command (use PowerShell equivalent) |
| `L661` | `| `L635` | `| `L842` | `| `L1210` | `git log --oneline --all-match --grep="docs:` | Unix text processing utilities (use PowerShell or Python) |
| `L662` | `| `L636` | `| `L843` | `| `L1365` | `DEPLOY_CONFIG=$(grep -A 20 "## Deploy Confi` | Unix text processing utilities (use PowerShell or Python) |
| `L663` | `| `L637` | `| `L844` | `| `L1370` | `PROD_URL=$(echo "$DEPLOY_CONFIG" | grep -i ` | Unix text processing utilities (use PowerShell or Python) |
| `L664` | `| `L638` | `| `L845` | `| `L1371` | `PLATFORM=$(echo "$DEPLOY_CONFIG" | grep -i ` | Unix text processing utilities (use PowerShell or Python) |
| `L665` | `| `L639` | `| `L846` | `| `L1386` | `[ -f "$f" ] ; grep -qiE "deploy|release|pro` | Unix text processing utilities (use PowerShell or Python) |
| `L666` | `| `L640` | `| `L847` | `| `L1387` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Ou` | Unix text processing utilities (use PowerShell or Python) |
| `L667` | `| `L641` | `| `L848` | `| `L1486` | `curl -sf {production-url} -o $null -w "%{ht` | Unix network tools (use PowerShell or Python) |
| `L668` | `| `L642` | `| `L857` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L669` | `| `L643` | `| `L858` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L670` | `| `L644` | `| `L860` | `| `L768` | `cat "$LEARN_FILE" | bun -e "` | Unix command` | Unix command (use PowerShell equivalent) |
| `L671` | `| `L645` | `| `L878` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L672` | `| `L646` | `| `L879` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L673` | `| `L647` | `| `L881` | `| `L694` | `curl -fsSL "https://bun.sh/install" -o "$tmp` | Unix network tools (use PowerShell or Python) |
| `L674` | `| `L648` | `| `L882` | `| `L695` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk ` | Unix text processing utilities (use PowerShell or Python) |
| `L675` | `| `L649` | `| `L883` | `| `L731` | `ls -t ~/.gstack/projects/$SLUG/*-design-*.md` | Unix command (use PowerShell equivalent) |
| `L676` | `| `L651` | `| `L885` | `| `L989` | `grep -li "<keyword1>\|<keyword2>\|<keyword3>` | Unix text processing utilities (use PowerShell or Python) |
| `L677` | `| `L652` | `| `L886` | `| `L1159` | `4. POST the new HTML to the running server ` | Unix network tools (use PowerShell or Python) |
| `L680` | `| `L655` | `| `L889` | `| `L1321` | `PRIOR=$(ls -t ~/.gstack/projects/$SLUG/*-$B` | Unix command (use PowerShell equivalent) |
| `L681` | `| `L656` | `| `L890` | `| `L1532` | `SESSION_TIER=$(echo "$PROFILE" | grep "^TIE` | Unix text processing utilities (use PowerShell or Python) |
| `L682` | `| `L657` | `| `L891` | `| `L1533` | `SESSION_COUNT=$(echo "$PROFILE" | grep "^SE` | Unix text processing utilities (use PowerShell or Python) |
| `L683` | `| `L658` | `| `L905` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L684` | `| `L659` | `| `L906` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L685` | `| `L660` | `| `L908` | `| `L689` | `curl -fsSL "https://bun.sh/install" -o "$tmp` | Unix network tools (use PowerShell or Python) |
| `L686` | `| `L661` | `| `L909` | `| `L690` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk ` | Unix text processing utilities (use PowerShell or Python) |
| `L687` | `| `L662` | `| `L910` | `| `L711` | `_OLD_PID=$(cat "$(git rev-parse --show-tople` | Unix command (use PowerShell equivalent) |
| `L688` | `| `L663` | `| `L911` | `| `L711` | `_OLD_PID=$(cat "$(git rev-parse --show-tople` | Unix command (use PowerShell equivalent) |
| `L689` | `| `L664` | `| `L912` | `| `L756` | `cat "$(git rev-parse --show-toplevel | Out-N` | Unix command (use PowerShell equivalent) |
| `L690` | `| `L665` | `| `L913` | `| `L756` | `cat "$(git rev-parse --show-toplevel | Out-N` | Unix command (use PowerShell equivalent) |
| `L691` | `| `L666` | `| `L922` | `| `L287` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L692` | `| `L667` | `| `L923` | `| `L290` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L693` | `| `L668` | `| `L925` | `| `L711` | `curl -fsSL "https://bun.sh/install" -o "$tmp` | Unix network tools (use PowerShell or Python) |
| `L694` | `| `L669` | `| `L926` | `| `L712` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk ` | Unix text processing utilities (use PowerShell or Python) |
| `L695` | `| `L670` | `| `L927` | `| `L908` | ``exec curl` syntax which OpenClaw understand` | Unix network tools (use PowerShell or Python) |
| `L696` | `| `L671` | `| `L928` | `| `L915` | `curl commands work directly. When using `--l` | Unix network tools (use PowerShell or Python) |
| `L697` | `| `L672` | `| `L937` | `| `L289` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L698` | `| `L673` | `| `L938` | `| `L292` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L700` | `| `L675` | `| `L941` | `| `L779` | `grep -r "TODO\|FIXME\|HACK\|XXX" -l --exclud` | Unix text processing utilities (use PowerShell or Python) |
| `L701` | `| `L676` | `| `L942` | `| `L789` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$B` | Unix command (use PowerShell equivalent) |
| `L702` | `| `L677` | `| `L943` | `| `L790` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/` | Unix command (use PowerShell equivalent) |
| `L703` | `| `L678` | `| `L944` | `| `L798` | `HANDOFF=$(ls -t ~/.gstack/projects/$SLUG/*-$` | Unix command (use PowerShell equivalent) |
| `L704` | `| `L679` | `| `L945` | `| `L860` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$B` | Unix command (use PowerShell equivalent) |
| `L705` | `| `L680` | `| `L946` | `| `L861` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/` | Unix command (use PowerShell equivalent) |
| `L706` | `| `L681` | `| `L955` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L707` | `| `L682` | `| `L956` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L709` | `| `L684` | `| `L959` | `| `L980` | `- `mkdir -p ~/.gstack/projects/$SLUG/designs` | Unix nested directory creation (use PowerShell equivalent) |
| `L710` | `| `L685` | `| `L960` | `| `L1057` | `cat "$_DESIGN_DIR/feedback.json"` | Unix co` | Unix command (use PowerShell equivalent) |
| `L711` | `| `L686` | `| `L961` | `| `L1060` | `cat "$_DESIGN_DIR/feedback-pending.json"` |` | Unix command (use PowerShell equivalent) |
| `L712` | `| `L687` | `| `L962` | `| `L1089` | ``curl -s -X POST http://127.0.0.1:PORT/api/` | Unix network tools (use PowerShell or Python) |
| `L713` | `| `L688` | `| `L976` | `| `L296` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L714` | `| `L689` | `| `L977` | `| `L299` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L716` | `| `L691` | `| `L981` | `| `L832` | `- Getting started guides (grep README for "G` | Unix text processing utilities (use PowerShell or Python) |
| `L717` | `| `L692` | `| `L982` | `| `L833` | `- CLI help text (grep for `--help`, `usage:`` | Unix text processing utilities (use PowerShell or Python) |
| `L718` | `| `L693` | `| `L983` | `| `L834` | `- Error message patterns (grep for `throw ne` | Unix text processing utilities (use PowerShell or Python) |
| `L719` | `| `L694` | `| `L984` | `| `L842` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$B` | Unix command (use PowerShell equivalent) |
| `L720` | `| `L695` | `| `L985` | `| `L843` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/` | Unix command (use PowerShell equivalent) |
| `L721` | `| `L696` | `| `L986` | `| `L902` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$B` | Unix command (use PowerShell equivalent) |
| `L722` | `| `L697` | `| `L987` | `| `L903` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/` | Unix command (use PowerShell equivalent) |
| `L723` | `| `L698` | `| `L988` | `| `L1264` | `$GSTACK_ROOT/bin/gstack-review-read | Out-N` | Unix text processing utilities (use PowerShell or Python) |
| `L724` | `| `L699` | `| `L997` | `| `L291` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_` | Unix text processing utilities (use PowerShell or Python) |
| `L725` | `| `L700` | `| `L998` | `| `L294` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANC` | Unix text processing utilities (use PowerShell or Python) |
| `L726` | `| `L701` | `| `L1000` | `| `L720` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$` | Unix command (use PowerShell equivalent) |
| `L727` | `| `L702` | `| `L1001` | `| `L721` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack` | Unix command (use PowerShell equivalent) |
| `L728` | `| `L703` | `| `L1002` | `| `L775` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$` | Unix command (use PowerShell equivalent) |
| `L729` | `| `L704` | `| `L1003` | `| `L776` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack` | Unix command (use PowerShell equivalent) |
| `L730` | `| `L705` | `| `L1004` | `| `L896` | `ls jest.config.* vitest.config.* playwright` | Unix command (use PowerShell equivalent) |
| `L731` | `| `L706` | `| `L1005` | `| `L897` | `ls -d test/ tests/ spec/ __tests__/ cypress` | Unix command (use PowerShell equivalent) |
| `L732` | `| `L707` | `| `L1014` | `| `L296` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$` | Unix text processing utilities (use PowerShell or Python) |
| `L733` | `| `L708` | `| `L1015` | `| `L299` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRAN` | Unix text processing utilities (use PowerShell or Python) |
| `L734` | `| `L709` | `| `L1025` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$` | Unix text processing utilities (use PowerShell or Python) |
| `L735` | `| `L710` | `| `L1026` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRAN` | Unix text processing utilities (use PowerShell or Python) |
| `L736` | `| `L711` | `| `L1028` | `| `L707` | `curl -fsSL "https://bun.sh/install" -o "$tm` | Unix network tools (use PowerShell or Python) |
| `L737` | `| `L712` | `| `L1029` | `| `L708` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk` | Unix text processing utilities (use PowerShell or Python) |
| `L738` | `| `L713` | `| `L1030` | `| `L748` | `ls -t ~/.gstack/projects/$SLUG/*-test-plan-` | Unix command (use PowerShell equivalent) |
| `L739` | `| `L714` | `| `L1044` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$` | Unix text processing utilities (use PowerShell or Python) |
| `L740` | `| `L715` | `| `L1045` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRAN` | Unix text processing utilities (use PowerShell or Python) |
| `L742` | `| `L717` | `| `L1048` | `| `L738` | `$B status | Out-Null | grep -q "Mode: cdp" ` | Unix text processing utilities (use PowerShell or Python) |
| `L743` | `| `L718` | `| `L1049` | `| `L785` | `curl -fsSL "https://bun.sh/install" -o "$tm` | Unix network tools (use PowerShell or Python) |
| `L744` | `| `L719` | `| `L1050` | `| `L786` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk` | Unix text processing utilities (use PowerShell or Python) |
| `L745` | `| `L720` | `| `L1051` | `| `L815` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | ` | Unix text processing utilities (use PowerShell or Python) |
| `L746` | `| `L721` | `| `L1052` | `| `L816` | `[ -f package.json ] ; grep -q '"next"' pack` | Unix text processing utilities (use PowerShell or Python) |
| `L747` | `| `L722` | `| `L1053` | `| `L818` | `ls jest.config.* vitest.config.* playwright` | Unix command (use PowerShell equivalent) |
| `L748` | `| `L723` | `| `L1054` | `| `L819` | `ls -d test/ tests/ spec/ __tests__/ cypress` | Unix command (use PowerShell equivalent) |
| `L749` | `| `L724` | `| `L1055` | `| `L904` | `ls -d .github/ | Out-Null ; echo "CI:github` | Unix command (use PowerShell equivalent) |
| `L750` | `| `L725` | `| `L1056` | `| `L905` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | ` | Unix command (use PowerShell equivalent) |
| `L751` | `| `L726` | `| `L1057` | `| `L981` | `ls -t ~/.gstack/projects/$SLUG/*-test-plan-` | Unix command (use PowerShell equivalent) |
| `L752` | `| `L727` | `| `L1071` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$` | Unix text processing utilities (use PowerShell or Python) |
| `L753` | `| `L728` | `| `L1072` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRAN` | Unix text processing utilities (use PowerShell or Python) |
| `L756` | `| `L732` | `| `L1077` | `| `L782` | `cat ~/.gstack/greptile-history.md | Out-Nul` | Unix command (use PowerShell equivalent) |
| `L757` | `| `L733` | `| `L1078` | `| `L785` | `cat TODOS.md | Out-Null ; true` | Unix comm` | Unix command (use PowerShell equivalent) |
| `L759` | `| `L735` | `| `L1081` | `| `L794` | `cat ~/.gstack/analytics/skill-usage.jsonl |` | Unix command (use PowerShell equivalent) |
| `L760` | `| `L737` | `| `L1083` | `| `L1029` | `ls -t .context/retros/*.json | Out-Null` |` | Unix command (use PowerShell equivalent) |
| `L761` | `| `L738` | `| `L1084` | `| `L1058` | `existing=$(ls .context/retros/${today}-*.j` | Unix command (use PowerShell equivalent) |
| `L762` | `| `L739` | `| `L1085` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jso` | Unix command (use PowerShell equivalent) |
| `L763` | `| `L739` | `| `L1085` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jso` | Unix command (use PowerShell equivalent) |
| `L764` | `| `L740` | `| `L1085` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jso` | Unix command (use PowerShell equivalent) |
| `L765` | `| `L740` | `| `L1085` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jso` | Unix command (use PowerShell equivalent) |
| `L766` | `| `L741` | `| `L1086` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jso` | Unix command (use PowerShell equivalent) |
| `L767` | `| `L741` | `| `L1086` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jso` | Unix command (use PowerShell equivalent) |
| `L768` | `| `L742` | `| `L1086` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jso` | Unix command (use PowerShell equivalent) |
| `L769` | `| `L742` | `| `L1086` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jso` | Unix command (use PowerShell equivalent) |
| `L770` | `| `L743` | `| `L1088` | `| `L1482` | `ls -t ~/.gstack/retros/global-*.json | Out` | Unix command (use PowerShell equivalent) |
| `L771` | `| `L744` | `| `L1089` | `| `L1501` | `existing=$(ls ~/.gstack/retros/global-${to` | Unix command (use PowerShell equivalent) |
| `L772` | `| `L745` | `| `L1103` | `| `L287` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$` | Unix text processing utilities (use PowerShell or Python) |
| `L773` | `| `L746` | `| `L1104` | `| `L290` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRAN` | Unix text processing utilities (use PowerShell or Python) |
| `L775` | `| `L748` | `| `L1107` | `| `L764` | `_PLAN_SLUG=$(git remote get-url origin | Ou` | Unix text processing utilities (use PowerShell or Python) |
| `L776` | `| `L749` | `| `L1108` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix text processing utilities (use PowerShell or Python) |
| `L776` | `| `L749` | `| `L1108` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L777` | `| `L749` | `| `L1108` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix text processing utilities (use PowerShell or Python) |
| `L777` | `| `L749` | `| `L1108` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L778` | `| `L750` | `| `L1108` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix text processing utilities (use PowerShell or Python) |
| `L778` | `| `L750` | `| `L1108` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L779` | `| `L750` | `| `L1108` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix text processing utilities (use PowerShell or Python) |
| `L779` | `| `L750` | `| `L1108` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L780` | `| `L751` | `| `L1109` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix text processing utilities (use PowerShell or Python) |
| `L780` | `| `L751` | `| `L1109` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L781` | `| `L751` | `| `L1109` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix text processing utilities (use PowerShell or Python) |
| `L781` | `| `L751` | `| `L1109` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L782` | `| `L752` | `| `L1109` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix text processing utilities (use PowerShell or Python) |
| `L782` | `| `L752` | `| `L1109` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L783` | `| `L752` | `| `L1109` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix text processing utilities (use PowerShell or Python) |
| `L783` | `| `L752` | `| `L1109` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L784` | `| `L753` | `| `L1110` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*` | Unix command (use PowerShell equivalent) |
| `L785` | `| `L754` | `| `L1110` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*` | Unix command (use PowerShell equivalent) |
| `L786` | `| `L755` | `| `L1111` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*` | Unix command (use PowerShell equivalent) |
| `L787` | `| `L756` | `| `L1111` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*` | Unix command (use PowerShell equivalent) |
| `L788` | `| `L757` | `| `L1120` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L788` | `| `L757` | `| `L1120` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L789` | `| `L757` | `| `L1120` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L789` | `| `L757` | `| `L1120` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L790` | `| `L758` | `| `L1120` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L790` | `| `L758` | `| `L1120` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L791` | `| `L758` | `| `L1120` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L791` | `| `L758` | `| `L1120` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L792` | `| `L759` | `| `L1121` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L792` | `| `L759` | `| `L1121` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L793` | `| `L759` | `| `L1121` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L793` | `| `L759` | `| `L1121` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L794` | `| `L760` | `| `L1121` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L794` | `| `L760` | `| `L1121` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L795` | `| `L760` | `| `L1121` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L795` | `| `L760` | `| `L1121` | `| `L334` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L796` | `| `L761` | `| `L1123` | `| `L370` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$` | Unix text processing utilities (use PowerShell or Python) |
| `L797` | `| `L762` | `| `L1124` | `| `L373` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRAN` | Unix text processing utilities (use PowerShell or Python) |
| `L798` | `| `L763` | `| `L1133` | `| `L389` | `$B status | Out-Null | grep -q "Mode: cdp" ` | Unix text processing utilities (use PowerShell or Python) |
| `L799` | `| `L764` | `| `L1134` | `| `L427` | `curl -fsSL "https://bun.sh/install" -o "$tm` | Unix network tools (use PowerShell or Python) |
| `L800` | `| `L765` | `| `L1135` | `| `L428` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk` | Unix text processing utilities (use PowerShell or Python) |
| `L801` | `| `L766` | `| `L1144` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$` | Unix text processing utilities (use PowerShell or Python) |
| `L802` | `| `L767` | `| `L1145` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRAN` | Unix text processing utilities (use PowerShell or Python) |
| `L803` | `| `L768` | `| `L1147` | `| `L662` | `grep -A 20 "## Deploy Configuration" CLAUDE` | Unix text processing utilities (use PowerShell or Python) |
| `L804` | `| `L769` | `| `L1148` | `| `L681` | `[ -f fly.toml ] ; echo "PLATFORM:fly" ; cat` | Unix command (use PowerShell equivalent) |
| `L805` | `| `L770` | `| `L1149` | `| `L682` | `[ -f render.yaml ] ; echo "PLATFORM:render"` | Unix command (use PowerShell equivalent) |
| `L806` | `| `L771` | `| `L1150` | `| `L684` | `[ -f netlify.toml ] ; echo "PLATFORM:netlif` | Unix command (use PowerShell equivalent) |
| `L807` | `| `L772` | `| `L1151` | `| `L690` | `[ -f "$f" ] ; grep -qiE "deploy|release|pro` | Unix text processing utilities (use PowerShell or Python) |
| `L808` | `| `L773` | `| `L1152` | `| `L694` | `[ -f package.json ] ; grep -q '"bin"' packa` | Unix text processing utilities (use PowerShell or Python) |
| `L809` | `| `L774` | `| `L1153` | `| `L695` | `find . -maxdepth 1 -name '*.gemspec' | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L810` | `| `L775` | `| `L1154` | `| `L706` | `1. Extract app name: `grep -m1 "^app" fly.t` | Unix text processing utilities (use PowerShell or Python) |
| `L811` | `| `L776` | `| `L1155` | `| `L734` | `2. If installed: `vercel ls --prod 2>/dev/n` | Unix command (use PowerShell equivalent) |
| `L812` | `| `L777` | `| `L1156` | `| `L807` | `curl -sf "{health-check-url}" -o $null -w "` | Unix network tools (use PowerShell or Python) |
| `L813` | `| `L778` | `| `L1165` | `| `L289` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$` | Unix text processing utilities (use PowerShell or Python) |
| `L814` | `| `L779` | `| `L1166` | `| `L292` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRAN` | Unix text processing utilities (use PowerShell or Python) |
| `L816` | `| `L781` | `| `L1169` | `| `L829` | `git diff origin/<base> --name-only | grep -` | Unix text processing utilities (use PowerShell or Python) |
| `L817` | `| `L782` | `| `L1170` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix text processing utilities (use PowerShell or Python) |
| `L817` | `| `L782` | `| `L1170` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix command (use PowerShell equivalent) |
| `L818` | `| `L782` | `| `L1170` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix text processing utilities (use PowerShell or Python) |
| `L818` | `| `L782` | `| `L1170` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix command (use PowerShell equivalent) |
| `L819` | `| `L783` | `| `L1170` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix text processing utilities (use PowerShell or Python) |
| `L819` | `| `L783` | `| `L1170` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix command (use PowerShell equivalent) |
| `L820` | `| `L783` | `| `L1170` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix text processing utilities (use PowerShell or Python) |
| `L820` | `| `L783` | `| `L1170` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix command (use PowerShell equivalent) |
| `L821` | `| `L784` | `| `L1171` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix text processing utilities (use PowerShell or Python) |
| `L821` | `| `L784` | `| `L1171` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix command (use PowerShell equivalent) |
| `L822` | `| `L784` | `| `L1171` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix text processing utilities (use PowerShell or Python) |
| `L822` | `| `L784` | `| `L1171` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix command (use PowerShell equivalent) |
| `L823` | `| `L785` | `| `L1171` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix text processing utilities (use PowerShell or Python) |
| `L823` | `| `L785` | `| `L1171` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix command (use PowerShell equivalent) |
| `L824` | `| `L785` | `| `L1171` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix text processing utilities (use PowerShell or Python) |
| `L824` | `| `L785` | `| `L1171` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE` | Unix command (use PowerShell equivalent) |
| `L825` | `| `L786` | `| `L1172` | `| `L835` | `grep -qE 'release|publish|deploy' .gitlab-c` | Unix text processing utilities (use PowerShell or Python) |
| `L826` | `| `L787` | `| `L1173` | `| `L881` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | ` | Unix text processing utilities (use PowerShell or Python) |
| `L827` | `| `L788` | `| `L1174` | `| `L882` | `[ -f package.json ] ; grep -q '"next"' pack` | Unix text processing utilities (use PowerShell or Python) |
| `L828` | `| `L789` | `| `L1175` | `| `L884` | `ls jest.config.* vitest.config.* playwright` | Unix command (use PowerShell equivalent) |
| `L829` | `| `L790` | `| `L1176` | `| `L885` | `ls -d test/ tests/ spec/ __tests__/ cypress` | Unix command (use PowerShell equivalent) |
| `L830` | `| `L791` | `| `L1177` | `| `L970` | `ls -d .github/ | Out-Null ; echo "CI:github` | Unix command (use PowerShell equivalent) |
| `L831` | `| `L792` | `| `L1178` | `| `L971` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | ` | Unix command (use PowerShell equivalent) |
| `L832` | `| `L793` | `| `L1179` | `| `L1176` | `grep -l "changed_file_basename" test/evals` | Unix text processing utilities (use PowerShell or Python) |
| `L833` | `| `L794` | `| `L1180` | `| `L1183` | `- Changes to `config/system_prompts/*.txt`` | Unix text processing utilities (use PowerShell or Python) |
| `L834` | `| `L795` | `| `L1181` | `| `L1238` | `ls jest.config.* vitest.config.* playwrigh` | Unix command (use PowerShell equivalent) |
| `L835` | `| `L796` | `| `L1182` | `| `L1239` | `ls -d test/ tests/ spec/ __tests__/ cypres` | Unix command (use PowerShell equivalent) |
| `L837` | `| `L798` | `| `L1186` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix text processing utilities (use PowerShell or Python) |
| `L837` | `| `L798` | `| `L1186` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L838` | `| `L798` | `| `L1186` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix text processing utilities (use PowerShell or Python) |
| `L838` | `| `L798` | `| `L1186` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L839` | `| `L799` | `| `L1186` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix text processing utilities (use PowerShell or Python) |
| `L839` | `| `L799` | `| `L1186` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L840` | `| `L799` | `| `L1186` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix text processing utilities (use PowerShell or Python) |
| `L840` | `| `L799` | `| `L1186` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L841` | `| `L800` | `| `L1187` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix text processing utilities (use PowerShell or Python) |
| `L841` | `| `L800` | `| `L1187` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L842` | `| `L800` | `| `L1187` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix text processing utilities (use PowerShell or Python) |
| `L842` | `| `L800` | `| `L1187` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L843` | `| `L801` | `| `L1187` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix text processing utilities (use PowerShell or Python) |
| `L843` | `| `L801` | `| `L1187` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L844` | `| `L801` | `| `L1187` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix text processing utilities (use PowerShell or Python) |
| `L844` | `| `L801` | `| `L1187` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L845` | `| `L802` | `| `L1188` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/` | Unix command (use PowerShell equivalent) |
| `L846` | `| `L803` | `| `L1188` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/` | Unix command (use PowerShell equivalent) |
| `L847` | `| `L804` | `| `L1189` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/` | Unix command (use PowerShell equivalent) |
| `L848` | `| `L805` | `| `L1189` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/` | Unix command (use PowerShell equivalent) |
| `L849` | `| `L806` | `| `L1191` | `| `L1647` | `curl -s -o $null -w '%{http_code}' http://` | Unix network tools (use PowerShell or Python) |
| `L850` | `| `L807` | `| `L1192` | `| `L1648` | `curl -s -o $null -w '%{http_code}' http://` | Unix network tools (use PowerShell or Python) |
| `L851` | `| `L808` | `| `L1193` | `| `L1649` | `curl -s -o $null -w '%{http_code}' http://` | Unix network tools (use PowerShell or Python) |
| `L852` | `| `L809` | `| `L1194` | `| `L1650` | `curl -s -o $null -w '%{http_code}' http://` | Unix network tools (use PowerShell or Python) |
| `L853` | `| `L810` | `| `L1195` | `| `L1660` | `cat ${CLAUDE_SKILL_DIR}/../qa-only/SKILL.m` | Unix command (use PowerShell equivalent) |
| `L854` | `| `L811` | `| `L1196` | `| `L1964` | `CURRENT_VERSION=$(cat VERSION | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L855` | `| `L812` | `| `L1197` | `| `L2029` | `if ! printf '%s' "$NEW_VERSION" | grep -qE` | Unix text processing utilities (use PowerShell or Python) |
| `L856` | `| `L813` | `| `L1198` | `| `L2055` | `REPAIR_VERSION=$(cat VERSION | tr -d '\r\n` | Unix command (use PowerShell equivalent) |
| `L857` | `| `L814` | `| `L1199` | `| `L2056` | `if ! printf '%s' "$REPAIR_VERSION" | grep ` | Unix text processing utilities (use PowerShell or Python) |
| `L858` | `| `L815` | `| `L1200` | `| `L2203` | `git commit -m "$(cat <<'EOF'` | Unix comma` | Unix command (use PowerShell equivalent) |
| `L860` | `| `L818` | `| `L1210` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L860` | `| `L818` | `| `L1210` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L861` | `| `L818` | `| `L1210` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L861` | `| `L818` | `| `L1210` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L862` | `| `L819` | `| `L1210` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L862` | `| `L819` | `| `L1210` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L863` | `| `L819` | `| `L1210` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L863` | `| `L819` | `| `L1210` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L864` | `| `L820` | `| `L1211` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L864` | `| `L820` | `| `L1211` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L865` | `| `L820` | `| `L1211` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L865` | `| `L820` | `| `L1211` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L866` | `| `L821` | `| `L1211` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L866` | `| `L821` | `| `L1211` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L867` | `| `L821` | `| `L1211` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix text processing utilities (use PowerShell or Python) |
| `L867` | `| `L821` | `| `L1211` | `| `L358` | `equivalents (cat, sed, find, grep). The ded` | Unix command (use PowerShell equivalent) |
| `L868` | `| `L822` | `| `L1219` | `| `L42` | `PREV=$(cat "$STATE_DIR/freeze-dir.txt")` | U` | Unix command (use PowerShell equivalent) |
| `L869` | `| `L823` | `| `L1227` | `| `L71` | `_SNOOZED_VER=$(awk '{print $1}' "$_SNOOZE_FI` | Unix text processing utilities (use PowerShell or Python) |
| `L870` | `| `L824` | `| `L1228` | `| `L73` | `_CUR_LEVEL=$(awk '{print $2}' "$_SNOOZE_FILE` | Unix text processing utilities (use PowerShell or Python) |
| `L871` | `| `L825` | `| `L1229` | `| `L127` | `OLD_VERSION=$(cat "$INSTALL_DIR/VERSION" | ` | Unix command (use PowerShell equivalent) |
| `L872` | `| `L826` | `| `L1230` | `| `L179` | `if ! grep -qF '.agents/skills/gstack/' .git` | Unix text processing utilities (use PowerShell or Python) |
| `L873` | `| `L827` | `| `L1231` | `| `L214` | `m_ver="$(basename "$migration" .sh | sed 's` | Unix text processing utilities (use PowerShell or Python) |
| `L874` | `| `L828` | `| `L1232` | `| `L283` | `PRIMARY_VER=$(cat "$INSTALL_DIR/VERSION" | ` | Unix command (use PowerShell equivalent) |
| `L875` | `| `L829` | `| `L1233` | `| `L284` | `LOCAL_VER=$(cat "$LOCAL_GSTACK/VERSION" | O` | Unix command (use PowerShell equivalent) |
| `L876` | `| `L830` | `| `L1241` | `| `L446` | `curl -fsSL "https://bun.sh/install" -o "$tm` | Unix network tools (use PowerShell or Python) |
| `L877` | `| `L831` | `| `L1242` | `| `L447` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk` | Unix text processing utilities (use PowerShell or Python) |
| `L878` | `| `L832` | `| `L1243` | `| `L470` | `> Set them before running: `export TEST_EMA` | Unix environment variable export (use PowerShell equivalent) |
| `L879` | `| `L833` | `| `L1257` | `| `L64` | `_SNOOZED_VER=$(awk '{print $1}' "$_SNOOZE_FI` | Unix text processing utilities (use PowerShell or Python) |
| `L880` | `| `L834` | `| `L1258` | `| `L66` | `_CUR_LEVEL=$(awk '{print $2}' "$_SNOOZE_FILE` | Unix text processing utilities (use PowerShell or Python) |
| `L881` | `| `L835` | `| `L1259` | `| `L120` | `OLD_VERSION=$(cat "$INSTALL_DIR/VERSION" | ` | Unix command (use PowerShell equivalent) |
| `L882` | `| `L836` | `| `L1260` | `| `L172` | `if ! grep -qF '.agents/skills/gstack/' .git` | Unix text processing utilities (use PowerShell or Python) |
| `L883` | `| `L837` | `| `L1261` | `| `L207` | `m_ver="$(basename "$migration" .sh | sed 's` | Unix text processing utilities (use PowerShell or Python) |
| `L884` | `| `L838` | `| `L1262` | `| `L276` | `PRIMARY_VER=$(cat "$INSTALL_DIR/VERSION" | ` | Unix command (use PowerShell equivalent) |
| `L885` | `| `L839` | `| `L1263` | `| `L277` | `LOCAL_VER=$(cat "$LOCAL_GSTACK/VERSION" | O` | Unix command (use PowerShell equivalent) |
| `L887` | `| `L842` | `| `L1280` | `| `L25` | `- **[HIGH]** — Reliably detectable via grep/` | Unix text processing utilities (use PowerShell or Python) |
| `L888` | `| `L843` | `| `L1289` | `| `L5` | `if ($content -like "*mkdir -p*") { throw "FAI` | Unix nested directory creation (use PowerShell equivalent) |
| `L889` | `| `L849` | `| `L101` | `| `L141` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L890` | `| `L850` | `| `L104` | `| `L148` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L891` | `| `L851` | `| `L159` | `| `L244` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L892` | `| `L852` | `| `L166` | `| `L254` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L893` | `| `L853` | `| `L184` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L894` | `| `L854` | `| `L185` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L895` | `| `L855` | `| `L186` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L896` | `| `L856` | `| `L187` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L897` | `| `L857` | `| `L188` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L898` | `| `L858` | `| `L192` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L899` | `| `L859` | `| `L193` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L900` | `| `L860` | `| `L194` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L901` | `| `L862` | `| `L442` | `| `L141` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L902` | `| `L863` | `| `L443` | `| `L148` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L903` | `| `L865` | `| `L445` | `| `L244` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L904` | `| `L867` | `| `L447` | `| `L254` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L905` | `| `L869` | `| `L449` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L906` | `| `L870` | `| `L450` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L907` | `| `L871` | `| `L451` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L908` | `| `L876` | `| `L456` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L909` | `| `L880` | `| `L460` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L910` | `| `L890` | `| `L555` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Unix force-remove command (use PowerShell equivalent) |
| `L911` | `| `L891` | `| `L562` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Unix force-remove command (use PowerShell equivalent) |
| `L912` | `| `L893` | `| `L658` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Unix command (use PowerShell equivalent) |
| `L913` | `| `L895` | `| `L668` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Unix command (use PowerShell equivalent) |
| `L914` | `| `L897` | `| `L709` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Unix command (use PowerShell equivalent) |
| `L915` | `| `L898` | `| `L710` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L916` | `| `L899` | `| `L711` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L917` | `| `L904` | `| `L723` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Unix command (use PowerShell equivalent) |
| `L918` | `| `L908` | `| `L727` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L919` | `| `L924` | `| `L82` | `Also, sanitize any Unix commands (like `mkdir -p` or `fin` | Unix nested directory creation (use PowerShell equivalent) |
| `L920` | `| `L925` | `| `L92` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdi` | Unix nested directory creation (use PowerShell equivalent) |
| `L921` | `| `L926` | `| `L155` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkd` | Unix nested directory creation (use PowerShell equivalent) |
| `L922` | `| `L927` | `| `L208` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkd` | Unix nested directory creation (use PowerShell equivalent) |
| `L923` | `| `L935` | `| `L76` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdi` | Unix nested directory creation (use PowerShell equivalent) |
| `L924` | `| `L936` | `| `L150` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkd` | Unix nested directory creation (use PowerShell equivalent) |
| `L925` | `| `L958` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timelin` | Unix text processing utilities (use PowerShell or Python) |
| `L926` | `| `L959` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PRO` | Unix text processing utilities (use PowerShell or Python) |
| `L927` | `| `L961` | `| `L698` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/nul` | Unix text processing utilities (use PowerShell or Python) |
| `L928` | `| `L962` | `| `L759` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design` | Unix command (use PowerShell equivalent) |
| `L929` | `| `L963` | `| `L760` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SL` | Unix command (use PowerShell equivalent) |
| `L930` | `| `L964` | `| `L922` | `- Discover design docs: `ls -t ~/.gstack/projects/$SLUG/` | Unix command (use PowerShell equivalent) |
| `L931` | `| `L965` | `| `L923` | `- Detect UI scope: grep the plan for view/rendering term` | Unix text processing utilities (use PowerShell or Python) |
| `L932` | `| `L966` | `| `L926` | `- Detect DX scope: grep the plan for developer-facing te` | Unix text processing utilities (use PowerShell or Python) |
| `L933` | `| `L974` | `| `L410` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Uni` | Unix network tools (use PowerShell or Python) |
| `L934` | `| `L975` | `| `L411` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}'` | Unix text processing utilities (use PowerShell or Python) |
| `L935` | `| `L983` | `| `L412` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Uni` | Unix network tools (use PowerShell or Python) |
| `L936` | `| `L984` | `| `L413` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}'` | Unix text processing utilities (use PowerShell or Python) |
| `L937` | `| `L999` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timelin` | Unix text processing utilities (use PowerShell or Python) |
| `L938` | `| `L1000` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L939` | `| `L1002` | `| `L666` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Un` | Unix network tools (use PowerShell or Python) |
| `L940` | `| `L1003` | `| `L667` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}` | Unix text processing utilities (use PowerShell or Python) |
| `L941` | `| `L1004` | `| `L706` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/nu` | Unix text processing utilities (use PowerShell or Python) |
| `L942` | `| `L1012` | `| `L5` | `Safety guardrails for destructive commands. Warns before ` | Unix force-remove command (use PowerShell equivalent) |
| `L943` | `| `L1014` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/d` | Unix force-remove command (use PowerShell equivalent) |
| `L944` | `| `L1015` | `| `L60` | `| `docker rm -f` / `docker system prune` | `docker syste` | Unix force-remove command (use PowerShell equivalent) |
| `L945` | `| `L1016` | `| `L65` | `- `rm -rf node_modules` / `.next` / `dist` / `__pycache_` | Unix force-remove command (use PowerShell equivalent) |
| `L946` | `| `L1021` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/d` | Unix force-remove command (use PowerShell equivalent) |
| `L947` | `| `L1030` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L948` | `| `L1031` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L951` | `| `L1042` | `| `L343` | `_GBRAIN_VERSION_OK=$(gbrain --version  | grep -c '^gbra` | Unix text processing utilities (use PowerShell or Python) |
| `L952` | `| `L1043` | `| `L391` | `_BRAIN_LAST=$(cat "$_BRAIN_LAST_PULL_FILE"  || echo 0)`` | Unix command (use PowerShell equivalent) |
| `L953` | `| `L1045` | `| `L411` | `[ -f "$_GSTACK_HOME/.brain-last-push" ] ; _BRAIN_LAST_P` | Unix command (use PowerShell equivalent) |
| `L954` | `| `L1046` | `| `L463` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix text processing utilities (use PowerShell or Python) |
| `L954` | `| `L1046` | `| `L463` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix command (use PowerShell equivalent) |
| `L955` | `| `L1046` | `| `L463` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix text processing utilities (use PowerShell or Python) |
| `L955` | `| `L1046` | `| `L463` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix command (use PowerShell equivalent) |
| `L956` | `| `L1047` | `| `L463` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix text processing utilities (use PowerShell or Python) |
| `L956` | `| `L1047` | `| `L463` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix command (use PowerShell equivalent) |
| `L957` | `| `L1047` | `| `L463` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix text processing utilities (use PowerShell or Python) |
| `L957` | `| `L1047` | `| `L463` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix command (use PowerShell equivalent) |
| `L958` | `| `L1049` | `| `L494` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L959` | `| `L1050` | `| `L496` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L961` | `| `L1052` | `| `L761` | ``ls -1t` (filesystem mtime). Filenames are stable acros` | Unix command (use PowerShell equivalent) |
| `L962` | `| `L1060` | `| `L342` | `_GBRAIN_VERSION_OK=$(gbrain --version  | grep -c '^gbra` | Unix text processing utilities (use PowerShell or Python) |
| `L963` | `| `L1061` | `| `L390` | `_BRAIN_LAST=$(cat "$_BRAIN_LAST_PULL_FILE"  || echo 0)`` | Unix command (use PowerShell equivalent) |
| `L964` | `| `L1063` | `| `L410` | `[ -f "$_GSTACK_HOME/.brain-last-push" ] ; _BRAIN_LAST_P` | Unix command (use PowerShell equivalent) |
| `L965` | `| `L1064` | `| `L462` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix text processing utilities (use PowerShell or Python) |
| `L965` | `| `L1064` | `| `L462` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix command (use PowerShell equivalent) |
| `L966` | `| `L1064` | `| `L462` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix text processing utilities (use PowerShell or Python) |
| `L966` | `| `L1064` | `| `L462` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix command (use PowerShell equivalent) |
| `L967` | `| `L1065` | `| `L462` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix text processing utilities (use PowerShell or Python) |
| `L967` | `| `L1065` | `| `L462` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix command (use PowerShell equivalent) |
| `L968` | `| `L1065` | `| `L462` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix text processing utilities (use PowerShell or Python) |
| `L968` | `| `L1065` | `| `L462` | `equivalents (cat, sed, Get-ChildItem, grep). The dedica` | Unix command (use PowerShell equivalent) |
| `L969` | `| `L1067` | `| `L493` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L970` | `| `L1068` | `| `L495` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L972` | `| `L1078` | `| `L294` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L973` | `| `L1079` | `| `L297` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L974` | `| `L1082` | `| `L700` | `ls package.json tsconfig.json | Out-Null ; echo "STACK:` | Unix command (use PowerShell equivalent) |
| `L975` | `| `L1083` | `| `L701` | `ls Gemfile | Out-Null ; echo "STACK: Ruby"` | Unix comm` | Unix command (use PowerShell equivalent) |
| `L976` | `| `L1084` | `| `L702` | `ls requirements.txt pyproject.toml setup.py | Out-Null ` | Unix command (use PowerShell equivalent) |
| `L977` | `| `L1085` | `| `L703` | `ls go.mod | Out-Null ; echo "STACK: Go"` | Unix command` | Unix command (use PowerShell equivalent) |
| `L978` | `| `L1086` | `| `L704` | `ls Cargo.toml | Out-Null ; echo "STACK: Rust"` | Unix c` | Unix command (use PowerShell equivalent) |
| `L979` | `| `L1087` | `| `L705` | `ls pom.xml build.gradle | Out-Null ; echo "STACK: JVM"`` | Unix command (use PowerShell equivalent) |
| `L980` | `| `L1088` | `| `L706` | `ls composer.json | Out-Null ; echo "STACK: PHP"` | Unix` | Unix command (use PowerShell equivalent) |
| `L982` | `| `L1090` | `| `L712` | `grep -q "next" package.json | Out-Null ; echo "FRAMEWOR` | Unix text processing utilities (use PowerShell or Python) |
| `L983` | `| `L1091` | `| `L713` | `grep -q "express" package.json | Out-Null ; echo "FRAME` | Unix text processing utilities (use PowerShell or Python) |
| `L984` | `| `L1092` | `| `L714` | `grep -q "fastify" package.json | Out-Null ; echo "FRAME` | Unix text processing utilities (use PowerShell or Python) |
| `L985` | `| `L1093` | `| `L715` | `grep -q "hono" package.json | Out-Null ; echo "FRAMEWOR` | Unix text processing utilities (use PowerShell or Python) |
| `L986` | `| `L1094` | `| `L716` | `grep -q "django" requirements.txt pyproject.toml | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L987` | `| `L1095` | `| `L717` | `grep -q "fastapi" requirements.txt pyproject.toml | Out` | Unix text processing utilities (use PowerShell or Python) |
| `L988` | `| `L1096` | `| `L718` | `grep -q "flask" requirements.txt pyproject.toml | Out-N` | Unix text processing utilities (use PowerShell or Python) |
| `L989` | `| `L1097` | `| `L719` | `grep -q "rails" Gemfile | Out-Null ; echo "FRAMEWORK: R` | Unix text processing utilities (use PowerShell or Python) |
| `L990` | `| `L1098` | `| `L720` | `grep -q "gin-gonic" go.mod | Out-Null ; echo "FRAMEWORK` | Unix text processing utilities (use PowerShell or Python) |
| `L991` | `| `L1099` | `| `L721` | `grep -q "spring-boot" pom.xml build.gradle | Out-Null ;` | Unix text processing utilities (use PowerShell or Python) |
| `L992` | `| `L1100` | `| `L722` | `grep -q "laravel" composer.json | Out-Null ; echo "FRAM` | Unix text processing utilities (use PowerShell or Python) |
| `L993` | `| `L1101` | `| `L759` | `ls .env .env.* | Out-Null` | Unix command (use PowerShe` | Unix command (use PowerShell equivalent) |
| `L994` | `| `L1102` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.ex` | Unix text processing utilities (use PowerShell or Python) |
| `L994` | `| `L1102` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.ex` | Unix command (use PowerShell equivalent) |
| `L995` | `| `L1102` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.ex` | Unix text processing utilities (use PowerShell or Python) |
| `L995` | `| `L1102` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.ex` | Unix command (use PowerShell equivalent) |
| `L996` | `| `L1103` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.ex` | Unix text processing utilities (use PowerShell or Python) |
| `L996` | `| `L1103` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.ex` | Unix command (use PowerShell equivalent) |
| `L997` | `| `L1103` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.ex` | Unix text processing utilities (use PowerShell or Python) |
| `L997` | `| `L1103` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.ex` | Unix command (use PowerShell equivalent) |
| `L998` | `| `L1104` | `| `L801` | `grep -q "^\.env$\|^\.env\.\*" .gitignore | Out-Null ; e` | Unix text processing utilities (use PowerShell or Python) |
| `L999` | `| `L1105` | `| `L807` | `[ -f "$f" ] ; grep -n "password:\|token:\|secret:\|api_` | Unix text processing utilities (use PowerShell or Python) |
| `L1000` | `| `L1106` | `| `L896` | `**Key checks (beyond grep):**` | Unix text processing u` | Unix text processing utilities (use PowerShell or Python) |
| `L1001` | `| `L1107` | `| `L914` | `ls -la .agents/skills/ | Out-Null` | Unix command (use ` | Unix command (use PowerShell equivalent) |
| `L1002` | `| `L1108` | `| `L918` | `- `curl`, `wget`, `fetch`, `http`, `exfiltrat` (network` | Unix network tools (use PowerShell or Python) |
| `L1003` | `| `L1118` | `| `L288` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1004` | `| `L1119` | `| `L291` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1005` | `| `L1121` | `| `L679` | `ls DESIGN.md design-system.md | Out-Null ; echo "NO_DES` | Unix command (use PowerShell equivalent) |
| `L1006` | `| `L1122` | `| `L688` | `cat README.md | Out-Null | head -50` | Unix command (us` | Unix command (use PowerShell equivalent) |
| `L1007` | `| `L1123` | `| `L689` | `cat package.json | Out-Null | head -20` | Unix command ` | Unix command (use PowerShell equivalent) |
| `L1008` | `| `L1124` | `| `L690` | `ls src/ app/ pages/ components/ | Out-Null | head -30` ` | Unix command (use PowerShell equivalent) |
| `L1009` | `| `L1125` | `| `L698` | `ls ~/.gstack/projects/$SLUG/*office-hours* | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L1010` | `| `L1126` | `| `L699` | `ls .context/*office-hours* .context/attachments/*office` | Unix command (use PowerShell equivalent) |
| `L1011` | `| `L1127` | `| `L731` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Un` | Unix network tools (use PowerShell or Python) |
| `L1012` | `| `L1128` | `| `L732` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}` | Unix text processing utilities (use PowerShell or Python) |
| `L1013` | `| `L1129` | `| `L1045` | `cat "$_DESIGN_DIR/feedback.json"` | Unix command (use ` | Unix command (use PowerShell equivalent) |
| `L1014` | `| `L1130` | `| `L1048` | `cat "$_DESIGN_DIR/feedback-pending.json"` | Unix comma` | Unix command (use PowerShell equivalent) |
| `L1015` | `| `L1131` | `| `L1077` | ``curl -s -X POST http://127.0.0.1:PORT/api/reload -H '` | Unix network tools (use PowerShell or Python) |
| `L1016` | `| `L1145` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1017` | `| `L1146` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1018` | `| `L1148` | `| `L811` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Un` | Unix network tools (use PowerShell or Python) |
| `L1019` | `| `L1149` | `| `L812` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}` | Unix text processing utilities (use PowerShell or Python) |
| `L1020` | `| `L1150` | `| `L836` | `_CEO=$(ls -t ~/.gstack/projects/$SLUG/ceo-plans/*.md | ` | Unix command (use PowerShell equivalent) |
| `L1021` | `| `L1151` | `| `L842` | `_APPROVED=$(ls -t ~/.gstack/projects/$SLUG/designs/*/ap` | Unix command (use PowerShell equivalent) |
| `L1022` | `| `L1152` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/va` | Unix command (use PowerShell equivalent) |
| `L1023` | `| `L1153` | `| `L854` | `_FINALIZED=$(ls -t ~/.gstack/projects/$SLUG/designs/*/f` | Unix command (use PowerShell equivalent) |
| `L1024` | `| `L1154` | `| `L979` | `[ -f package.json ] ; cat package.json | grep -o '"reac` | Unix text processing utilities (use PowerShell or Python) |
| `L1024` | `| `L1154` | `| `L979` | `[ -f package.json ] ; cat package.json | grep -o '"reac` | Unix command (use PowerShell equivalent) |
| `L1025` | `| `L1154` | `| `L979` | `[ -f package.json ] ; cat package.json | grep -o '"reac` | Unix text processing utilities (use PowerShell or Python) |
| `L1025` | `| `L1154` | `| `L979` | `[ -f package.json ] ; cat package.json | grep -o '"reac` | Unix command (use PowerShell equivalent) |
| `L1026` | `| `L1155` | `| `L979` | `[ -f package.json ] ; cat package.json | grep -o '"reac` | Unix text processing utilities (use PowerShell or Python) |
| `L1026` | `| `L1155` | `| `L979` | `[ -f package.json ] ; cat package.json | grep -o '"reac` | Unix command (use PowerShell equivalent) |
| `L1027` | `| `L1155` | `| `L979` | `[ -f package.json ] ; cat package.json | grep -o '"reac` | Unix text processing utilities (use PowerShell or Python) |
| `L1027` | `| `L1155` | `| `L979` | `[ -f package.json ] ; cat package.json | grep -o '"reac` | Unix command (use PowerShell equivalent) |
| `L1028` | `| `L1156` | `| `L1226` | `_PORT=$(lsof -i -P -n | grep "$_SERVER_PID" | grep LIS` | Unix text processing utilities (use PowerShell or Python) |
| `L1029` | `| `L1162` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/va` | Unix command (use PowerShell equivalent) |
| `L1030` | `| `L1171` | `| `L288` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1031` | `| `L1172` | `| `L291` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1032` | `| `L1174` | `| `L689` | `$B status | Out-Null | grep -q "Mode: cdp" ; echo "CDP_` | Unix text processing utilities (use PowerShell or Python) |
| `L1033` | `| `L1175` | `| `L740` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Un` | Unix network tools (use PowerShell or Python) |
| `L1034` | `| `L1176` | `| `L741` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}` | Unix text processing utilities (use PowerShell or Python) |
| `L1035` | `| `L1177` | `| `L770` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | Out-Null ; e` | Unix text processing utilities (use PowerShell or Python) |
| `L1036` | `| `L1178` | `| `L771` | `[ -f package.json ] ; grep -q '"next"' package.json | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1037` | `| `L1179` | `| `L773` | `ls jest.config.* vitest.config.* playwright.config.* .r` | Unix command (use PowerShell equivalent) |
| `L1038` | `| `L1180` | `| `L774` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out` | Unix command (use PowerShell equivalent) |
| `L1039` | `| `L1181` | `| `L859` | `ls -d .github/ | Out-Null ; echo "CI:github"` | Unix co` | Unix command (use PowerShell equivalent) |
| `L1040` | `| `L1182` | `| `L860` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | Out-Null` | ` | Unix command (use PowerShell equivalent) |
| `L1041` | `| `L1196` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1042` | `| `L1197` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1043` | `| `L1199` | `| `L829` | `cat DESIGN.md | Out-Null | head -80 ; echo "NO_DESIGN_M` | Unix command (use PowerShell equivalent) |
| `L1044` | `| `L1200` | `| `L833` | `ls src/ app/ pages/ components/ | Out-Null | head -30` ` | Unix command (use PowerShell equivalent) |
| `L1045` | `| `L1201` | `| `L838` | `ls ~/.gstack/projects/$SLUG/*office-hours* | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L1046` | `| `L1202` | `| `L848` | `curl -s -o $null -w "%{http_code}" http://localhost:300` | Unix network tools (use PowerShell or Python) |
| `L1047` | `| `L1203` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` |` | Unix command (use PowerShell equivalent) |
| `L1048` | `| `L1204` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L1049` | `| `L1204` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L1050` | `| `L1205` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L1051` | `| `L1205` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L1052` | `| `L1206` | `| `L1043` | `cat "$_DESIGN_DIR/feedback.json"` | Unix command (use ` | Unix command (use PowerShell equivalent) |
| `L1053` | `| `L1207` | `| `L1046` | `cat "$_DESIGN_DIR/feedback-pending.json"` | Unix comma` | Unix command (use PowerShell equivalent) |
| `L1054` | `| `L1208` | `| `L1075` | ``curl -s -X POST http://127.0.0.1:PORT/api/reload -H '` | Unix network tools (use PowerShell or Python) |
| `L1055` | `| `L1217` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` |` | Unix command (use PowerShell equivalent) |
| `L1056` | `| `L1221` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L1057` | `| `L1221` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L1058` | `| `L1231` | `| `L292` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1059` | `| `L1232` | `| `L295` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1060` | `| `L1234` | `| `L697` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/nu` | Unix text processing utilities (use PowerShell or Python) |
| `L1061` | `| `L1235` | `| `L732` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Un` | Unix network tools (use PowerShell or Python) |
| `L1062` | `| `L1236` | `| `L733` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}` | Unix text processing utilities (use PowerShell or Python) |
| `L1063` | `| `L1238` | `| `L849` | `$GSTACK_ROOT/bin/gstack-review-read | Out-Null | grep p` | Unix text processing utilities (use PowerShell or Python) |
| `L1064` | `| `L1239` | `| `L903` | `- Deprecation warnings in code (grep for deprecated/obs` | Unix text processing utilities (use PowerShell or Python) |
| `L1065` | `| `L1247` | `| `L345` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L1066` | `| `L1249` | `| `L465` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, ` | Unix text processing utilities (use PowerShell or Python) |
| `L1067` | `| `L1251` | `| `L496` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1068` | `| `L1252` | `| `L498` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1069` | `| `L1254` | `| `L668` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/nu` | Unix text processing utilities (use PowerShell or Python) |
| `L1070` | `| `L1255` | `| `L871` | `- Use ASCII diagrams for architecture. They're grep-abl` | Unix text processing utilities (use PowerShell or Python) |
| `L1071` | `| `L1256` | `| `L1036` | `git diff --cached --no-color | grep '^+' | sed 's/^+//` | Unix text processing utilities (use PowerShell or Python) |
| `L1072` | `| `L1265` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1073` | `| `L1266` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1074` | `| `L1268` | `| `L672` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/nu` | Unix text processing utilities (use PowerShell or Python) |
| `L1075` | `| `L1269` | `| `L939` | `git commit -m "$(cat <<'EOF'` | Unix command (use Power` | Unix command (use PowerShell equivalent) |
| `L1076` | `| `L1270` | `| `L984` | `glab mr update -d "$(cat <<'MRBODY'` | Unix command (us` | Unix command (use PowerShell equivalent) |
| `L1077` | `| `L1291` | `| `L6` | `Combines /gs:careful (warns before rm -rf, DROP TABLE, fo` | Unix force-remove command (use PowerShell equivalent) |
| `L1078` | `| `L1293` | `| `L89` | `- "1. **Destructive command warnings** — rm -rf, DROP TA` | Unix force-remove command (use PowerShell equivalent) |
| `L1079` | `| `L1302` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1080` | `| `L1303` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1081` | `| `L1305` | `| `L675` | `ls eslint.config.* .eslintrc.* .eslintrc | Out-Null | h` | Unix command (use PowerShell equivalent) |
| `L1082` | `| `L1306` | `| `L676` | `[ -f .pylintrc ] ; [ -f pyproject.toml ] ; grep -q "pyl` | Unix text processing utilities (use PowerShell or Python) |
| `L1083` | `| `L1307` | `| `L679` | `[ -f package.json ] ; grep -q '"test"' package.json | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1084` | `| `L1308` | `| `L680` | `[ -f pyproject.toml ] ; grep -q "pytest" pyproject.toml` | Unix text processing utilities (use PowerShell or Python) |
| `L1085` | `| `L1309` | `| `L686` | `[ -f package.json ] ; grep -q '"knip"' package.json | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1086` | `| `L1310` | `| `L689` | `command -v shellcheck | Out-Null 2>&1 ; ls *.sh scripts` | Unix command (use PowerShell equivalent) |
| `L1087` | `| `L1319` | `| `L304` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1088` | `| `L1320` | `| `L307` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1089` | `| `L1330` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1090` | `| `L1331` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1091` | `| `L1333` | `| `L684` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Un` | Unix network tools (use PowerShell or Python) |
| `L1092` | `| `L1334` | `| `L685` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}` | Unix text processing utilities (use PowerShell or Python) |
| `L1093` | `| `L1335` | `| `L724` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/nu` | Unix text processing utilities (use PowerShell or Python) |
| `L1094` | `| `L1336` | `| `L825` | `SAVED_HASH=$(cat ~/.gstack/projects/$SLUG/land-deploy-c` | Unix command (use PowerShell equivalent) |
| `L1095` | `| `L1337` | `| `L826` | `CURRENT_HASH=$(sed -n '/## Deploy Configuration/,/^## /` | Unix text processing utilities (use PowerShell or Python) |
| `L1096` | `| `L1339` | `| `L865` | `DEPLOY_CONFIG=$(grep -A 20 "## Deploy Configuration" CL` | Unix text processing utilities (use PowerShell or Python) |
| `L1097` | `| `L1340` | `| `L870` | `PROD_URL=$(echo "$DEPLOY_CONFIG" | grep -i "production.` | Unix text processing utilities (use PowerShell or Python) |
| `L1098` | `| `L1341` | `| `L871` | `PLATFORM=$(echo "$DEPLOY_CONFIG" | grep -i "platform" |` | Unix text processing utilities (use PowerShell or Python) |
| `L1099` | `| `L1342` | `| `L886` | `[ -f "$f" ] ; grep -qiE "deploy|release|production|cd" ` | Unix text processing utilities (use PowerShell or Python) |
| `L1100` | `| `L1343` | `| `L887` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Out-Null ; ech` | Unix text processing utilities (use PowerShell or Python) |
| `L1101` | `| `L1344` | `| `L932` | `║  ├─ curl prod URL:      ✓ PASS (200 OK) / ⚠ UNREACHAB` | Unix network tools (use PowerShell or Python) |
| `L1102` | `| `L1345` | `| `L953` | `failed at Step 1). If `curl` fails, note "I couldn't re` | Unix network tools (use PowerShell or Python) |
| `L1103` | `| `L1346` | `| `L966` | `grep -i "staging" CLAUDE.md | Out-Null | head -3` | Uni` | Unix text processing utilities (use PowerShell or Python) |
| `L1104` | `| `L1347` | `| `L972` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Out-Null ; ech` | Unix text processing utilities (use PowerShell or Python) |
| `L1105` | `| `L1348` | `| `L1020` | `CURRENT_HASH=$(sed -n '/## Deploy Configuration/,/^## ` | Unix text processing utilities (use PowerShell or Python) |
| `L1106` | `| `L1350` | `| `L1130` | `cat $GSTACK_ROOT/review/checklist.md | Out-Null ; echo` | Unix command (use PowerShell equivalent) |
| `L1107` | `| `L1351` | `| `L1164` | `ls -t ~/.gstack-dev/evals/*-e2e-*-$(date +%Y-%m-%d)*.j` | Unix command (use PowerShell equivalent) |
| `L1108` | `| `L1352` | `| `L1180` | `ls -t ~/.gstack-dev/evals/*-llm-judge-*-$(date +%Y-%m-` | Unix command (use PowerShell equivalent) |
| `L1109` | `| `L1353` | `| `L1210` | `git log --oneline --all-match --grep="docs:" $(gh pr v` | Unix text processing utilities (use PowerShell or Python) |
| `L1110` | `| `L1354` | `| `L1365` | `DEPLOY_CONFIG=$(grep -A 20 "## Deploy Configuration" C` | Unix text processing utilities (use PowerShell or Python) |
| `L1111` | `| `L1355` | `| `L1370` | `PROD_URL=$(echo "$DEPLOY_CONFIG" | grep -i "production` | Unix text processing utilities (use PowerShell or Python) |
| `L1112` | `| `L1356` | `| `L1371` | `PLATFORM=$(echo "$DEPLOY_CONFIG" | grep -i "platform" ` | Unix text processing utilities (use PowerShell or Python) |
| `L1113` | `| `L1357` | `| `L1386` | `[ -f "$f" ] ; grep -qiE "deploy|release|production|cd"` | Unix text processing utilities (use PowerShell or Python) |
| `L1114` | `| `L1358` | `| `L1387` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Out-Null ; ec` | Unix text processing utilities (use PowerShell or Python) |
| `L1115` | `| `L1359` | `| `L1486` | `curl -sf {production-url} -o $null -w "%{http_code}" |` | Unix network tools (use PowerShell or Python) |
| `L1116` | `| `L1368` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1117` | `| `L1369` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1118` | `| `L1371` | `| `L768` | `cat "$LEARN_FILE" | bun -e "` | Unix command (use Power` | Unix command (use PowerShell equivalent) |
| `L1119` | `| `L1388` | `| `L264` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L1120` | `| `L1390` | `| `L384` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, ` | Unix text processing utilities (use PowerShell or Python) |
| `L1121` | `| `L1406` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1122` | `| `L1407` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1123` | `| `L1409` | `| `L694` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Un` | Unix network tools (use PowerShell or Python) |
| `L1124` | `| `L1410` | `| `L695` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}` | Unix text processing utilities (use PowerShell or Python) |
| `L1125` | `| `L1411` | `| `L731` | `ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-Null` | Unix command (use PowerShell equivalent) |
| `L1127` | `| `L1413` | `| `L989` | `grep -li "<keyword1>\|<keyword2>\|<keyword3>" ~/.gstack` | Unix text processing utilities (use PowerShell or Python) |
| `L1128` | `| `L1414` | `| `L1159` | `4. POST the new HTML to the running server via `curl -` | Unix network tools (use PowerShell or Python) |
| `L1129` | `| `L1415` | `| `L1253` | `Use a 5-minute timeout (`timeout: 300000`). After comp` | Unix command (use PowerShell equivalent) |
| `L1130` | `| `L1416` | `| `L1253` | `Use a 5-minute timeout (`timeout: 300000`). After comp` | Unix command (use PowerShell equivalent) |
| `L1131` | `| `L1417` | `| `L1321` | `PRIOR=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-desig` | Unix command (use PowerShell equivalent) |
| `L1132` | `| `L1418` | `| `L1532` | `SESSION_TIER=$(echo "$PROFILE" | grep "^TIER:" | awk '` | Unix text processing utilities (use PowerShell or Python) |
| `L1133` | `| `L1419` | `| `L1533` | `SESSION_COUNT=$(echo "$PROFILE" | grep "^SESSION_COUNT` | Unix text processing utilities (use PowerShell or Python) |
| `L1134` | `| `L1433` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1135` | `| `L1434` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1136` | `| `L1436` | `| `L689` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Un` | Unix network tools (use PowerShell or Python) |
| `L1137` | `| `L1437` | `| `L690` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}` | Unix text processing utilities (use PowerShell or Python) |
| `L1138` | `| `L1438` | `| `L711` | `_OLD_PID=$(cat "$(git rev-parse --show-toplevel)/.gstac` | Unix command (use PowerShell equivalent) |
| `L1139` | `| `L1439` | `| `L711` | `_OLD_PID=$(cat "$(git rev-parse --show-toplevel)/.gstac` | Unix command (use PowerShell equivalent) |
| `L1140` | `| `L1440` | `| `L756` | `cat "$(git rev-parse --show-toplevel | Out-Null)/.gstac` | Unix command (use PowerShell equivalent) |
| `L1141` | `| `L1441` | `| `L756` | `cat "$(git rev-parse --show-toplevel | Out-Null)/.gstac` | Unix command (use PowerShell equivalent) |
| `L1142` | `| `L1450` | `| `L287` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1143` | `| `L1451` | `| `L290` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1144` | `| `L1453` | `| `L711` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Un` | Unix network tools (use PowerShell or Python) |
| `L1145` | `| `L1454` | `| `L712` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}` | Unix text processing utilities (use PowerShell or Python) |
| `L1146` | `| `L1455` | `| `L908` | ``exec curl` syntax which OpenClaw understands natively.` | Unix network tools (use PowerShell or Python) |
| `L1147` | `| `L1456` | `| `L915` | `curl commands work directly. When using `--local codex`` | Unix network tools (use PowerShell or Python) |
| `L1148` | `| `L1465` | `| `L289` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1149` | `| `L1466` | `| `L292` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1150` | `| `L1468` | `| `L694` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/nu` | Unix text processing utilities (use PowerShell or Python) |
| `L1151` | `| `L1469` | `| `L779` | `grep -r "TODO\|FIXME\|HACK\|XXX" -l --exclude-dir=node_` | Unix text processing utilities (use PowerShell or Python) |
| `L1152` | `| `L1470` | `| `L789` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-desig` | Unix command (use PowerShell equivalent) |
| `L1153` | `| `L1471` | `| `L790` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$S` | Unix command (use PowerShell equivalent) |
| `L1154` | `| `L1472` | `| `L798` | `HANDOFF=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-ceo-` | Unix command (use PowerShell equivalent) |
| `L1155` | `| `L1473` | `| `L860` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-desig` | Unix command (use PowerShell equivalent) |
| `L1156` | `| `L1474` | `| `L861` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$S` | Unix command (use PowerShell equivalent) |
| `L1157` | `| `L1483` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1158` | `| `L1484` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1159` | `| `L1486` | `| `L691` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/nu` | Unix text processing utilities (use PowerShell or Python) |
| `L1160` | `| `L1487` | `| `L980` | `- `mkdir -p ~/.gstack/projects/$SLUG/designs/...`` | Un` | Unix nested directory creation (use PowerShell equivalent) |
| `L1161` | `| `L1488` | `| `L1057` | `cat "$_DESIGN_DIR/feedback.json"` | Unix command (use ` | Unix command (use PowerShell equivalent) |
| `L1162` | `| `L1489` | `| `L1060` | `cat "$_DESIGN_DIR/feedback-pending.json"` | Unix comma` | Unix command (use PowerShell equivalent) |
| `L1163` | `| `L1490` | `| `L1089` | ``curl -s -X POST http://127.0.0.1:PORT/api/reload -H '` | Unix network tools (use PowerShell or Python) |
| `L1164` | `| `L1504` | `| `L296` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1165` | `| `L1505` | `| `L299` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1166` | `| `L1507` | `| `L701` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/nu` | Unix text processing utilities (use PowerShell or Python) |
| `L1167` | `| `L1509` | `| `L832` | `- Getting started guides (grep README for "Getting Star` | Unix text processing utilities (use PowerShell or Python) |
| `L1168` | `| `L1510` | `| `L833` | `- CLI help text (grep for `--help`, `usage:`, `commands` | Unix text processing utilities (use PowerShell or Python) |
| `L1169` | `| `L1511` | `| `L834` | `- Error message patterns (grep for `throw new Error`, `` | Unix text processing utilities (use PowerShell or Python) |
| `L1170` | `| `L1512` | `| `L842` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-desig` | Unix command (use PowerShell equivalent) |
| `L1171` | `| `L1513` | `| `L843` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$S` | Unix command (use PowerShell equivalent) |
| `L1172` | `| `L1514` | `| `L902` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-desig` | Unix command (use PowerShell equivalent) |
| `L1173` | `| `L1515` | `| `L903` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$S` | Unix command (use PowerShell equivalent) |
| `L1174` | `| `L1516` | `| `L1264` | `$GSTACK_ROOT/bin/gstack-review-read | Out-Null | grep ` | Unix text processing utilities (use PowerShell or Python) |
| `L1175` | `| `L1525` | `| `L291` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1176` | `| `L1526` | `| `L294` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1177` | `| `L1528` | `| `L720` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-desig` | Unix command (use PowerShell equivalent) |
| `L1178` | `| `L1529` | `| `L721` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$S` | Unix command (use PowerShell equivalent) |
| `L1179` | `| `L1530` | `| `L775` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-desig` | Unix command (use PowerShell equivalent) |
| `L1180` | `| `L1531` | `| `L776` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$S` | Unix command (use PowerShell equivalent) |
| `L1181` | `| `L1532` | `| `L896` | `ls jest.config.* vitest.config.* playwright.config.* cy` | Unix command (use PowerShell equivalent) |
| `L1182` | `| `L1533` | `| `L897` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out` | Unix command (use PowerShell equivalent) |
| `L1183` | `| `L1542` | `| `L296` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1184` | `| `L1543` | `| `L299` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1185` | `| `L1553` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1186` | `| `L1554` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1187` | `| `L1556` | `| `L707` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Un` | Unix network tools (use PowerShell or Python) |
| `L1188` | `| `L1557` | `| `L708` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}` | Unix text processing utilities (use PowerShell or Python) |
| `L1189` | `| `L1558` | `| `L748` | `ls -t ~/.gstack/projects/$SLUG/*-test-plan-*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L1190` | `| `L1572` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1191` | `| `L1573` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1192` | `| `L1575` | `| `L698` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/nu` | Unix text processing utilities (use PowerShell or Python) |
| `L1193` | `| `L1576` | `| `L738` | `$B status | Out-Null | grep -q "Mode: cdp" ; echo "CDP_` | Unix text processing utilities (use PowerShell or Python) |
| `L1194` | `| `L1577` | `| `L785` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Un` | Unix network tools (use PowerShell or Python) |
| `L1195` | `| `L1578` | `| `L786` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}` | Unix text processing utilities (use PowerShell or Python) |
| `L1196` | `| `L1579` | `| `L815` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | Out-Null ; e` | Unix text processing utilities (use PowerShell or Python) |
| `L1197` | `| `L1580` | `| `L816` | `[ -f package.json ] ; grep -q '"next"' package.json | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1198` | `| `L1581` | `| `L818` | `ls jest.config.* vitest.config.* playwright.config.* .r` | Unix command (use PowerShell equivalent) |
| `L1199` | `| `L1582` | `| `L819` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out` | Unix command (use PowerShell equivalent) |
| `L1200` | `| `L1583` | `| `L904` | `ls -d .github/ | Out-Null ; echo "CI:github"` | Unix co` | Unix command (use PowerShell equivalent) |
| `L1201` | `| `L1584` | `| `L905` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | Out-Null` | ` | Unix command (use PowerShell equivalent) |
| `L1202` | `| `L1585` | `| `L981` | `ls -t ~/.gstack/projects/$SLUG/*-test-plan-*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L1203` | `| `L1599` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1204` | `| `L1600` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1205` | `| `L1602` | `| `L670` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/nu` | Unix text processing utilities (use PowerShell or Python) |
| `L1207` | `| `L1604` | `| `L773` | `git log origin/<default> --since="<window>" --format="%` | Unix text processing utilities (use PowerShell or Python) |
| `L1208` | `| `L1605` | `| `L782` | `cat ~/.gstack/greptile-history.md | Out-Null ; true` | ` | Unix command (use PowerShell equivalent) |
| `L1209` | `| `L1606` | `| `L785` | `cat TODOS.md | Out-Null ; true` | Unix command (use Pow` | Unix command (use PowerShell equivalent) |
| `L1210` | `| `L1608` | `| `L791` | `git log origin/<default> --since="<window>" --oneline -` | Unix text processing utilities (use PowerShell or Python) |
| `L1211` | `| `L1609` | `| `L794` | `cat ~/.gstack/analytics/skill-usage.jsonl | Out-Null ; ` | Unix command (use PowerShell equivalent) |
| `L1213` | `| `L1611` | `| `L1029` | `ls -t .context/retros/*.json | Out-Null` | Unix comman` | Unix command (use PowerShell equivalent) |
| `L1214` | `| `L1612` | `| `L1058` | `existing=$(ls .context/retros/${today}-*.json | Out-Nu` | Unix command (use PowerShell equivalent) |
| `L1215` | `| `L1613` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Nul` | Unix text processing utilities (use PowerShell or Python) |
| `L1215` | `| `L1613` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Nul` | Unix command (use PowerShell equivalent) |
| `L1216` | `| `L1613` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Nul` | Unix text processing utilities (use PowerShell or Python) |
| `L1216` | `| `L1613` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Nul` | Unix command (use PowerShell equivalent) |
| `L1217` | `| `L1614` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Nul` | Unix text processing utilities (use PowerShell or Python) |
| `L1217` | `| `L1614` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Nul` | Unix command (use PowerShell equivalent) |
| `L1218` | `| `L1614` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Nul` | Unix text processing utilities (use PowerShell or Python) |
| `L1218` | `| `L1614` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Nul` | Unix command (use PowerShell equivalent) |
| `L1219` | `| `L1616` | `| `L1482` | `ls -t ~/.gstack/retros/global-*.json | Out-Null | head` | Unix command (use PowerShell equivalent) |
| `L1220` | `| `L1617` | `| `L1501` | `existing=$(ls ~/.gstack/retros/global-${today}-*.json ` | Unix command (use PowerShell equivalent) |
| `L1221` | `| `L1631` | `| `L287` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1222` | `| `L1632` | `| `L290` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1223` | `| `L1634` | `| `L692` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/nu` | Unix text processing utilities (use PowerShell or Python) |
| `L1224` | `| `L1635` | `| `L764` | `_PLAN_SLUG=$(git remote get-url origin | Out-Null | sed` | Unix text processing utilities (use PowerShell or Python) |
| `L1225` | `| `L1636` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -` | Unix text processing utilities (use PowerShell or Python) |
| `L1225` | `| `L1636` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -` | Unix command (use PowerShell equivalent) |
| `L1226` | `| `L1636` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -` | Unix text processing utilities (use PowerShell or Python) |
| `L1226` | `| `L1636` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -` | Unix command (use PowerShell equivalent) |
| `L1227` | `| `L1637` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -` | Unix text processing utilities (use PowerShell or Python) |
| `L1227` | `| `L1637` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -` | Unix command (use PowerShell equivalent) |
| `L1228` | `| `L1637` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -` | Unix text processing utilities (use PowerShell or Python) |
| `L1228` | `| `L1637` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -` | Unix command (use PowerShell equivalent) |
| `L1229` | `| `L1638` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Nu` | Unix command (use PowerShell equivalent) |
| `L1230` | `| `L1638` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Nu` | Unix command (use PowerShell equivalent) |
| `L1231` | `| `L1639` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Nu` | Unix command (use PowerShell equivalent) |
| `L1232` | `| `L1639` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Nu` | Unix command (use PowerShell equivalent) |
| `L1233` | `| `L1648` | `| `L334` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix text processing utilities (use PowerShell or Python) |
| `L1233` | `| `L1648` | `| `L334` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix command (use PowerShell equivalent) |
| `L1234` | `| `L1648` | `| `L334` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix text processing utilities (use PowerShell or Python) |
| `L1234` | `| `L1648` | `| `L334` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix command (use PowerShell equivalent) |
| `L1235` | `| `L1649` | `| `L334` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix text processing utilities (use PowerShell or Python) |
| `L1235` | `| `L1649` | `| `L334` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix command (use PowerShell equivalent) |
| `L1236` | `| `L1649` | `| `L334` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix text processing utilities (use PowerShell or Python) |
| `L1236` | `| `L1649` | `| `L334` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix command (use PowerShell equivalent) |
| `L1237` | `| `L1651` | `| `L370` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1238` | `| `L1652` | `| `L373` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1239` | `| `L1661` | `| `L389` | `$B status | Out-Null | grep -q "Mode: cdp" ; echo "CDP_` | Unix text processing utilities (use PowerShell or Python) |
| `L1240` | `| `L1662` | `| `L427` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Un` | Unix network tools (use PowerShell or Python) |
| `L1241` | `| `L1663` | `| `L428` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}` | Unix text processing utilities (use PowerShell or Python) |
| `L1242` | `| `L1672` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1243` | `| `L1673` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1244` | `| `L1675` | `| `L662` | `grep -A 20 "## Deploy Configuration" CLAUDE.md | Out-Nu` | Unix text processing utilities (use PowerShell or Python) |
| `L1245` | `| `L1676` | `| `L681` | `[ -f fly.toml ] ; echo "PLATFORM:fly" ; cat fly.toml` |` | Unix command (use PowerShell equivalent) |
| `L1246` | `| `L1677` | `| `L682` | `[ -f render.yaml ] ; echo "PLATFORM:render" ; cat rende` | Unix command (use PowerShell equivalent) |
| `L1247` | `| `L1678` | `| `L684` | `[ -f netlify.toml ] ; echo "PLATFORM:netlify" ; cat net` | Unix command (use PowerShell equivalent) |
| `L1248` | `| `L1679` | `| `L690` | `[ -f "$f" ] ; grep -qiE "deploy|release|production|stag` | Unix text processing utilities (use PowerShell or Python) |
| `L1249` | `| `L1680` | `| `L694` | `[ -f package.json ] ; grep -q '"bin"' package.json | Ou` | Unix text processing utilities (use PowerShell or Python) |
| `L1250` | `| `L1681` | `| `L695` | `find . -maxdepth 1 -name '*.gemspec' | Out-Null | grep ` | Unix text processing utilities (use PowerShell or Python) |
| `L1251` | `| `L1682` | `| `L706` | `1. Extract app name: `grep -m1 "^app" fly.toml | sed 's` | Unix text processing utilities (use PowerShell or Python) |
| `L1252` | `| `L1683` | `| `L734` | `2. If installed: `vercel ls --prod 2>/dev/null | head -` | Unix command (use PowerShell equivalent) |
| `L1253` | `| `L1684` | `| `L807` | `curl -sf "{health-check-url}" -o $null -w "%{http_code}` | Unix network tools (use PowerShell or Python) |
| `L1254` | `| `L1693` | `| `L289` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1255` | `| `L1694` | `| `L292` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1256` | `| `L1696` | `| `L694` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/nu` | Unix text processing utilities (use PowerShell or Python) |
| `L1257` | `| `L1697` | `| `L829` | `git diff origin/<base> --name-only | grep -E '(cmd/.*/m` | Unix text processing utilities (use PowerShell or Python) |
| `L1258` | `| `L1698` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE 'release|pu` | Unix text processing utilities (use PowerShell or Python) |
| `L1258` | `| `L1698` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE 'release|pu` | Unix command (use PowerShell equivalent) |
| `L1259` | `| `L1698` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE 'release|pu` | Unix text processing utilities (use PowerShell or Python) |
| `L1259` | `| `L1698` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE 'release|pu` | Unix command (use PowerShell equivalent) |
| `L1260` | `| `L1699` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE 'release|pu` | Unix text processing utilities (use PowerShell or Python) |
| `L1260` | `| `L1699` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE 'release|pu` | Unix command (use PowerShell equivalent) |
| `L1261` | `| `L1699` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE 'release|pu` | Unix text processing utilities (use PowerShell or Python) |
| `L1261` | `| `L1699` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE 'release|pu` | Unix command (use PowerShell equivalent) |
| `L1262` | `| `L1700` | `| `L835` | `grep -qE 'release|publish|deploy' .gitlab-ci.yml | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L1263` | `| `L1701` | `| `L881` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | Out-Null ; e` | Unix text processing utilities (use PowerShell or Python) |
| `L1264` | `| `L1702` | `| `L882` | `[ -f package.json ] ; grep -q '"next"' package.json | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1265` | `| `L1703` | `| `L884` | `ls jest.config.* vitest.config.* playwright.config.* .r` | Unix command (use PowerShell equivalent) |
| `L1266` | `| `L1704` | `| `L885` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out` | Unix command (use PowerShell equivalent) |
| `L1267` | `| `L1705` | `| `L970` | `ls -d .github/ | Out-Null ; echo "CI:github"` | Unix co` | Unix command (use PowerShell equivalent) |
| `L1268` | `| `L1706` | `| `L971` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | Out-Null` | ` | Unix command (use PowerShell equivalent) |
| `L1269` | `| `L1707` | `| `L1176` | `grep -l "changed_file_basename" test/evals/*_eval_runn` | Unix text processing utilities (use PowerShell or Python) |
| `L1270` | `| `L1708` | `| `L1183` | `- Changes to `config/system_prompts/*.txt` — grep eval` | Unix text processing utilities (use PowerShell or Python) |
| `L1271` | `| `L1709` | `| `L1238` | `ls jest.config.* vitest.config.* playwright.config.* c` | Unix command (use PowerShell equivalent) |
| `L1272` | `| `L1710` | `| `L1239` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Ou` | Unix command (use PowerShell equivalent) |
| `L1273` | `| `L1713` | `| `L1511` | `_PLAN_SLUG=$(git remote get-url origin | Out-Null | se` | Unix text processing utilities (use PowerShell or Python) |
| `L1274` | `| `L1714` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep ` | Unix text processing utilities (use PowerShell or Python) |
| `L1274` | `| `L1714` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep ` | Unix command (use PowerShell equivalent) |
| `L1275` | `| `L1714` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep ` | Unix text processing utilities (use PowerShell or Python) |
| `L1275` | `| `L1714` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep ` | Unix command (use PowerShell equivalent) |
| `L1276` | `| `L1715` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep ` | Unix text processing utilities (use PowerShell or Python) |
| `L1276` | `| `L1715` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep ` | Unix command (use PowerShell equivalent) |
| `L1277` | `| `L1715` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep ` | Unix text processing utilities (use PowerShell or Python) |
| `L1277` | `| `L1715` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep ` | Unix command (use PowerShell equivalent) |
| `L1278` | `| `L1716` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L1279` | `| `L1716` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L1280` | `| `L1717` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L1281` | `| `L1717` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L1282` | `| `L1719` | `| `L1647` | `curl -s -o $null -w '%{http_code}' http://localhost:30` | Unix network tools (use PowerShell or Python) |
| `L1283` | `| `L1720` | `| `L1648` | `curl -s -o $null -w '%{http_code}' http://localhost:80` | Unix network tools (use PowerShell or Python) |
| `L1284` | `| `L1721` | `| `L1649` | `curl -s -o $null -w '%{http_code}' http://localhost:51` | Unix network tools (use PowerShell or Python) |
| `L1285` | `| `L1722` | `| `L1650` | `curl -s -o $null -w '%{http_code}' http://localhost:40` | Unix network tools (use PowerShell or Python) |
| `L1286` | `| `L1723` | `| `L1660` | `cat ${CLAUDE_SKILL_DIR}/../qa-only/SKILL.md` | Unix co` | Unix command (use PowerShell equivalent) |
| `L1287` | `| `L1724` | `| `L1964` | `CURRENT_VERSION=$(cat VERSION | Out-Null | tr -d '\r\n` | Unix command (use PowerShell equivalent) |
| `L1288` | `| `L1725` | `| `L2029` | `if ! printf '%s' "$NEW_VERSION" | grep -qE '^[0-9]+\.[` | Unix text processing utilities (use PowerShell or Python) |
| `L1289` | `| `L1726` | `| `L2055` | `REPAIR_VERSION=$(cat VERSION | tr -d '\r\n[:space:]')`` | Unix command (use PowerShell equivalent) |
| `L1290` | `| `L1727` | `| `L2056` | `if ! printf '%s' "$REPAIR_VERSION" | grep -qE '^[0-9]+` | Unix text processing utilities (use PowerShell or Python) |
| `L1291` | `| `L1728` | `| `L2203` | `git commit -m "$(cat <<'EOF'` | Unix command (use Powe` | Unix command (use PowerShell equivalent) |
| `L1293` | `| `L1730` | `| `L2375` | `glab mr create -b <base> -t "<type>: <summary>" -d "$(` | Unix command (use PowerShell equivalent) |
| `L1294` | `| `L1738` | `| `L358` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix text processing utilities (use PowerShell or Python) |
| `L1294` | `| `L1738` | `| `L358` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix command (use PowerShell equivalent) |
| `L1295` | `| `L1738` | `| `L358` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix text processing utilities (use PowerShell or Python) |
| `L1295` | `| `L1738` | `| `L358` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix command (use PowerShell equivalent) |
| `L1296` | `| `L1739` | `| `L358` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix text processing utilities (use PowerShell or Python) |
| `L1296` | `| `L1739` | `| `L358` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix command (use PowerShell equivalent) |
| `L1297` | `| `L1739` | `| `L358` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix text processing utilities (use PowerShell or Python) |
| `L1297` | `| `L1739` | `| `L358` | `equivalents (cat, sed, find, grep). The dedicated tools` | Unix command (use PowerShell equivalent) |
| `L1298` | `| `L1747` | `| `L340` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L1299` | `| `L1749` | `| `L460` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, ` | Unix text processing utilities (use PowerShell or Python) |
| `L1300` | `| `L1751` | `| `L491` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeli` | Unix text processing utilities (use PowerShell or Python) |
| `L1301` | `| `L1752` | `| `L493` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PR` | Unix text processing utilities (use PowerShell or Python) |
| `L1303` | `| `L1755` | `| `L1264` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L1304` | `| `L1757` | `| `L1384` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse,` | Unix text processing utilities (use PowerShell or Python) |
| `L1305` | `| `L1759` | `| `L1415` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timel` | Unix text processing utilities (use PowerShell or Python) |
| `L1306` | `| `L1760` | `| `L1417` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_P` | Unix text processing utilities (use PowerShell or Python) |
| `L1307` | `| `L1762` | `| `L1611` | `ISSUE_NUMBER=$(echo "$ISSUE_URL" | sed -E 's|.*/issues` | Unix text processing utilities (use PowerShell or Python) |
| `L1308` | `| `L1778` | `| `L42` | `PREV=$(cat "$STATE_DIR/freeze-dir.txt")` | Unix command ` | Unix command (use PowerShell equivalent) |
| `L1309` | `| `L1786` | `| `L71` | `_SNOOZED_VER=$(awk '{print $1}' "$_SNOOZE_FILE")` | Unix` | Unix text processing utilities (use PowerShell or Python) |
| `L1310` | `| `L1787` | `| `L73` | `_CUR_LEVEL=$(awk '{print $2}' "$_SNOOZE_FILE")` | Unix t` | Unix text processing utilities (use PowerShell or Python) |
| `L1311` | `| `L1788` | `| `L127` | `OLD_VERSION=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; e` | Unix command (use PowerShell equivalent) |
| `L1312` | `| `L1789` | `| `L179` | `if ! grep -qF '.agents/skills/gstack/' .gitignore | Out` | Unix text processing utilities (use PowerShell or Python) |
| `L1313` | `| `L1790` | `| `L214` | `m_ver="$(basename "$migration" .sh | sed 's/^v//')"` | ` | Unix text processing utilities (use PowerShell or Python) |
| `L1314` | `| `L1791` | `| `L283` | `PRIMARY_VER=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; e` | Unix command (use PowerShell equivalent) |
| `L1315` | `| `L1792` | `| `L284` | `LOCAL_VER=$(cat "$LOCAL_GSTACK/VERSION" | Out-Null ; ec` | Unix command (use PowerShell equivalent) |
| `L1316` | `| `L1800` | `| `L446` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Un` | Unix network tools (use PowerShell or Python) |
| `L1317` | `| `L1801` | `| `L447` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}` | Unix text processing utilities (use PowerShell or Python) |
| `L1318` | `| `L1802` | `| `L470` | `> Set them before running: `export TEST_EMAIL="..." TES` | Unix environment variable export (use PowerShell equivalent) |
| `L1319` | `| `L1816` | `| `L64` | `_SNOOZED_VER=$(awk '{print $1}' "$_SNOOZE_FILE")` | Unix` | Unix text processing utilities (use PowerShell or Python) |
| `L1320` | `| `L1817` | `| `L66` | `_CUR_LEVEL=$(awk '{print $2}' "$_SNOOZE_FILE")` | Unix t` | Unix text processing utilities (use PowerShell or Python) |
| `L1321` | `| `L1818` | `| `L120` | `OLD_VERSION=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; e` | Unix command (use PowerShell equivalent) |
| `L1322` | `| `L1819` | `| `L172` | `if ! grep -qF '.agents/skills/gstack/' .gitignore | Out` | Unix text processing utilities (use PowerShell or Python) |
| `L1323` | `| `L1820` | `| `L207` | `m_ver="$(basename "$migration" .sh | sed 's/^v//')"` | ` | Unix text processing utilities (use PowerShell or Python) |
| `L1324` | `| `L1821` | `| `L276` | `PRIMARY_VER=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; e` | Unix command (use PowerShell equivalent) |
| `L1325` | `| `L1822` | `| `L277` | `LOCAL_VER=$(cat "$LOCAL_GSTACK/VERSION" | Out-Null ; ec` | Unix command (use PowerShell equivalent) |
| `L1326` | `| `L1830` | `| `L63` | `- **Trace it through every consumer.** Read (don't just ` | Unix text processing utilities (use PowerShell or Python) |
| `L1328` | `| `L1839` | `| `L25` | `- **[HIGH]** — Reliably detectable via grep/pattern matc` | Unix text processing utilities (use PowerShell or Python) |
| `L1329` | `| `L1848` | `| `L6` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdi` | Unix nested directory creation (use PowerShell equivalent) |
| `L1330` | `| `L1857` | `| `L9` | `if ($content -like $mkdir_pattern) { throw "FAIL: Unix mk` | Unix nested directory creation (use PowerShell equivalent) |
| `L1331` | `| `L1870` | `| `L5` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdi` | Unix nested directory creation (use PowerShell equivalent) |
| `L1337` | `| `L116` | `| `L101` | `| `L141` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L1338` | `| `L119` | `| `L104` | `| `L148` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L1339` | `| `L175` | `| `L159` | `| `L244` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L1340` | `| `L186` | `| `L166` | `| `L254` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L1341` | `| `L204` | `| `L184` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L1342` | `| `L205` | `| `L185` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1343` | `| `L206` | `| `L186` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1344` | `| `L207` | `| `L187` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1345` | `| `L208` | `| `L188` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1346` | `| `L212` | `| `L192` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L1347` | `| `L213` | `| `L193` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1348` | `| `L214` | `| `L194` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1349` | `| `L468` | `| `L442` | `| `L141` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L1350` | `| `L469` | `| `L443` | `| `L148` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L1351` | `| `L470` | `| `L445` | `| `L244` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L1352` | `| `L471` | `| `L447` | `| `L254` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L1353` | `| `L472` | `| `L449` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L1354` | `| `L473` | `| `L450` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1355` | `| `L474` | `| `L451` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1356` | `| `L475` | `| `L456` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L1357` | `| `L476` | `| `L460` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1358` | `| `L497` | `| `L555` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Unix force-remove command (use PowerShell equivalent) |
| `L1359` | `| `L500` | `| `L562` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Unix force-remove command (use PowerShell equivalent) |
| `L1360` | `| `L555` | `| `L658` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Unix command (use PowerShell equivalent) |
| `L1361` | `| `L562` | `| `L668` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Unix command (use PowerShell equivalent) |
| `L1362` | `| `L580` | `| `L709` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Unix command (use PowerShell equivalent) |
| `L1363` | `| `L581` | `| `L710` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L1364` | `| `L582` | `| `L710` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L1365` | `| `L583` | `| `L711` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L1366` | `| `L584` | `| `L711` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L1367` | `| `L588` | `| `L723` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Unix command (use PowerShell equivalent) |
| `L1368` | `| `L589` | `| `L727` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L1369` | `| `L590` | `| `L727` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L1370` | `| `L849` | `| `L101` | `| `L141` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L1371` | `| `L850` | `| `L104` | `| `L148` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L1372` | `| `L851` | `| `L159` | `| `L244` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L1373` | `| `L852` | `| `L166` | `| `L254` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L1374` | `| `L853` | `| `L184` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L1375` | `| `L854` | `| `L185` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1376` | `| `L855` | `| `L186` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1377` | `| `L856` | `| `L187` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1378` | `| `L857` | `| `L188` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1379` | `| `L858` | `| `L192` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L1380` | `| `L859` | `| `L193` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1381` | `| `L860` | `| `L194` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1383` | `| `L862` | `| `L442` | `| `L141` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L1384` | `| `L863` | `| `L443` | `| `L148` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recu` | Unix force-remove command (use PowerShell equivalent) |
| `L1386` | `| `L865` | `| `L445` | `| `L244` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L1388` | `| `L867` | `| `L447` | `| `L254` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/proj` | Unix command (use PowerShell equivalent) |
| `L1390` | `| `L869` | `| `L449` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L1391` | `| `L870` | `| `L450` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1392` | `| `L871` | `| `L451` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1395` | `| `L876` | `| `L456` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Unix command (use PowerShell equivalent) |
| `L1398` | `| `L880` | `| `L460` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Unix command (use PowerShell equivalent) |
| `L1407` | `| `L890` | `| `L555` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Unix force-remove command (use PowerShell equivalent) |
| `L1408` | `| `L891` | `| `L562` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Unix force-remove command (use PowerShell equivalent) |
| `L1410` | `| `L893` | `| `L658` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Unix command (use PowerShell equivalent) |
| `L1412` | `| `L895` | `| `L668` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Unix command (use PowerShell equivalent) |
| `L1414` | `| `L897` | `| `L709` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Unix command (use PowerShell equivalent) |
| `L1415` | `| `L898` | `| `L710` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L1416` | `| `L899` | `| `L711` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L1421` | `| `L904` | `| `L723` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Unix command (use PowerShell equivalent) |
| `L1425` | `| `L908` | `| `L727` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Unix command (use PowerShell equivalent) |
| `L1435` | `| `L1014` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/d` | Unix force-remove command (use PowerShell equivalent) |
| `L1436` | `| `L1021` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/d` | Unix force-remove command (use PowerShell equivalent) |
| `L1438` | `| `L1152` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/va` | Unix command (use PowerShell equivalent) |
| `L1440` | `| `L1162` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/va` | Unix command (use PowerShell equivalent) |
| `L1442` | `| `L1203` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` |` | Unix command (use PowerShell equivalent) |
| `L1443` | `| `L1204` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L1444` | `| `L1205` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L1449` | `| `L1217` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` |` | Unix command (use PowerShell equivalent) |
| `L1453` | `| `L1221` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L1476` | `| `L82` | `Also, sanitize any Unix commands (like `mkdir -p` or `find`) in their` | Unix nested directory creation (use PowerShell equivalent) |
| `L1477` | `| `L92` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detecte` | Unix nested directory creation (use PowerShell equivalent) |
| `L1478` | `| `L155` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detect` | Unix nested directory creation (use PowerShell equivalent) |
| `L1479` | `| `L208` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detect` | Unix nested directory creation (use PowerShell equivalent) |
| `L1487` | `| `L76` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detecte` | Unix nested directory creation (use PowerShell equivalent) |
| `L1488` | `| `L150` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detect` | Unix nested directory creation (use PowerShell equivalent) |
| `L1510` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1511` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1513` | `| `L698` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|r` | Unix text processing utilities (use PowerShell or Python) |
| `L1514` | `| `L759` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-` | Unix command (use PowerShell equivalent) |
| `L1515` | `| `L760` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-` | Unix command (use PowerShell equivalent) |
| `L1516` | `| `L922` | `- Discover design docs: `ls -t ~/.gstack/projects/$SLUG/*-design-*.m` | Unix command (use PowerShell equivalent) |
| `L1517` | `| `L923` | `- Detect UI scope: grep the plan for view/rendering terms (component` | Unix text processing utilities (use PowerShell or Python) |
| `L1518` | `| `L926` | `- Detect DX scope: grep the plan for developer-facing terms (API, en` | Unix text processing utilities (use PowerShell or Python) |
| `L1526` | `| `L410` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L1527` | `| `L411` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L1535` | `| `L412` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L1536` | `| `L413` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L1551` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1552` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1554` | `| `L666` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L1555` | `| `L667` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L1556` | `| `L706` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|r` | Unix text processing utilities (use PowerShell or Python) |
| `L1564` | `| `L5` | `Safety guardrails for destructive commands. Warns before rm -rf, DROP ` | Unix force-remove command (use PowerShell equivalent) |
| `L1566` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/data` | Recurs` | Unix force-remove command (use PowerShell equivalent) |
| `L1567` | `| `L60` | `| `docker rm -f` / `docker system prune` | `docker system prune -a` |` | Unix force-remove command (use PowerShell equivalent) |
| `L1568` | `| `L65` | `- `rm -rf node_modules` / `.next` / `dist` / `__pycache__` / `.cache`` | Unix force-remove command (use PowerShell equivalent) |
| `L1573` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/data` | Recurs` | Unix force-remove command (use PowerShell equivalent) |
| `L1582` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1583` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1585` | `| `L803` | `find "$CHECKPOINT_DIR" -maxdepth 1 -name "*.md" -type f | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L1586` | `| `L866` | `find "$CHECKPOINT_DIR" -maxdepth 1 -name "*.md" -type f | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L1594` | `| `L343` | `_GBRAIN_VERSION_OK=$(gbrain --version  | grep -c '^gbrain ' || echo ` | Unix text processing utilities (use PowerShell or Python) |
| `L1595` | `| `L391` | `_BRAIN_LAST=$(cat "$_BRAIN_LAST_PULL_FILE"  || echo 0)` | Unix comma` | Unix command (use PowerShell equivalent) |
| `L1597` | `| `L411` | `[ -f "$_GSTACK_HOME/.brain-last-push" ] ; _BRAIN_LAST_PUSH=$(cat "$_` | Unix command (use PowerShell equivalent) |
| `L1598` | `| `L463` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are` | Unix text processing utilities (use PowerShell or Python) |
| `L1598` | `| `L463` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are` | Unix command (use PowerShell equivalent) |
| `L1599` | `| `L463` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are` | Unix text processing utilities (use PowerShell or Python) |
| `L1599` | `| `L463` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are` | Unix command (use PowerShell equivalent) |
| `L1601` | `| `L494` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl"  | ` | Unix text processing utilities (use PowerShell or Python) |
| `L1602` | `| `L496` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1603` | `| `L499` | `_LATEST_CP=$(Get-ChildItem "$_PROJ/checkpoints" -name "*.md" -type f` | Unix command (use PowerShell equivalent) |
| `L1604` | `| `L761` | ``ls -1t` (filesystem mtime). Filenames are stable across file-system` | Unix command (use PowerShell equivalent) |
| `L1612` | `| `L342` | `_GBRAIN_VERSION_OK=$(gbrain --version  | grep -c '^gbrain ' || echo ` | Unix text processing utilities (use PowerShell or Python) |
| `L1613` | `| `L390` | `_BRAIN_LAST=$(cat "$_BRAIN_LAST_PULL_FILE"  || echo 0)` | Unix comma` | Unix command (use PowerShell equivalent) |
| `L1615` | `| `L410` | `[ -f "$_GSTACK_HOME/.brain-last-push" ] ; _BRAIN_LAST_PUSH=$(cat "$_` | Unix command (use PowerShell equivalent) |
| `L1616` | `| `L462` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are` | Unix text processing utilities (use PowerShell or Python) |
| `L1616` | `| `L462` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are` | Unix command (use PowerShell equivalent) |
| `L1617` | `| `L462` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are` | Unix text processing utilities (use PowerShell or Python) |
| `L1617` | `| `L462` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are` | Unix command (use PowerShell equivalent) |
| `L1619` | `| `L493` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl"  | ` | Unix text processing utilities (use PowerShell or Python) |
| `L1620` | `| `L495` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1621` | `| `L498` | `_LATEST_CP=$(Get-ChildItem "$_PROJ/checkpoints" -name "*.md" -type f` | Unix command (use PowerShell equivalent) |
| `L1630` | `| `L294` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1631` | `| `L297` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1634` | `| `L700` | `ls package.json tsconfig.json | Out-Null ; echo "STACK: Node/TypeScr` | Unix command (use PowerShell equivalent) |
| `L1635` | `| `L701` | `ls Gemfile | Out-Null ; echo "STACK: Ruby"` | Unix command (use Powe` | Unix command (use PowerShell equivalent) |
| `L1636` | `| `L702` | `ls requirements.txt pyproject.toml setup.py | Out-Null ; echo "STACK` | Unix command (use PowerShell equivalent) |
| `L1637` | `| `L703` | `ls go.mod | Out-Null ; echo "STACK: Go"` | Unix command (use PowerSh` | Unix command (use PowerShell equivalent) |
| `L1638` | `| `L704` | `ls Cargo.toml | Out-Null ; echo "STACK: Rust"` | Unix command (use P` | Unix command (use PowerShell equivalent) |
| `L1639` | `| `L705` | `ls pom.xml build.gradle | Out-Null ; echo "STACK: JVM"` | Unix comma` | Unix command (use PowerShell equivalent) |
| `L1640` | `| `L706` | `ls composer.json | Out-Null ; echo "STACK: PHP"` | Unix command (use` | Unix command (use PowerShell equivalent) |
| `L1641` | `| `L707` | `find . -maxdepth 1 \( -name '*.csproj' -o -name '*.sln' \) | Out-Nul` | Unix text processing utilities (use PowerShell or Python) |
| `L1642` | `| `L712` | `grep -q "next" package.json | Out-Null ; echo "FRAMEWORK: Next.js"` ` | Unix text processing utilities (use PowerShell or Python) |
| `L1643` | `| `L713` | `grep -q "express" package.json | Out-Null ; echo "FRAMEWORK: Express` | Unix text processing utilities (use PowerShell or Python) |
| `L1644` | `| `L714` | `grep -q "fastify" package.json | Out-Null ; echo "FRAMEWORK: Fastify` | Unix text processing utilities (use PowerShell or Python) |
| `L1645` | `| `L715` | `grep -q "hono" package.json | Out-Null ; echo "FRAMEWORK: Hono"` | U` | Unix text processing utilities (use PowerShell or Python) |
| `L1646` | `| `L716` | `grep -q "django" requirements.txt pyproject.toml | Out-Null ; echo "` | Unix text processing utilities (use PowerShell or Python) |
| `L1647` | `| `L717` | `grep -q "fastapi" requirements.txt pyproject.toml | Out-Null ; echo ` | Unix text processing utilities (use PowerShell or Python) |
| `L1648` | `| `L718` | `grep -q "flask" requirements.txt pyproject.toml | Out-Null ; echo "F` | Unix text processing utilities (use PowerShell or Python) |
| `L1649` | `| `L719` | `grep -q "rails" Gemfile | Out-Null ; echo "FRAMEWORK: Rails"` | Unix` | Unix text processing utilities (use PowerShell or Python) |
| `L1650` | `| `L720` | `grep -q "gin-gonic" go.mod | Out-Null ; echo "FRAMEWORK: Gin"` | Uni` | Unix text processing utilities (use PowerShell or Python) |
| `L1651` | `| `L721` | `grep -q "spring-boot" pom.xml build.gradle | Out-Null ; echo "FRAMEW` | Unix text processing utilities (use PowerShell or Python) |
| `L1652` | `| `L722` | `grep -q "laravel" composer.json | Out-Null ; echo "FRAMEWORK: Larave` | Unix text processing utilities (use PowerShell or Python) |
| `L1653` | `| `L759` | `ls .env .env.* | Out-Null` | Unix command (use PowerShell equivalent` | Unix command (use PowerShell equivalent) |
| `L1654` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.example\|.sampl` | Unix text processing utilities (use PowerShell or Python) |
| `L1654` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.example\|.sampl` | Unix command (use PowerShell equivalent) |
| `L1655` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.example\|.sampl` | Unix text processing utilities (use PowerShell or Python) |
| `L1655` | `| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.example\|.sampl` | Unix command (use PowerShell equivalent) |
| `L1656` | `| `L801` | `grep -q "^\.env$\|^\.env\.\*" .gitignore | Out-Null ; echo ".env IS ` | Unix text processing utilities (use PowerShell or Python) |
| `L1657` | `| `L807` | `[ -f "$f" ] ; grep -n "password:\|token:\|secret:\|api_key:" "$f" | ` | Unix text processing utilities (use PowerShell or Python) |
| `L1658` | `| `L896` | `**Key checks (beyond grep):**` | Unix text processing utilities (use` | Unix text processing utilities (use PowerShell or Python) |
| `L1659` | `| `L914` | `ls -la .agents/skills/ | Out-Null` | Unix command (use PowerShell eq` | Unix command (use PowerShell equivalent) |
| `L1660` | `| `L918` | `- `curl`, `wget`, `fetch`, `http`, `exfiltrat` (network exfiltration` | Unix network tools (use PowerShell or Python) |
| `L1670` | `| `L288` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1671` | `| `L291` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1673` | `| `L679` | `ls DESIGN.md design-system.md | Out-Null ; echo "NO_DESIGN_FILE"` | ` | Unix command (use PowerShell equivalent) |
| `L1674` | `| `L688` | `cat README.md | Out-Null | head -50` | Unix command (use PowerShell ` | Unix command (use PowerShell equivalent) |
| `L1675` | `| `L689` | `cat package.json | Out-Null | head -20` | Unix command (use PowerShe` | Unix command (use PowerShell equivalent) |
| `L1676` | `| `L690` | `ls src/ app/ pages/ components/ | Out-Null | head -30` | Unix comman` | Unix command (use PowerShell equivalent) |
| `L1677` | `| `L698` | `ls ~/.gstack/projects/$SLUG/*office-hours* | Out-Null | head -5` | U` | Unix command (use PowerShell equivalent) |
| `L1678` | `| `L699` | `ls .context/*office-hours* .context/attachments/*office-hours* | Out` | Unix command (use PowerShell equivalent) |
| `L1679` | `| `L731` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L1680` | `| `L732` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L1681` | `| `L1045` | `cat "$_DESIGN_DIR/feedback.json"` | Unix command (use PowerShell eq` | Unix command (use PowerShell equivalent) |
| `L1682` | `| `L1048` | `cat "$_DESIGN_DIR/feedback-pending.json"` | Unix command (use Power` | Unix command (use PowerShell equivalent) |
| `L1683` | `| `L1077` | ``curl -s -X POST http://127.0.0.1:PORT/api/reload -H 'Content-Type:` | Unix network tools (use PowerShell or Python) |
| `L1697` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1698` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1700` | `| `L811` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L1701` | `| `L812` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L1702` | `| `L836` | `_CEO=$(ls -t ~/.gstack/projects/$SLUG/ceo-plans/*.md | Out-Null | he` | Unix command (use PowerShell equivalent) |
| `L1703` | `| `L842` | `_APPROVED=$(ls -t ~/.gstack/projects/$SLUG/designs/*/approved.json |` | Unix command (use PowerShell equivalent) |
| `L1704` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/variant-*.png |` | Unix command (use PowerShell equivalent) |
| `L1705` | `| `L854` | `_FINALIZED=$(ls -t ~/.gstack/projects/$SLUG/designs/*/finalized.html` | Unix command (use PowerShell equivalent) |
| `L1706` | `| `L979` | `[ -f package.json ] ; cat package.json | grep -o '"react"\|"svelte"\` | Unix text processing utilities (use PowerShell or Python) |
| `L1706` | `| `L979` | `[ -f package.json ] ; cat package.json | grep -o '"react"\|"svelte"\` | Unix command (use PowerShell equivalent) |
| `L1707` | `| `L979` | `[ -f package.json ] ; cat package.json | grep -o '"react"\|"svelte"\` | Unix text processing utilities (use PowerShell or Python) |
| `L1707` | `| `L979` | `[ -f package.json ] ; cat package.json | grep -o '"react"\|"svelte"\` | Unix command (use PowerShell equivalent) |
| `L1708` | `| `L1226` | `_PORT=$(lsof -i -P -n | grep "$_SERVER_PID" | grep LISTEN | awk '{p` | Unix text processing utilities (use PowerShell or Python) |
| `L1714` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/variant-*.png |` | Unix command (use PowerShell equivalent) |
| `L1723` | `| `L288` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1724` | `| `L291` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1726` | `| `L689` | `$B status | Out-Null | grep -q "Mode: cdp" ; echo "CDP_MODE=true" ; ` | Unix text processing utilities (use PowerShell or Python) |
| `L1727` | `| `L740` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L1728` | `| `L741` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L1729` | `| `L770` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | Out-Null ; echo "FRAMEWOR` | Unix text processing utilities (use PowerShell or Python) |
| `L1730` | `| `L771` | `[ -f package.json ] ; grep -q '"next"' package.json | Out-Null ; ech` | Unix text processing utilities (use PowerShell or Python) |
| `L1731` | `| `L773` | `ls jest.config.* vitest.config.* playwright.config.* .rspec pytest.i` | Unix command (use PowerShell equivalent) |
| `L1732` | `| `L774` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Unix` | Unix command (use PowerShell equivalent) |
| `L1733` | `| `L859` | `ls -d .github/ | Out-Null ; echo "CI:github"` | Unix command (use Po` | Unix command (use PowerShell equivalent) |
| `L1734` | `| `L860` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | Out-Null` | Unix command ` | Unix command (use PowerShell equivalent) |
| `L1748` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1749` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1751` | `| `L829` | `cat DESIGN.md | Out-Null | head -80 ; echo "NO_DESIGN_MD"` | Unix co` | Unix command (use PowerShell equivalent) |
| `L1752` | `| `L833` | `ls src/ app/ pages/ components/ | Out-Null | head -30` | Unix comman` | Unix command (use PowerShell equivalent) |
| `L1753` | `| `L838` | `ls ~/.gstack/projects/$SLUG/*office-hours* | Out-Null | head -5` | U` | Unix command (use PowerShell equivalent) |
| `L1754` | `| `L848` | `curl -s -o $null -w "%{http_code}" http://localhost:3000 | Out-Null ` | Unix network tools (use PowerShell or Python) |
| `L1755` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` | Unix command` | Unix command (use PowerShell equivalent) |
| `L1756` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' |` | Unix text processing utilities (use PowerShell or Python) |
| `L1756` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' |` | Unix command (use PowerShell equivalent) |
| `L1757` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' |` | Unix text processing utilities (use PowerShell or Python) |
| `L1757` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' |` | Unix command (use PowerShell equivalent) |
| `L1758` | `| `L1043` | `cat "$_DESIGN_DIR/feedback.json"` | Unix command (use PowerShell eq` | Unix command (use PowerShell equivalent) |
| `L1759` | `| `L1046` | `cat "$_DESIGN_DIR/feedback-pending.json"` | Unix command (use Power` | Unix command (use PowerShell equivalent) |
| `L1760` | `| `L1075` | ``curl -s -X POST http://127.0.0.1:PORT/api/reload -H 'Content-Type:` | Unix network tools (use PowerShell or Python) |
| `L1769` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` | Hardcoded Un` | Unix command (use PowerShell equivalent) |
| `L1773` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' |` | Unix text processing utilities (use PowerShell or Python) |
| `L1773` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' |` | Unix command (use PowerShell equivalent) |
| `L1783` | `| `L292` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1784` | `| `L295` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1786` | `| `L697` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|r` | Unix text processing utilities (use PowerShell or Python) |
| `L1787` | `| `L732` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L1788` | `| `L733` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L1790` | `| `L849` | `$GSTACK_ROOT/bin/gstack-review-read | Out-Null | grep plan-devex-rev` | Unix text processing utilities (use PowerShell or Python) |
| `L1791` | `| `L903` | `- Deprecation warnings in code (grep for deprecated/obsolete)` | Uni` | Unix text processing utilities (use PowerShell or Python) |
| `L1799` | `| `L345` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | grep -c '^gbrain` | Unix text processing utilities (use PowerShell or Python) |
| `L1801` | `| `L465` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, grep). The de` | Unix text processing utilities (use PowerShell or Python) |
| `L1803` | `| `L496` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>/` | Unix text processing utilities (use PowerShell or Python) |
| `L1804` | `| `L498` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1806` | `| `L668` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|r` | Unix text processing utilities (use PowerShell or Python) |
| `L1807` | `| `L871` | `- Use ASCII diagrams for architecture. They're grep-able, diff-frien` | Unix text processing utilities (use PowerShell or Python) |
| `L1808` | `| `L1036` | `git diff --cached --no-color | grep '^+' | sed 's/^+//' | \` | Unix` | Unix text processing utilities (use PowerShell or Python) |
| `L1817` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1818` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1820` | `| `L672` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|r` | Unix text processing utilities (use PowerShell or Python) |
| `L1821` | `| `L939` | `git commit -m "$(cat <<'EOF'` | Unix command (use PowerShell equival` | Unix command (use PowerShell equivalent) |
| `L1822` | `| `L984` | `glab mr update -d "$(cat <<'MRBODY'` | Unix command (use PowerShell ` | Unix command (use PowerShell equivalent) |
| `L1843` | `| `L6` | `Combines /gs:careful (warns before rm -rf, DROP TABLE, force-push, etc` | Unix force-remove command (use PowerShell equivalent) |
| `L1845` | `| `L89` | `- "1. **Destructive command warnings** — rm -rf, DROP TABLE, force-pu` | Unix force-remove command (use PowerShell equivalent) |
| `L1854` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1855` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1857` | `| `L675` | `ls eslint.config.* .eslintrc.* .eslintrc | Out-Null | head -1 | xarg` | Unix command (use PowerShell equivalent) |
| `L1858` | `| `L676` | `[ -f .pylintrc ] ; [ -f pyproject.toml ] ; grep -q "pylint\|ruff" py` | Unix text processing utilities (use PowerShell or Python) |
| `L1859` | `| `L679` | `[ -f package.json ] ; grep -q '"test"' package.json | Out-Null ; ech` | Unix text processing utilities (use PowerShell or Python) |
| `L1860` | `| `L680` | `[ -f pyproject.toml ] ; grep -q "pytest" pyproject.toml | Out-Null ;` | Unix text processing utilities (use PowerShell or Python) |
| `L1861` | `| `L686` | `[ -f package.json ] ; grep -q '"knip"' package.json | Out-Null ; ech` | Unix text processing utilities (use PowerShell or Python) |
| `L1862` | `| `L689` | `command -v shellcheck | Out-Null 2>&1 ; ls *.sh scripts/*.sh bin/*.s` | Unix command (use PowerShell equivalent) |
| `L1871` | `| `L304` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1872` | `| `L307` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1882` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1883` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1885` | `| `L684` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L1886` | `| `L685` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L1887` | `| `L724` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|r` | Unix text processing utilities (use PowerShell or Python) |
| `L1888` | `| `L825` | `SAVED_HASH=$(cat ~/.gstack/projects/$SLUG/land-deploy-confirmed | Ou` | Unix command (use PowerShell equivalent) |
| `L1889` | `| `L826` | `CURRENT_HASH=$(sed -n '/## Deploy Configuration/,/^## /p' CLAUDE.md ` | Unix text processing utilities (use PowerShell or Python) |
| `L1891` | `| `L865` | `DEPLOY_CONFIG=$(grep -A 20 "## Deploy Configuration" CLAUDE.md | Out` | Unix text processing utilities (use PowerShell or Python) |
| `L1892` | `| `L870` | `PROD_URL=$(echo "$DEPLOY_CONFIG" | grep -i "production.*url" | head ` | Unix text processing utilities (use PowerShell or Python) |
| `L1893` | `| `L871` | `PLATFORM=$(echo "$DEPLOY_CONFIG" | grep -i "platform" | head -1 | se` | Unix text processing utilities (use PowerShell or Python) |
| `L1894` | `| `L886` | `[ -f "$f" ] ; grep -qiE "deploy|release|production|cd" "$f" | Out-Nu` | Unix text processing utilities (use PowerShell or Python) |
| `L1895` | `| `L887` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Out-Null ; echo "STAGING_WO` | Unix text processing utilities (use PowerShell or Python) |
| `L1896` | `| `L932` | `║  ├─ curl prod URL:      ✓ PASS (200 OK) / ⚠ UNREACHABLE   ║` | Uni` | Unix network tools (use PowerShell or Python) |
| `L1897` | `| `L953` | `failed at Step 1). If `curl` fails, note "I couldn't reach that URL ` | Unix network tools (use PowerShell or Python) |
| `L1898` | `| `L966` | `grep -i "staging" CLAUDE.md | Out-Null | head -3` | Unix text proces` | Unix text processing utilities (use PowerShell or Python) |
| `L1899` | `| `L972` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Out-Null ; echo "STAGING_WO` | Unix text processing utilities (use PowerShell or Python) |
| `L1900` | `| `L1020` | `CURRENT_HASH=$(sed -n '/## Deploy Configuration/,/^## /p' CLAUDE.md` | Unix text processing utilities (use PowerShell or Python) |
| `L1902` | `| `L1130` | `cat $GSTACK_ROOT/review/checklist.md | Out-Null ; echo "Checklist n` | Unix command (use PowerShell equivalent) |
| `L1903` | `| `L1164` | `ls -t ~/.gstack-dev/evals/*-e2e-*-$(date +%Y-%m-%d)*.json | Out-Nul` | Unix command (use PowerShell equivalent) |
| `L1904` | `| `L1180` | `ls -t ~/.gstack-dev/evals/*-llm-judge-*-$(date +%Y-%m-%d)*.json | O` | Unix command (use PowerShell equivalent) |
| `L1905` | `| `L1210` | `git log --oneline --all-match --grep="docs:" $(gh pr view --json ba` | Unix text processing utilities (use PowerShell or Python) |
| `L1906` | `| `L1365` | `DEPLOY_CONFIG=$(grep -A 20 "## Deploy Configuration" CLAUDE.md | Ou` | Unix text processing utilities (use PowerShell or Python) |
| `L1907` | `| `L1370` | `PROD_URL=$(echo "$DEPLOY_CONFIG" | grep -i "production.*url" | head` | Unix text processing utilities (use PowerShell or Python) |
| `L1908` | `| `L1371` | `PLATFORM=$(echo "$DEPLOY_CONFIG" | grep -i "platform" | head -1 | s` | Unix text processing utilities (use PowerShell or Python) |
| `L1909` | `| `L1386` | `[ -f "$f" ] ; grep -qiE "deploy|release|production|cd" "$f" | Out-N` | Unix text processing utilities (use PowerShell or Python) |
| `L1910` | `| `L1387` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Out-Null ; echo "STAGING_W` | Unix text processing utilities (use PowerShell or Python) |
| `L1911` | `| `L1486` | `curl -sf {production-url} -o $null -w "%{http_code}" | Out-Null` | ` | Unix network tools (use PowerShell or Python) |
| `L1920` | `| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1921` | `| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1923` | `| `L768` | `cat "$LEARN_FILE" | bun -e "` | Unix command (use PowerShell equival` | Unix command (use PowerShell equivalent) |
| `L1940` | `| `L264` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | grep -c '^gbrain` | Unix text processing utilities (use PowerShell or Python) |
| `L1942` | `| `L384` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, grep). The de` | Unix text processing utilities (use PowerShell or Python) |
| `L1958` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1959` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1961` | `| `L694` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L1962` | `| `L695` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L1963` | `| `L731` | `ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-Null` | Unix comm` | Unix command (use PowerShell equivalent) |
| `L1964` | `| `L986` | `Extract 3-5 significant keywords from the user's problem statement a` | Unix text processing utilities (use PowerShell or Python) |
| `L1965` | `| `L989` | `grep -li "<keyword1>\|<keyword2>\|<keyword3>" ~/.gstack/projects/$SL` | Unix text processing utilities (use PowerShell or Python) |
| `L1966` | `| `L1159` | `4. POST the new HTML to the running server via `curl -X POST http:/` | Unix network tools (use PowerShell or Python) |
| `L1967` | `| `L1253` | `Use a 5-minute timeout (`timeout: 300000`). After completion: `cat ` | Unix command (use PowerShell equivalent) |
| `L1968` | `| `L1253` | `Use a 5-minute timeout (`timeout: 300000`). After completion: `cat ` | Unix command (use PowerShell equivalent) |
| `L1969` | `| `L1321` | `PRIOR=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-` | Unix command (use PowerShell equivalent) |
| `L1970` | `| `L1532` | `SESSION_TIER=$(echo "$PROFILE" | grep "^TIER:" | awk '{print $2}')`` | Unix text processing utilities (use PowerShell or Python) |
| `L1971` | `| `L1533` | `SESSION_COUNT=$(echo "$PROFILE" | grep "^SESSION_COUNT:" | awk '{pr` | Unix text processing utilities (use PowerShell or Python) |
| `L1985` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L1986` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L1988` | `| `L689` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L1989` | `| `L690` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L1990` | `| `L711` | `_OLD_PID=$(cat "$(git rev-parse --show-toplevel)/.gstack/browse.json` | Unix command (use PowerShell equivalent) |
| `L1991` | `| `L711` | `_OLD_PID=$(cat "$(git rev-parse --show-toplevel)/.gstack/browse.json` | Unix command (use PowerShell equivalent) |
| `L1992` | `| `L756` | `cat "$(git rev-parse --show-toplevel | Out-Null)/.gstack/browse.json` | Unix command (use PowerShell equivalent) |
| `L1993` | `| `L756` | `cat "$(git rev-parse --show-toplevel | Out-Null)/.gstack/browse.json` | Unix command (use PowerShell equivalent) |
| `L2002` | `| `L287` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L2003` | `| `L290` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L2005` | `| `L711` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L2006` | `| `L712` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L2007` | `| `L908` | ``exec curl` syntax which OpenClaw understands natively. When using `` | Unix network tools (use PowerShell or Python) |
| `L2008` | `| `L915` | `curl commands work directly. When using `--local codex`, credentials` | Unix network tools (use PowerShell or Python) |
| `L2017` | `| `L289` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L2018` | `| `L292` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L2020` | `| `L694` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|r` | Unix text processing utilities (use PowerShell or Python) |
| `L2021` | `| `L779` | `grep -r "TODO\|FIXME\|HACK\|XXX" -l --exclude-dir=node_modules --exc` | Unix text processing utilities (use PowerShell or Python) |
| `L2022` | `| `L789` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-` | Unix command (use PowerShell equivalent) |
| `L2023` | `| `L790` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-` | Unix command (use PowerShell equivalent) |
| `L2024` | `| `L798` | `HANDOFF=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-ceo-handoff-*.md ` | Unix command (use PowerShell equivalent) |
| `L2025` | `| `L860` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-` | Unix command (use PowerShell equivalent) |
| `L2026` | `| `L861` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-` | Unix command (use PowerShell equivalent) |
| `L2035` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L2036` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L2038` | `| `L691` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|r` | Unix text processing utilities (use PowerShell or Python) |
| `L2039` | `| `L980` | `- `mkdir -p ~/.gstack/projects/$SLUG/designs/...`` | Unix nested dir` | Unix nested directory creation (use PowerShell equivalent) |
| `L2040` | `| `L1057` | `cat "$_DESIGN_DIR/feedback.json"` | Unix command (use PowerShell eq` | Unix command (use PowerShell equivalent) |
| `L2041` | `| `L1060` | `cat "$_DESIGN_DIR/feedback-pending.json"` | Unix command (use Power` | Unix command (use PowerShell equivalent) |
| `L2042` | `| `L1089` | ``curl -s -X POST http://127.0.0.1:PORT/api/reload -H 'Content-Type:` | Unix network tools (use PowerShell or Python) |
| `L2056` | `| `L296` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L2057` | `| `L299` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L2059` | `| `L701` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|r` | Unix text processing utilities (use PowerShell or Python) |
| `L2061` | `| `L832` | `- Getting started guides (grep README for "Getting Started", "Quick ` | Unix text processing utilities (use PowerShell or Python) |
| `L2062` | `| `L833` | `- CLI help text (grep for `--help`, `usage:`, `commands:`)` | Unix t` | Unix text processing utilities (use PowerShell or Python) |
| `L2063` | `| `L834` | `- Error message patterns (grep for `throw new Error`, `console.error` | Unix text processing utilities (use PowerShell or Python) |
| `L2064` | `| `L842` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-` | Unix command (use PowerShell equivalent) |
| `L2065` | `| `L843` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-` | Unix command (use PowerShell equivalent) |
| `L2066` | `| `L902` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-` | Unix command (use PowerShell equivalent) |
| `L2067` | `| `L903` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-` | Unix command (use PowerShell equivalent) |
| `L2068` | `| `L1264` | `$GSTACK_ROOT/bin/gstack-review-read | Out-Null | grep plan-devex-re` | Unix text processing utilities (use PowerShell or Python) |
| `L2077` | `| `L291` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L2078` | `| `L294` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L2080` | `| `L720` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-` | Unix command (use PowerShell equivalent) |
| `L2081` | `| `L721` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-` | Unix command (use PowerShell equivalent) |
| `L2082` | `| `L775` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-` | Unix command (use PowerShell equivalent) |
| `L2083` | `| `L776` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-` | Unix command (use PowerShell equivalent) |
| `L2084` | `| `L896` | `ls jest.config.* vitest.config.* playwright.config.* cypress.config.` | Unix command (use PowerShell equivalent) |
| `L2085` | `| `L897` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Unix` | Unix command (use PowerShell equivalent) |
| `L2094` | `| `L296` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L2095` | `| `L299` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L2105` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L2106` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L2108` | `| `L707` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L2109` | `| `L708` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L2110` | `| `L748` | `ls -t ~/.gstack/projects/$SLUG/*-test-plan-*.md | Out-Null | head -1` | Unix command (use PowerShell equivalent) |
| `L2124` | `| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L2125` | `| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L2127` | `| `L698` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|r` | Unix text processing utilities (use PowerShell or Python) |
| `L2128` | `| `L738` | `$B status | Out-Null | grep -q "Mode: cdp" ; echo "CDP_MODE=true" ; ` | Unix text processing utilities (use PowerShell or Python) |
| `L2129` | `| `L785` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L2130` | `| `L786` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L2131` | `| `L815` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | Out-Null ; echo "FRAMEWOR` | Unix text processing utilities (use PowerShell or Python) |
| `L2132` | `| `L816` | `[ -f package.json ] ; grep -q '"next"' package.json | Out-Null ; ech` | Unix text processing utilities (use PowerShell or Python) |
| `L2133` | `| `L818` | `ls jest.config.* vitest.config.* playwright.config.* .rspec pytest.i` | Unix command (use PowerShell equivalent) |
| `L2134` | `| `L819` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Unix` | Unix command (use PowerShell equivalent) |
| `L2135` | `| `L904` | `ls -d .github/ | Out-Null ; echo "CI:github"` | Unix command (use Po` | Unix command (use PowerShell equivalent) |
| `L2136` | `| `L905` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | Out-Null` | Unix command ` | Unix command (use PowerShell equivalent) |
| `L2137` | `| `L981` | `ls -t ~/.gstack/projects/$SLUG/*-test-plan-*.md | Out-Null | head -1` | Unix command (use PowerShell equivalent) |
| `L2151` | `| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L2152` | `| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L2154` | `| `L670` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|r` | Unix text processing utilities (use PowerShell or Python) |
| `L2155` | `| `L770` | `git log origin/<default> --since="<window>" --format="" --name-only ` | Unix text processing utilities (use PowerShell or Python) |
| `L2156` | `| `L773` | `git log origin/<default> --since="<window>" --format="%s" | grep -oE` | Unix text processing utilities (use PowerShell or Python) |
| `L2157` | `| `L782` | `cat ~/.gstack/greptile-history.md | Out-Null ; true` | Unix command ` | Unix command (use PowerShell equivalent) |
| `L2158` | `| `L785` | `cat TODOS.md | Out-Null ; true` | Unix command (use PowerShell equiv` | Unix command (use PowerShell equivalent) |
| `L2160` | `| `L791` | `git log origin/<default> --since="<window>" --oneline --grep="test(q` | Unix text processing utilities (use PowerShell or Python) |
| `L2161` | `| `L794` | `cat ~/.gstack/analytics/skill-usage.jsonl | Out-Null ; true` | Unix ` | Unix command (use PowerShell equivalent) |
| `L2162` | `| `L797` | `git log origin/<default> --since="<window>" --format="" --name-only ` | Unix text processing utilities (use PowerShell or Python) |
| `L2163` | `| `L1029` | `ls -t .context/retros/*.json | Out-Null` | Unix command (use PowerS` | Unix command (use PowerShell equivalent) |
| `L2164` | `| `L1058` | `existing=$(ls .context/retros/${today}-*.json | Out-Null | wc -l | ` | Unix command (use PowerShell equivalent) |
| `L2165` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Null | grep '"sk` | Unix text processing utilities (use PowerShell or Python) |
| `L2165` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Null | grep '"sk` | Unix command (use PowerShell equivalent) |
| `L2166` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Null | grep '"sk` | Unix text processing utilities (use PowerShell or Python) |
| `L2166` | `| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Null | grep '"sk` | Unix command (use PowerShell equivalent) |
| `L2168` | `| `L1482` | `ls -t ~/.gstack/retros/global-*.json | Out-Null | head -5` | Unix c` | Unix command (use PowerShell equivalent) |
| `L2169` | `| `L1501` | `existing=$(ls ~/.gstack/retros/global-${today}-*.json | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L2183` | `| `L287` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L2184` | `| `L290` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L2186` | `| `L692` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|r` | Unix text processing utilities (use PowerShell or Python) |
| `L2187` | `| `L764` | `_PLAN_SLUG=$(git remote get-url origin | Out-Null | sed 's|.*[:/]\([` | Unix text processing utilities (use PowerShell or Python) |
| `L2188` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" |` | Unix text processing utilities (use PowerShell or Python) |
| `L2188` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" |` | Unix command (use PowerShell equivalent) |
| `L2189` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" |` | Unix text processing utilities (use PowerShell or Python) |
| `L2189` | `| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" |` | Unix command (use PowerShell equivalent) |
| `L2190` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs gr` | Unix text processing utilities (use PowerShell or Python) |
| `L2190` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs gr` | Unix command (use PowerShell equivalent) |
| `L2191` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs gr` | Unix text processing utilities (use PowerShell or Python) |
| `L2191` | `| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs gr` | Unix command (use PowerShell equivalent) |
| `L2200` | `| `L334` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper ` | Unix text processing utilities (use PowerShell or Python) |
| `L2200` | `| `L334` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper ` | Unix command (use PowerShell equivalent) |
| `L2201` | `| `L334` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper ` | Unix text processing utilities (use PowerShell or Python) |
| `L2201` | `| `L334` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper ` | Unix command (use PowerShell equivalent) |
| `L2203` | `| `L370` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L2204` | `| `L373` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L2213` | `| `L389` | `$B status | Out-Null | grep -q "Mode: cdp" ; echo "CDP_MODE=true" ; ` | Unix text processing utilities (use PowerShell or Python) |
| `L2214` | `| `L427` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L2215` | `| `L428` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L2224` | `| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L2225` | `| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L2227` | `| `L662` | `grep -A 20 "## Deploy Configuration" CLAUDE.md | Out-Null ; echo "NO` | Unix text processing utilities (use PowerShell or Python) |
| `L2228` | `| `L681` | `[ -f fly.toml ] ; echo "PLATFORM:fly" ; cat fly.toml` | Unix command` | Unix command (use PowerShell equivalent) |
| `L2229` | `| `L682` | `[ -f render.yaml ] ; echo "PLATFORM:render" ; cat render.yaml` | Uni` | Unix command (use PowerShell equivalent) |
| `L2230` | `| `L684` | `[ -f netlify.toml ] ; echo "PLATFORM:netlify" ; cat netlify.toml` | ` | Unix command (use PowerShell equivalent) |
| `L2231` | `| `L690` | `[ -f "$f" ] ; grep -qiE "deploy|release|production|staging|cd" "$f" ` | Unix text processing utilities (use PowerShell or Python) |
| `L2232` | `| `L694` | `[ -f package.json ] ; grep -q '"bin"' package.json | Out-Null ; echo` | Unix text processing utilities (use PowerShell or Python) |
| `L2233` | `| `L695` | `find . -maxdepth 1 -name '*.gemspec' | Out-Null | grep -q . ; echo "` | Unix text processing utilities (use PowerShell or Python) |
| `L2234` | `| `L706` | `1. Extract app name: `grep -m1 "^app" fly.toml | sed 's/app = "\(.*\` | Unix text processing utilities (use PowerShell or Python) |
| `L2235` | `| `L734` | `2. If installed: `vercel ls --prod 2>/dev/null | head -3`` | Unix co` | Unix command (use PowerShell equivalent) |
| `L2236` | `| `L807` | `curl -sf "{health-check-url}" -o $null -w "%{http_code}" | Out-Null ` | Unix network tools (use PowerShell or Python) |
| `L2245` | `| `L289` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | O` | Unix text processing utilities (use PowerShell or Python) |
| `L2246` | `| `L292` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L2248` | `| `L694` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|r` | Unix text processing utilities (use PowerShell or Python) |
| `L2249` | `| `L829` | `git diff origin/<base> --name-only | grep -E '(cmd/.*/main\.go|bin/|` | Unix text processing utilities (use PowerShell or Python) |
| `L2250` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE 'release|publish|dist'` ` | Unix text processing utilities (use PowerShell or Python) |
| `L2250` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE 'release|publish|dist'` ` | Unix command (use PowerShell equivalent) |
| `L2251` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE 'release|publish|dist'` ` | Unix text processing utilities (use PowerShell or Python) |
| `L2251` | `| `L834` | `ls .github/workflows/ | Out-Null | grep -iE 'release|publish|dist'` ` | Unix command (use PowerShell equivalent) |
| `L2252` | `| `L835` | `grep -qE 'release|publish|deploy' .gitlab-ci.yml | Out-Null ; echo "` | Unix text processing utilities (use PowerShell or Python) |
| `L2253` | `| `L881` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | Out-Null ; echo "FRAMEWOR` | Unix text processing utilities (use PowerShell or Python) |
| `L2254` | `| `L882` | `[ -f package.json ] ; grep -q '"next"' package.json | Out-Null ; ech` | Unix text processing utilities (use PowerShell or Python) |
| `L2255` | `| `L884` | `ls jest.config.* vitest.config.* playwright.config.* .rspec pytest.i` | Unix command (use PowerShell equivalent) |
| `L2256` | `| `L885` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Unix` | Unix command (use PowerShell equivalent) |
| `L2257` | `| `L970` | `ls -d .github/ | Out-Null ; echo "CI:github"` | Unix command (use Po` | Unix command (use PowerShell equivalent) |
| `L2258` | `| `L971` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | Out-Null` | Unix command ` | Unix command (use PowerShell equivalent) |
| `L2259` | `| `L1176` | `grep -l "changed_file_basename" test/evals/*_eval_runner.rb` | Unix` | Unix text processing utilities (use PowerShell or Python) |
| `L2260` | `| `L1183` | `- Changes to `config/system_prompts/*.txt` — grep eval runners for ` | Unix text processing utilities (use PowerShell or Python) |
| `L2261` | `| `L1238` | `ls jest.config.* vitest.config.* playwright.config.* cypress.config` | Unix command (use PowerShell equivalent) |
| `L2262` | `| `L1239` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Uni` | Unix command (use PowerShell equivalent) |
| `L2265` | `| `L1511` | `_PLAN_SLUG=$(git remote get-url origin | Out-Null | sed 's|.*[:/]\(` | Unix text processing utilities (use PowerShell or Python) |
| `L2266` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" ` | Unix text processing utilities (use PowerShell or Python) |
| `L2266` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" ` | Unix command (use PowerShell equivalent) |
| `L2267` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" ` | Unix text processing utilities (use PowerShell or Python) |
| `L2267` | `| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" ` | Unix command (use PowerShell equivalent) |
| `L2268` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs g` | Unix text processing utilities (use PowerShell or Python) |
| `L2268` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs g` | Unix command (use PowerShell equivalent) |
| `L2269` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs g` | Unix text processing utilities (use PowerShell or Python) |
| `L2269` | `| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs g` | Unix command (use PowerShell equivalent) |
| `L2271` | `| `L1647` | `curl -s -o $null -w '%{http_code}' http://localhost:3000 | Out-Null` | Unix network tools (use PowerShell or Python) |
| `L2272` | `| `L1648` | `curl -s -o $null -w '%{http_code}' http://localhost:8080 | Out-Null` | Unix network tools (use PowerShell or Python) |
| `L2273` | `| `L1649` | `curl -s -o $null -w '%{http_code}' http://localhost:5173 | Out-Null` | Unix network tools (use PowerShell or Python) |
| `L2274` | `| `L1650` | `curl -s -o $null -w '%{http_code}' http://localhost:4000 | Out-Null` | Unix network tools (use PowerShell or Python) |
| `L2275` | `| `L1660` | `cat ${CLAUDE_SKILL_DIR}/../qa-only/SKILL.md` | Unix command (use Po` | Unix command (use PowerShell equivalent) |
| `L2276` | `| `L1964` | `CURRENT_VERSION=$(cat VERSION | Out-Null | tr -d '\r\n[:space:]' ; ` | Unix command (use PowerShell equivalent) |
| `L2277` | `| `L2029` | `if ! printf '%s' "$NEW_VERSION" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+` | Unix text processing utilities (use PowerShell or Python) |
| `L2278` | `| `L2055` | `REPAIR_VERSION=$(cat VERSION | tr -d '\r\n[:space:]')` | Unix comma` | Unix command (use PowerShell equivalent) |
| `L2279` | `| `L2056` | `if ! printf '%s' "$REPAIR_VERSION" | grep -qE '^[0-9]+\.[0-9]+\.[0-` | Unix text processing utilities (use PowerShell or Python) |
| `L2280` | `| `L2203` | `git commit -m "$(cat <<'EOF'` | Unix command (use PowerShell equiva` | Unix command (use PowerShell equivalent) |
| `L2281` | `| `L2366` | `gh pr create --base <base> --title "<type>: <summary>" --body "$(ca` | Unix command (use PowerShell equivalent) |
| `L2282` | `| `L2375` | `glab mr create -b <base> -t "<type>: <summary>" -d "$(cat <<'EOF'` ` | Unix command (use PowerShell equivalent) |
| `L2290` | `| `L358` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper ` | Unix text processing utilities (use PowerShell or Python) |
| `L2290` | `| `L358` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper ` | Unix command (use PowerShell equivalent) |
| `L2291` | `| `L358` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper ` | Unix text processing utilities (use PowerShell or Python) |
| `L2291` | `| `L358` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper ` | Unix command (use PowerShell equivalent) |
| `L2299` | `| `L340` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | grep -c '^gbrain` | Unix text processing utilities (use PowerShell or Python) |
| `L2301` | `| `L460` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, grep). The de` | Unix text processing utilities (use PowerShell or Python) |
| `L2303` | `| `L491` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>/` | Unix text processing utilities (use PowerShell or Python) |
| `L2304` | `| `L493` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.j` | Unix text processing utilities (use PowerShell or Python) |
| `L2306` | `| `L852` | `[ -z "$REDACT_VIS" ] && REDACT_VIS=$(glab repo view -F json 2>/dev/n` | Unix text processing utilities (use PowerShell or Python) |
| `L2307` | `| `L1264` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | grep -c '^gbrai` | Unix text processing utilities (use PowerShell or Python) |
| `L2309` | `| `L1384` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, grep). The d` | Unix text processing utilities (use PowerShell or Python) |
| `L2311` | `| `L1415` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>` | Unix text processing utilities (use PowerShell or Python) |
| `L2312` | `| `L1417` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.` | Unix text processing utilities (use PowerShell or Python) |
| `L2314` | `| `L1611` | `ISSUE_NUMBER=$(echo "$ISSUE_URL" | sed -E 's|.*/issues/([0-9]+)$|\1` | Unix text processing utilities (use PowerShell or Python) |
| `L2330` | `| `L42` | `PREV=$(cat "$STATE_DIR/freeze-dir.txt")` | Unix command (use PowerShe` | Unix command (use PowerShell equivalent) |
| `L2338` | `| `L71` | `_SNOOZED_VER=$(awk '{print $1}' "$_SNOOZE_FILE")` | Unix text process` | Unix text processing utilities (use PowerShell or Python) |
| `L2339` | `| `L73` | `_CUR_LEVEL=$(awk '{print $2}' "$_SNOOZE_FILE")` | Unix text processin` | Unix text processing utilities (use PowerShell or Python) |
| `L2340` | `| `L127` | `OLD_VERSION=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; echo "unknown"` | Unix command (use PowerShell equivalent) |
| `L2341` | `| `L179` | `if ! grep -qF '.agents/skills/gstack/' .gitignore | Out-Null; then` ` | Unix text processing utilities (use PowerShell or Python) |
| `L2342` | `| `L214` | `m_ver="$(basename "$migration" .sh | sed 's/^v//')"` | Unix text pro` | Unix text processing utilities (use PowerShell or Python) |
| `L2343` | `| `L283` | `PRIMARY_VER=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; echo "unknown"` | Unix command (use PowerShell equivalent) |
| `L2344` | `| `L284` | `LOCAL_VER=$(cat "$LOCAL_GSTACK/VERSION" | Out-Null ; echo "unknown")` | Unix command (use PowerShell equivalent) |
| `L2352` | `| `L446` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network to` | Unix network tools (use PowerShell or Python) |
| `L2353` | `| `L447` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix te` | Unix text processing utilities (use PowerShell or Python) |
| `L2354` | `| `L470` | `> Set them before running: `export TEST_EMAIL="..." TEST_PASSWORD=".` | Unix environment variable export (use PowerShell equivalent) |
| `L2368` | `| `L64` | `_SNOOZED_VER=$(awk '{print $1}' "$_SNOOZE_FILE")` | Unix text process` | Unix text processing utilities (use PowerShell or Python) |
| `L2369` | `| `L66` | `_CUR_LEVEL=$(awk '{print $2}' "$_SNOOZE_FILE")` | Unix text processin` | Unix text processing utilities (use PowerShell or Python) |
| `L2370` | `| `L120` | `OLD_VERSION=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; echo "unknown"` | Unix command (use PowerShell equivalent) |
| `L2371` | `| `L172` | `if ! grep -qF '.agents/skills/gstack/' .gitignore | Out-Null; then` ` | Unix text processing utilities (use PowerShell or Python) |
| `L2372` | `| `L207` | `m_ver="$(basename "$migration" .sh | sed 's/^v//')"` | Unix text pro` | Unix text processing utilities (use PowerShell or Python) |
| `L2373` | `| `L276` | `PRIMARY_VER=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; echo "unknown"` | Unix command (use PowerShell equivalent) |
| `L2374` | `| `L277` | `LOCAL_VER=$(cat "$LOCAL_GSTACK/VERSION" | Out-Null ; echo "unknown")` | Unix command (use PowerShell equivalent) |
| `L2382` | `| `L63` | `- **Trace it through every consumer.** Read (don't just grep — READ) ` | Unix text processing utilities (use PowerShell or Python) |
| `L2383` | `| `L66` | `To do this: use Grep to find all references to the sibling values (e.` | Unix text processing utilities (use PowerShell or Python) |
| `L2391` | `| `L25` | `- **[HIGH]** — Reliably detectable via grep/pattern match. Definitive` | Unix text processing utilities (use PowerShell or Python) |
| `L2400` | `| `L6` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detected` | Unix nested directory creation (use PowerShell equivalent) |
| `L2409` | `| `L9` | `if ($content -like $mkdir_pattern) { throw "FAIL: Unix mkdir -p detect` | Unix nested directory creation (use PowerShell equivalent) |
| `L2422` | `| `L5` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detected` | Unix nested directory creation (use PowerShell equivalent) |
| `L2431` | `| `L12` | `if ($content -like "*$unixMkdirPattern*") { throw "FAIL: Unix mkdir -` | Unix nested directory creation (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L217` | `| `L204` | `| `L184` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L218` | `| `L205` | `| `L185` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L219` | `| `L206` | `| `L186` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L220` | `| `L207` | `| `L187` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L221` | `| `L208` | `| `L188` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L225` | `| `L212` | `| `L192` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L226` | `| `L213` | `| `L193` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L227` | `| `L214` | `| `L194` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L493` | `| `L472` | `| `L449` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L494` | `| `L473` | `| `L450` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L495` | `| `L474` | `| `L451` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L496` | `| `L475` | `| `L456` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L497` | `| `L476` | `| `L460` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L518` | `| `L497` | `| `L555` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L521` | `| `L500` | `| `L562` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L577` | `| `L555` | `| `L658` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L588` | `| `L562` | `| `L668` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L606` | `| `L580` | `| `L709` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L607` | `| `L581` | `| `L710` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L608` | `| `L582` | `| `L710` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L609` | `| `L583` | `| `L711` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L610` | `| `L584` | `| `L711` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L614` | `| `L588` | `| `L723` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L615` | `| `L589` | `| `L727` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L616` | `| `L590` | `| `L727` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L893` | `| `L853` | `| `L184` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L894` | `| `L854` | `| `L185` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L895` | `| `L855` | `| `L186` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L896` | `| `L856` | `| `L187` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L897` | `| `L857` | `| `L188` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L898` | `| `L858` | `| `L192` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L899` | `| `L859` | `| `L193` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L900` | `| `L860` | `| `L194` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L905` | `| `L869` | `| `L449` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L906` | `| `L870` | `| `L450` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L907` | `| `L871` | `| `L451` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L908` | `| `L876` | `| `L456` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L909` | `| `L880` | `| `L460` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L910` | `| `L890` | `| `L555` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L911` | `| `L891` | `| `L562` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L912` | `| `L893` | `| `L658` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L913` | `| `L895` | `| `L668` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L914` | `| `L897` | `| `L709` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L915` | `| `L898` | `| `L710` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L916` | `| `L899` | `| `L711` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L917` | `| `L904` | `| `L723` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L918` | `| `L908` | `| `L727` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L943` | `| `L1014` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/d` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L946` | `| `L1021` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/d` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1022` | `| `L1152` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/va` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1029` | `| `L1162` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/va` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1047` | `| `L1203` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` |` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1048` | `| `L1204` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1049` | `| `L1204` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1050` | `| `L1205` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1051` | `| `L1205` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1055` | `| `L1217` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` |` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1056` | `| `L1221` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1057` | `| `L1221` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1341` | `| `L204` | `| `L184` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1342` | `| `L205` | `| `L185` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1343` | `| `L206` | `| `L186` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1344` | `| `L207` | `| `L187` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1345` | `| `L208` | `| `L188` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1346` | `| `L212` | `| `L192` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1347` | `| `L213` | `| `L193` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1348` | `| `L214` | `| `L194` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1353` | `| `L472` | `| `L449` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1354` | `| `L473` | `| `L450` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1355` | `| `L474` | `| `L451` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1356` | `| `L475` | `| `L456` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1357` | `| `L476` | `| `L460` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1358` | `| `L497` | `| `L555` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1359` | `| `L500` | `| `L562` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1360` | `| `L555` | `| `L658` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1361` | `| `L562` | `| `L668` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1362` | `| `L580` | `| `L709` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1363` | `| `L581` | `| `L710` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1364` | `| `L582` | `| `L710` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1365` | `| `L583` | `| `L711` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1366` | `| `L584` | `| `L711` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1367` | `| `L588` | `| `L723` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1368` | `| `L589` | `| `L727` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1369` | `| `L590` | `| `L727` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1374` | `| `L853` | `| `L184` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1375` | `| `L854` | `| `L185` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1376` | `| `L855` | `| `L186` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1377` | `| `L856` | `| `L187` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1378` | `| `L857` | `| `L188` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1379` | `| `L858` | `| `L192` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1380` | `| `L859` | `| `L193` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1381` | `| `L860` | `| `L194` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1382` | `| `L861` | `| `L441` | `| `L116` | `| `L604` | `Example: `$B snapshot -i -a -C -` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1385` | `| `L864` | `| `L444` | `| `L228` | `| `L788` | ``docs/designs/`, `/tmp/`, or any` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1387` | `| `L866` | `| `L446` | `| `L253` | `| `L700` | ``docs/designs/`, `/tmp/`, or any` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1389` | `| `L868` | `| `L448` | `| `L279` | `| `L951` | ``docs/designs/`, `/tmp/`, or any` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1390` | `| `L869` | `| `L449` | `| `L295` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1391` | `| `L870` | `| `L450` | `| `L296` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1392` | `| `L871` | `| `L451` | `| `L297` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1393` | `| `L872` | `| `L452` | `| `L305` | `| `L691` | ``docs/designs/`, `/tmp/`, or any` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1395` | `| `L876` | `| `L456` | `| `L309` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1396` | `| `L877` | `| `L457` | `| `L310` | `| `L976` | `**Why /tmp/ then cp?** In observ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1398` | `| `L880` | `| `L460` | `| `L313` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/vari` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1399` | `| `L882` | `| `L462` | `| `L350` | `| `L982` | `Read the contents of `/tmp/gstac` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1400` | `| `L883` | `| `L463` | `| `L482` | `| `L1228` | `The screenshot file at `/tmp/gs` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1401` | `| `L884` | `| `L464` | `| `L553` | `| `L934` | ``docs/designs/`, `/tmp/`, or any` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1404` | `| `L887` | `| `L467` | `| `L680` | `| `L1277` | `Read the stderr output from `/t` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1405` | `| `L888` | `| `L468` | `| `L812` | `| `L686` | `Example: `$B snapshot -i -a -C -` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1406` | `| `L889` | `| `L530` | `| `L604` | `Example: `$B snapshot -i -a -C -o /tmp/annot` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1407` | `| `L890` | `| `L555` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1408` | `| `L891` | `| `L562` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1409` | `| `L892` | `| `L642` | `| `L788` | ``docs/designs/`, `/tmp/`, or any project-loc` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1410` | `| `L893` | `| `L658` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1411` | `| `L894` | `| `L667` | `| `L700` | ``docs/designs/`, `/tmp/`, or any project-loc` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1412` | `| `L895` | `| `L668` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/d` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1413` | `| `L896` | `| `L693` | `| `L951` | ``docs/designs/`, `/tmp/`, or any project-loc` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1414` | `| `L897` | `| `L709` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1415` | `| `L898` | `| `L710` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1416` | `| `L899` | `| `L711` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1417` | `| `L900` | `| `L719` | `| `L691` | ``docs/designs/`, `/tmp/`, or any project-loc` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1418` | `| `L901` | `| `L720` | `| `L954` | `Final location: {_DESIGN_DIR absolute path}/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1421` | `| `L904` | `| `L723` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{let` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1422` | `| `L905` | `| `L724` | `| `L976` | `**Why /tmp/ then cp?** In observed sessions,` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1424` | `| `L907` | `| `L726` | `| `L978` | `a sandbox restriction. Always generate to `/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1425` | `| `L908` | `| `L727` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1427` | `| `L910` | `| `L764` | `| `L982` | `Read the contents of `/tmp/gstack-pr-body-$$` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1428` | `| `L911` | `| `L896` | `| `L1228` | `The screenshot file at `/tmp/gstack-sketch.` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1429` | `| `L912` | `| `L967` | `| `L934` | ``docs/designs/`, `/tmp/`, or any project-loc` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1430` | `| `L913` | `| `L1035` | `| `L676` | `| Output dir | `.gstack/qa-reports/` | `Out` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1431` | `| `L914` | `| `L1062` | `| `L725` | `| Output dir | `.gstack/qa-reports/` | `Out` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1432` | `| `L915` | `| `L1094` | `| `L1277` | `Read the stderr output from `/tmp/gstack-d` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1433` | `| `L916` | `| `L1248` | `| `L686` | `Example: `$B snapshot -i -a -C -o /tmp/anno` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1434` | `| `L989` | `| `L604` | `Example: `$B snapshot -i -a -C -o /tmp/annotated.png`` |` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1435` | `| `L1014` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/d` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1436` | `| `L1021` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/d` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1437` | `| `L1136` | `| `L788` | ``docs/designs/`, `/tmp/`, or any project-local director` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1438` | `| `L1152` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/va` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1439` | `| `L1161` | `| `L700` | ``docs/designs/`, `/tmp/`, or any project-local director` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1440` | `| `L1162` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/va` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1441` | `| `L1187` | `| `L951` | ``docs/designs/`, `/tmp/`, or any project-local director` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1442` | `| `L1203` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` |` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1443` | `| `L1204` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1444` | `| `L1205` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1445` | `| `L1213` | `| `L691` | ``docs/designs/`, `/tmp/`, or any project-local director` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1446` | `| `L1214` | `| `L954` | `Final location: {_DESIGN_DIR absolute path}/variant-{le` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1447` | `| `L1215` | `| `L961` | `4. Copy: cp $env:TEMP\variant-{letter}.png {_DESIGN_DIR` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1448` | `| `L1216` | `| `L962` | `5. Quality check: {$D path} check --image {_DESIGN_DIR}` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1449` | `| `L1217` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` |` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1450` | `| `L1218` | `| `L976` | `**Why /tmp/ then cp?** In observed sessions, `$D genera` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1451` | `| `L1219` | `| `L977` | `failed with "The operation was aborted" while `--output` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1452` | `| `L1220` | `| `L978` | `a sandbox restriction. Always generate to `/tmp/` first` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1453` | `| `L1221` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1454` | `| `L1222` | `| `L1140` | `1. **Never save to `.context/`, `docs/designs/`, or `/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1455` | `| `L1275` | `| `L982` | `Read the contents of `/tmp/gstack-pr-body-$$.md` using ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1456` | `| `L1395` | `| `L473` | `$P generate letter.md                 # writes /tmp/let` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1457` | `| `L1396` | `| `L573` | `stdout: /tmp/letter.pdf          ← just the path, one l` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1458` | `| `L1397` | `| `L576` | `Done in 1.5s. 43 words · 22KB · /tmp/letter.pdf` | Hard` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1459` | `| `L1424` | `| `L1228` | `The screenshot file at `/tmp/gstack-sketch.png` can be` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1460` | `| `L1495` | `| `L934` | ``docs/designs/`, `/tmp/`, or any project-local director` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1461` | `| `L1563` | `| `L676` | `| Output dir | `.gstack/qa-reports/` | `Output to /tmp/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1462` | `| `L1590` | `| `L725` | `| Output dir | `.gstack/qa-reports/` | `Output to /tmp/` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1463` | `| `L1622` | `| `L1277` | `Read the stderr output from `/tmp/gstack-discover-stde` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1464` | `| `L1767` | `| `L827` | `printf '%s' "<the final draft body>" > /tmp/spec-semant` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1465` | `| `L1768` | `| `L830` | `/tmp/spec-semantic-$$.txt` | Hardcoded Unix path prefix` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1466` | `| `L1769` | `| `L831` | `Remove-Item -Force /tmp/spec-semantic-$$.txt` | Hardcod` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1467` | `| `L1770` | `| `L891` | `TMPERR_GATE=$(mktemp /tmp/spec-gate-XXXXXXXX)` | Hardco` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1468` | `| `L1807` | `| `L686` | `Example: `$B snapshot -i -a -C -o /tmp/annotated.png`` ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1541` | `| `L604` | `Example: `$B snapshot -i -a -C -o /tmp/annotated.png`` | Hardcoded U` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1566` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/data` | Recurs` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1573` | `| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/data` | Recurs` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1688` | `| `L788` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design art` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1704` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/variant-*.png |` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1713` | `| `L700` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design art` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1714` | `| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/variant-*.png |` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1739` | `| `L951` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design art` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1755` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` | Unix command` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1756` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' |` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1757` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' |` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1765` | `| `L691` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design art` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1766` | `| `L954` | `Final location: {_DESIGN_DIR absolute path}/variant-{letter}.png` | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1767` | `| `L961` | `4. Copy: cp $env:TEMP\variant-{letter}.png {_DESIGN_DIR}/variant-{le` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1768` | `| `L962` | `5. Quality check: {$D path} check --image {_DESIGN_DIR}/variant-{let` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1769` | `| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` | Hardcoded Un` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1770` | `| `L976` | `**Why /tmp/ then cp?** In observed sessions, `$D generate --output ~` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1771` | `| `L977` | `failed with "The operation was aborted" while `--output /tmp/...` su` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1772` | `| `L978` | `a sandbox restriction. Always generate to `/tmp/` first, then `cp`.`` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1773` | `| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' |` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1774` | `| `L1140` | `1. **Never save to `.context/`, `docs/designs/`, or `/tmp/`.** All ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1827` | `| `L982` | `Read the contents of `/tmp/gstack-pr-body-$$.md` using the Read tool` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1947` | `| `L473` | `$P generate letter.md                 # writes /tmp/letter.pdf` | Ha` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1948` | `| `L573` | `stdout: /tmp/letter.pdf          ← just the path, one line` | Hardco` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1949` | `| `L576` | `Done in 1.5s. 43 words · 22KB · /tmp/letter.pdf` | Hardcoded Unix pa` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1976` | `| `L1228` | `The screenshot file at `/tmp/gstack-sketch.png` can be referenced b` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L2047` | `| `L934` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design art` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L2115` | `| `L676` | `| Output dir | `.gstack/qa-reports/` | `Output to /tmp/qa` |` | Hard` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L2142` | `| `L725` | `| Output dir | `.gstack/qa-reports/` | `Output to /tmp/qa` |` | Hard` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L2174` | `| `L1277` | `Read the stderr output from `/tmp/gstack-discover-stderr` for diagn` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L2319` | `| `L827` | `printf '%s' "<the final draft body>" > /tmp/spec-semantic-$$.txt` | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L2320` | `| `L830` | `/tmp/spec-semantic-$$.txt` | Hardcoded Unix path prefix (use relativ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L2321` | `| `L831` | `Remove-Item -Force /tmp/spec-semantic-$$.txt` | Hardcoded Unix path ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L2322` | `| `L891` | `TMPERR_GATE=$(mktemp /tmp/spec-gate-XXXXXXXX)` | Hardcoded Unix path` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L2359` | `| `L686` | `Example: `$B snapshot -i -a -C -o /tmp/annotated.png`` | Hardcoded U` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-autoplan\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L286` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L299` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L698` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L759` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L760` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L922` | `- Discover design docs: `ls -t ~/.gstack/projects/$SLUG/*-design-*.md 2>/dev/nul` | Unix command (use PowerShell equivalent) |
| `L923` | `- Detect UI scope: grep the plan for view/rendering terms (component, screen, fo` | Unix text processing utilities (use PowerShell or Python) |
| `L926` | `- Detect DX scope: grep the plan for developer-facing terms (API, endpoint, REST` | Unix text processing utilities (use PowerShell or Python) |

---

### 📂 `skills\gstack-benchmark\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L410` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L411` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |

---

### 📂 `skills\gstack-browse\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L412` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L413` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L604` | `Example: `$B snapshot -i -a -C -o /tmp/annotated.png`` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L725` | `| `eval <file>` | Run JavaScript from file and return result as string (path mus` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-canary\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L276` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L289` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L666` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L667` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L706` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |

---

### 📂 `skills\gstack-careful\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L5` | `Safety guardrails for destructive commands. Warns before rm -rf, DROP TABLE,` | Unix force-remove command (use PowerShell equivalent) |
| `L35` | `> **Safety Advisory:** This skill includes safety checks that check bash command` | Unix force-remove command (use PowerShell equivalent) |
| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/data` | Recursive delete ` | Unix force-remove command (use PowerShell equivalent) |
| `L60` | `| `docker rm -f` / `docker system prune` | `docker system prune -a` | Container/` | Unix force-remove command (use PowerShell equivalent) |
| `L65` | `- `rm -rf node_modules` / `.next` / `dist` / `__pycache__` / `.cache` / `build` ` | Unix force-remove command (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/data` | Recursive delete ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-checkpoint\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L279` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L292` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L803` | `find "$CHECKPOINT_DIR" -maxdepth 1 -name "*.md" -type f | Out-Null | xargs ls -1` | Unix command (use PowerShell equivalent) |
| `L866` | `find "$CHECKPOINT_DIR" -maxdepth 1 -name "*.md" -type f | Out-Null | xargs ls -1` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-context-restore\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L343` | `_GBRAIN_VERSION_OK=$(gbrain --version  | grep -c '^gbrain ' || echo 0)` | Unix text processing utilities (use PowerShell or Python) |
| `L391` | `_BRAIN_LAST=$(cat "$_BRAIN_LAST_PULL_FILE"  || echo 0)` | Unix command (use PowerShell equivalent) |
| `L405` | `_GBRAIN_HOST=$(jq -r '.mcpServers.gbrain.url // empty' "$env:USERPROFILE\.claude` | Unix text processing utilities (use PowerShell or Python) |
| `L411` | `[ -f "$_GSTACK_HOME/.brain-last-push" ] ; _BRAIN_LAST_PUSH=$(cat "$_GSTACK_HOME/` | Unix command (use PowerShell equivalent) |
| `L463` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are cheaper and` | Unix text processing utilities (use PowerShell or Python) |
| `L463` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are cheaper and` | Unix command (use PowerShell equivalent) |
| `L490` | `Get-ChildItem "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md"  | xa` | Unix command (use PowerShell equivalent) |
| `L494` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl"  | grep '"event` | Unix text processing utilities (use PowerShell or Python) |
| `L496` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl"  | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L499` | `_LATEST_CP=$(Get-ChildItem "$_PROJ/checkpoints" -name "*.md" -type f  | xargs ls` | Unix command (use PowerShell equivalent) |
| `L761` | ``ls -1t` (filesystem mtime). Filenames are stable across file-system` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-context-save\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L342` | `_GBRAIN_VERSION_OK=$(gbrain --version  | grep -c '^gbrain ' || echo 0)` | Unix text processing utilities (use PowerShell or Python) |
| `L390` | `_BRAIN_LAST=$(cat "$_BRAIN_LAST_PULL_FILE"  || echo 0)` | Unix command (use PowerShell equivalent) |
| `L404` | `_GBRAIN_HOST=$(jq -r '.mcpServers.gbrain.url // empty' "$env:USERPROFILE\.claude` | Unix text processing utilities (use PowerShell or Python) |
| `L410` | `[ -f "$_GSTACK_HOME/.brain-last-push" ] ; _BRAIN_LAST_PUSH=$(cat "$_GSTACK_HOME/` | Unix command (use PowerShell equivalent) |
| `L462` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are cheaper and` | Unix text processing utilities (use PowerShell or Python) |
| `L462` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are cheaper and` | Unix command (use PowerShell equivalent) |
| `L489` | `Get-ChildItem "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md"  | xa` | Unix command (use PowerShell equivalent) |
| `L493` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl"  | grep '"event` | Unix text processing utilities (use PowerShell or Python) |
| `L495` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl"  | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L498` | `_LATEST_CP=$(Get-ChildItem "$_PROJ/checkpoints" -name "*.md" -type f  | xargs ls` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-cso\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L287` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L294` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L297` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L300` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L690` | `The bash blocks throughout this skill show WHAT patterns to search for, not HOW ` | Unix text processing utilities (use PowerShell or Python) |
| `L700` | `ls package.json tsconfig.json | Out-Null ; echo "STACK: Node/TypeScript"` | Unix command (use PowerShell equivalent) |
| `L701` | `ls Gemfile | Out-Null ; echo "STACK: Ruby"` | Unix command (use PowerShell equivalent) |
| `L702` | `ls requirements.txt pyproject.toml setup.py | Out-Null ; echo "STACK: Python"` | Unix command (use PowerShell equivalent) |
| `L703` | `ls go.mod | Out-Null ; echo "STACK: Go"` | Unix command (use PowerShell equivalent) |
| `L704` | `ls Cargo.toml | Out-Null ; echo "STACK: Rust"` | Unix command (use PowerShell equivalent) |
| `L705` | `ls pom.xml build.gradle | Out-Null ; echo "STACK: JVM"` | Unix command (use PowerShell equivalent) |
| `L706` | `ls composer.json | Out-Null ; echo "STACK: PHP"` | Unix command (use PowerShell equivalent) |
| `L707` | `find . -maxdepth 1 \( -name '*.csproj' -o -name '*.sln' \) | Out-Null | grep -q ` | Unix text processing utilities (use PowerShell or Python) |
| `L712` | `grep -q "next" package.json | Out-Null ; echo "FRAMEWORK: Next.js"` | Unix text processing utilities (use PowerShell or Python) |
| `L713` | `grep -q "express" package.json | Out-Null ; echo "FRAMEWORK: Express"` | Unix text processing utilities (use PowerShell or Python) |
| `L714` | `grep -q "fastify" package.json | Out-Null ; echo "FRAMEWORK: Fastify"` | Unix text processing utilities (use PowerShell or Python) |
| `L715` | `grep -q "hono" package.json | Out-Null ; echo "FRAMEWORK: Hono"` | Unix text processing utilities (use PowerShell or Python) |
| `L716` | `grep -q "django" requirements.txt pyproject.toml | Out-Null ; echo "FRAMEWORK: D` | Unix text processing utilities (use PowerShell or Python) |
| `L717` | `grep -q "fastapi" requirements.txt pyproject.toml | Out-Null ; echo "FRAMEWORK: ` | Unix text processing utilities (use PowerShell or Python) |
| `L718` | `grep -q "flask" requirements.txt pyproject.toml | Out-Null ; echo "FRAMEWORK: Fl` | Unix text processing utilities (use PowerShell or Python) |
| `L719` | `grep -q "rails" Gemfile | Out-Null ; echo "FRAMEWORK: Rails"` | Unix text processing utilities (use PowerShell or Python) |
| `L720` | `grep -q "gin-gonic" go.mod | Out-Null ; echo "FRAMEWORK: Gin"` | Unix text processing utilities (use PowerShell or Python) |
| `L721` | `grep -q "spring-boot" pom.xml build.gradle | Out-Null ; echo "FRAMEWORK: Spring ` | Unix text processing utilities (use PowerShell or Python) |
| `L722` | `grep -q "laravel" composer.json | Out-Null ; echo "FRAMEWORK: Laravel"` | Unix text processing utilities (use PowerShell or Python) |
| `L759` | `ls .env .env.* | Out-Null` | Unix command (use PowerShell equivalent) |
| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.example\|.sample\|.template` | Unix text processing utilities (use PowerShell or Python) |
| `L800` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.example\|.sample\|.template` | Unix command (use PowerShell equivalent) |
| `L801` | `grep -q "^\.env$\|^\.env\.\*" .gitignore | Out-Null ; echo ".env IS gitignored" ` | Unix text processing utilities (use PowerShell or Python) |
| `L807` | `[ -f "$f" ] ; grep -n "password:\|token:\|secret:\|api_key:" "$f" | grep -v '\${` | Unix text processing utilities (use PowerShell or Python) |
| `L896` | `**Key checks (beyond grep):**` | Unix text processing utilities (use PowerShell or Python) |
| `L914` | `ls -la .agents/skills/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L918` | `- `curl`, `wget`, `fetch`, `http`, `exfiltrat` (network exfiltration)` | Unix network tools (use PowerShell or Python) |
| `L930` | `**FP rules:** gstack's own skills are trusted (check if skill path resolves to a` | Unix network tools (use PowerShell or Python) |

---

### 📂 `skills\gstack-design-consultation\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L281` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L288` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L291` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L294` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L679` | `ls DESIGN.md design-system.md | Out-Null ; echo "NO_DESIGN_FILE"` | Unix command (use PowerShell equivalent) |
| `L688` | `cat README.md | Out-Null | head -50` | Unix command (use PowerShell equivalent) |
| `L689` | `cat package.json | Out-Null | head -20` | Unix command (use PowerShell equivalent) |
| `L690` | `ls src/ app/ pages/ components/ | Out-Null | head -30` | Unix command (use PowerShell equivalent) |
| `L698` | `ls ~/.gstack/projects/$SLUG/*office-hours* | Out-Null | head -5` | Unix command (use PowerShell equivalent) |
| `L699` | `ls .context/*office-hours* .context/attachments/*office-hours* | Out-Null | head` | Unix command (use PowerShell equivalent) |
| `L731` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L732` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L1045` | `cat "$_DESIGN_DIR/feedback.json"` | Unix command (use PowerShell equivalent) |
| `L1048` | `cat "$_DESIGN_DIR/feedback-pending.json"` | Unix command (use PowerShell equivalent) |
| `L1077` | ``curl -s -X POST http://127.0.0.1:PORT/api/reload -H 'Content-Type: application/` | Unix network tools (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L788` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design artifacts are U` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-design-html\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L286` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L299` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L811` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L812` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L836` | `_CEO=$(ls -t ~/.gstack/projects/$SLUG/ceo-plans/*.md | Out-Null | head -1)` | Unix command (use PowerShell equivalent) |
| `L842` | `_APPROVED=$(ls -t ~/.gstack/projects/$SLUG/designs/*/approved.json | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/variant-*.png | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L854` | `_FINALIZED=$(ls -t ~/.gstack/projects/$SLUG/designs/*/finalized.html | Out-Null ` | Unix command (use PowerShell equivalent) |
| `L979` | `[ -f package.json ] ; cat package.json | grep -o '"react"\|"svelte"\|"vue"\|"@an` | Unix text processing utilities (use PowerShell or Python) |
| `L979` | `[ -f package.json ] ; cat package.json | grep -o '"react"\|"svelte"\|"vue"\|"@an` | Unix command (use PowerShell equivalent) |
| `L1226` | `_PORT=$(lsof -i -P -n | grep "$_SERVER_PID" | grep LISTEN | awk '{print $9}' | c` | Unix text processing utilities (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L700` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design artifacts are U` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L848` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/variant-*.png | Out-Null | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-design-review\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L281` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L288` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L291` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L294` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L689` | `$B status | Out-Null | grep -q "Mode: cdp" ; echo "CDP_MODE=true" ; echo "CDP_MO` | Unix text processing utilities (use PowerShell or Python) |
| `L740` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L741` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L770` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | Out-Null ; echo "FRAMEWORK:rails"` | Unix text processing utilities (use PowerShell or Python) |
| `L771` | `[ -f package.json ] ; grep -q '"next"' package.json | Out-Null ; echo "FRAMEWORK` | Unix text processing utilities (use PowerShell or Python) |
| `L773` | `ls jest.config.* vitest.config.* playwright.config.* .rspec pytest.ini pyproject` | Unix command (use PowerShell equivalent) |
| `L774` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L859` | `ls -d .github/ | Out-Null ; echo "CI:github"` | Unix command (use PowerShell equivalent) |
| `L860` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | Out-Null` | Unix command (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L951` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design artifacts are U` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-design-shotgun\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L278` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L291` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L829` | `cat DESIGN.md | Out-Null | head -80 ; echo "NO_DESIGN_MD"` | Unix command (use PowerShell equivalent) |
| `L833` | `ls src/ app/ pages/ components/ | Out-Null | head -30` | Unix command (use PowerShell equivalent) |
| `L838` | `ls ~/.gstack/projects/$SLUG/*office-hours* | Out-Null | head -5` | Unix command (use PowerShell equivalent) |
| `L848` | `curl -s -o $null -w "%{http_code}" http://localhost:3000 | Out-Null ; echo "NO_L` | Unix network tools (use PowerShell or Python) |
| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` | Unix command (use PowerShell equivalent) |
| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' | sed 's/,$//` | Unix text processing utilities (use PowerShell or Python) |
| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' | sed 's/,$//` | Unix command (use PowerShell equivalent) |
| `L1043` | `cat "$_DESIGN_DIR/feedback.json"` | Unix command (use PowerShell equivalent) |
| `L1046` | `cat "$_DESIGN_DIR/feedback-pending.json"` | Unix command (use PowerShell equivalent) |
| `L1075` | ``curl -s -X POST http://127.0.0.1:PORT/api/reload -H 'Content-Type: application/` | Unix network tools (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L691` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design artifacts are U` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L954` | `Final location: {_DESIGN_DIR absolute path}/variant-{letter}.png` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L961` | `4. Copy: cp $env:TEMP\variant-{letter}.png {_DESIGN_DIR}/variant-{letter}.png` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L962` | `5. Quality check: {$D path} check --image {_DESIGN_DIR}/variant-{letter}.png --b` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L964` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L976` | `**Why /tmp/ then cp?** In observed sessions, `$D generate --output ~/.gstack/...` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L977` | `failed with "The operation was aborted" while `--output /tmp/...` succeeded. Thi` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L978` | `a sandbox restriction. Always generate to `/tmp/` first, then `cp`.` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L998` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' | sed 's/,$//` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1140` | `1. **Never save to `.context/`, `docs/designs/`, or `/tmp/`.** All design artifa` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-devex-review\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L285` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L292` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L295` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L298` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L697` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L732` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L733` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L770` | `| 1 | **Usable** | Simple to install, set up, use. Intuitive APIs. Fast feedback` | Unix network tools (use PowerShell or Python) |
| `L849` | `$GSTACK_ROOT/bin/gstack-review-read | Out-Null | grep plan-devex-review ; echo "` | Unix text processing utilities (use PowerShell or Python) |
| `L903` | `- Deprecation warnings in code (grep for deprecated/obsolete)` | Unix text processing utilities (use PowerShell or Python) |

---

### 📂 `skills\gstack-document-generate\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L345` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | grep -c '^gbrain ' || echo 0` | Unix text processing utilities (use PowerShell or Python) |
| `L407` | `_GBRAIN_HOST=$(jq -r '.mcpServers.gbrain.url // empty' "$HOME/.claude.json" 2>/d` | Unix text processing utilities (use PowerShell or Python) |
| `L465` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, grep). The dediGet-Conten` | Unix text processing utilities (use PowerShell or Python) |
| `L492` | `Get-ChildItem -Recurse "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.` | Unix command (use PowerShell equivalent) |
| `L496` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>/dev/null | g` | Unix text processing utilities (use PowerShell or Python) |
| `L498` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>/dev` | Unix text processing utilities (use PowerShell or Python) |
| `L501` | `_LATEST_CP=$(Get-ChildItem -Recurse "$_PROJ/checkpoints" -name "*.md" -type f 2>` | Unix command (use PowerShell equivalent) |
| `L668` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L871` | `- Use ASCII diagrams for architecture. They're grep-able, diff-friendly, and ren` | Unix text processing utilities (use PowerShell or Python) |
| `L1036` | `git diff --cached --no-color | grep '^+' | sed 's/^+//' | \` | Unix text processing utilities (use PowerShell or Python) |

---

### 📂 `skills\gstack-document-release\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L278` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L291` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L672` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L939` | `git commit -m "$(cat <<'EOF'` | Unix command (use PowerShell equivalent) |
| `L984` | `glab mr update -d "$(cat <<'MRBODY'` | Unix command (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L982` | `Read the contents of `/tmp/gstack-pr-body-$$.md` using the Read tool, then pass ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-freeze\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L95` | `- This prevents accidental edits, not a security boundary — Bash commands like `` | Unix text processing utilities (use PowerShell or Python) |

---

### 📂 `skills\gstack-guard\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L6` | `Combines /gs:careful (warns before rm -rf, DROP TABLE, force-push, etc.) with` | Unix force-remove command (use PowerShell equivalent) |
| `L46` | `> **Safety Advisory:** This skill includes safety checks that check bash command` | Unix force-remove command (use PowerShell equivalent) |
| `L89` | `- "1. **Destructive command warnings** — rm -rf, DROP TABLE, force-push, etc. wi` | Unix force-remove command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-health\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L278` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L291` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L675` | `ls eslint.config.* .eslintrc.* .eslintrc | Out-Null | head -1 | xargs -I{} echo ` | Unix command (use PowerShell equivalent) |
| `L676` | `[ -f .pylintrc ] ; [ -f pyproject.toml ] ; grep -q "pylint\|ruff" pyproject.toml` | Unix text processing utilities (use PowerShell or Python) |
| `L679` | `[ -f package.json ] ; grep -q '"test"' package.json | Out-Null ; echo "TEST: $(n` | Unix text processing utilities (use PowerShell or Python) |
| `L680` | `[ -f pyproject.toml ] ; grep -q "pytest" pyproject.toml | Out-Null ; echo "TEST:` | Unix text processing utilities (use PowerShell or Python) |
| `L686` | `[ -f package.json ] ; grep -q '"knip"' package.json | Out-Null ; echo "DEADCODE:` | Unix text processing utilities (use PowerShell or Python) |
| `L689` | `command -v shellcheck | Out-Null 2>&1 ; ls *.sh scripts/*.sh bin/*.sh | Out-Null` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-investigate\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L297` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L304` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L307` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L310` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-land-and-deploy\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L276` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L289` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L684` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L685` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L724` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L825` | `SAVED_HASH=$(cat ~/.gstack/projects/$SLUG/land-deploy-confirmed | Out-Null)` | Unix command (use PowerShell equivalent) |
| `L826` | `CURRENT_HASH=$(sed -n '/## Deploy Configuration/,/^## /p' CLAUDE.md | Out-Null |` | Unix text processing utilities (use PowerShell or Python) |
| `L828` | `WORKFLOW_HASH=$(find .github/workflows -maxdepth 1 \( -name '*deploy*' -o -name ` | Unix command (use PowerShell equivalent) |
| `L865` | `DEPLOY_CONFIG=$(grep -A 20 "## Deploy Configuration" CLAUDE.md | Out-Null ; echo` | Unix text processing utilities (use PowerShell or Python) |
| `L870` | `PROD_URL=$(echo "$DEPLOY_CONFIG" | grep -i "production.*url" | head -1 | sed 's/` | Unix text processing utilities (use PowerShell or Python) |
| `L871` | `PLATFORM=$(echo "$DEPLOY_CONFIG" | grep -i "platform" | head -1 | sed 's/.*: *//` | Unix text processing utilities (use PowerShell or Python) |
| `L886` | `[ -f "$f" ] ; grep -qiE "deploy|release|production|cd" "$f" | Out-Null ; echo "D` | Unix text processing utilities (use PowerShell or Python) |
| `L887` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Out-Null ; echo "STAGING_WORKFLOW:$f"` | Unix text processing utilities (use PowerShell or Python) |
| `L932` | `║  ├─ curl prod URL:      ✓ PASS (200 OK) / ⚠ UNREACHABLE   ║` | Unix network tools (use PowerShell or Python) |
| `L953` | `failed at Step 1). If `curl` fails, note "I couldn't reach that URL — might be a` | Unix network tools (use PowerShell or Python) |
| `L966` | `grep -i "staging" CLAUDE.md | Out-Null | head -3` | Unix text processing utilities (use PowerShell or Python) |
| `L972` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Out-Null ; echo "STAGING_WORKFLOW:$f"` | Unix text processing utilities (use PowerShell or Python) |
| `L1020` | `CURRENT_HASH=$(sed -n '/## Deploy Configuration/,/^## /p' CLAUDE.md | Out-Null |` | Unix text processing utilities (use PowerShell or Python) |
| `L1021` | `WORKFLOW_HASH=$(find .github/workflows -maxdepth 1 \( -name '*deploy*' -o -name ` | Unix command (use PowerShell equivalent) |
| `L1130` | `cat $GSTACK_ROOT/review/checklist.md | Out-Null ; echo "Checklist not found"` | Unix command (use PowerShell equivalent) |
| `L1164` | `ls -t ~/.gstack-dev/evals/*-e2e-*-$(date +%Y-%m-%d)*.json | Out-Null | head -20` | Unix command (use PowerShell equivalent) |
| `L1180` | `ls -t ~/.gstack-dev/evals/*-llm-judge-*-$(date +%Y-%m-%d)*.json | Out-Null | hea` | Unix command (use PowerShell equivalent) |
| `L1210` | `git log --oneline --all-match --grep="docs:" $(gh pr view --json baseRefName -q ` | Unix text processing utilities (use PowerShell or Python) |
| `L1365` | `DEPLOY_CONFIG=$(grep -A 20 "## Deploy Configuration" CLAUDE.md | Out-Null ; echo` | Unix text processing utilities (use PowerShell or Python) |
| `L1370` | `PROD_URL=$(echo "$DEPLOY_CONFIG" | grep -i "production.*url" | head -1 | sed 's/` | Unix text processing utilities (use PowerShell or Python) |
| `L1371` | `PLATFORM=$(echo "$DEPLOY_CONFIG" | grep -i "platform" | head -1 | sed 's/.*: *//` | Unix text processing utilities (use PowerShell or Python) |
| `L1386` | `[ -f "$f" ] ; grep -qiE "deploy|release|production|cd" "$f" | Out-Null ; echo "D` | Unix text processing utilities (use PowerShell or Python) |
| `L1387` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Out-Null ; echo "STAGING_WORKFLOW:$f"` | Unix text processing utilities (use PowerShell or Python) |
| `L1486` | `curl -sf {production-url} -o $null -w "%{http_code}" | Out-Null` | Unix network tools (use PowerShell or Python) |

---

### 📂 `skills\gstack-learn\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L278` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L285` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L288` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L291` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L768` | `cat "$LEARN_FILE" | bun -e "` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-maintainer-auditor\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L49` | `- **Tự động đề xuất đoạn mã sửa đổi** bằng PowerShell thuần túy Windows (Ví dụ: ` | Unix force-remove command (use PowerShell equivalent) |
| `L49` | `- **Tự động đề xuất đoạn mã sửa đổi** bằng PowerShell thuần túy Windows (Ví dụ: ` | Unix nested directory creation (use PowerShell equivalent) |

---

### 📂 `skills\gstack-make-pdf\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L264` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | grep -c '^gbrain ' || echo 0` | Unix text processing utilities (use PowerShell or Python) |
| `L326` | `_GBRAIN_HOST=$(jq -r '.mcpServers.gbrain.url // empty' "$HOME/.claude.json" 2>/d` | Unix text processing utilities (use PowerShell or Python) |
| `L384` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, grep). The dediGet-Conten` | Unix text processing utilities (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L473` | `$P generate letter.md                 # writes /tmp/letter.pdf` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L573` | `stdout: /tmp/letter.pdf          ← just the path, one line` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L576` | `Done in 1.5s. 43 words · 22KB · /tmp/letter.pdf` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-office-hours\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L286` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L299` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L694` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L695` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L731` | `ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-Null` | Unix command (use PowerShell equivalent) |
| `L986` | `Extract 3-5 significant keywords from the user's problem statement and grep acro` | Unix text processing utilities (use PowerShell or Python) |
| `L989` | `grep -li "<keyword1>\|<keyword2>\|<keyword3>" ~/.gstack/projects/$SLUG/*-design-` | Unix text processing utilities (use PowerShell or Python) |
| `L1159` | `4. POST the new HTML to the running server via `curl -X POST http://localhost:PO` | Unix network tools (use PowerShell or Python) |
| `L1253` | `Use a 5-minute timeout (`timeout: 300000`). After completion: `cat "$TMPERR_SKET` | Unix force-remove command (use PowerShell equivalent) |
| `L1253` | `Use a 5-minute timeout (`timeout: 300000`). After completion: `cat "$TMPERR_SKET` | Unix command (use PowerShell equivalent) |
| `L1321` | `PRIOR=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head -` | Unix command (use PowerShell equivalent) |
| `L1532` | `SESSION_TIER=$(echo "$PROFILE" | grep "^TIER:" | awk '{print $2}')` | Unix text processing utilities (use PowerShell or Python) |
| `L1533` | `SESSION_COUNT=$(echo "$PROFILE" | grep "^SESSION_COUNT:" | awk '{print $2}')` | Unix text processing utilities (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L1228` | `The screenshot file at `/tmp/gstack-sketch.png` can be referenced by downstream ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-open-gstack-browser\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L276` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L289` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L689` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L690` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L711` | `_OLD_PID=$(cat "$(git rev-parse --show-toplevel)/.gstack/browse.json" | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L711` | `_OLD_PID=$(cat "$(git rev-parse --show-toplevel)/.gstack/browse.json" | Out-Null` | Unix command (use PowerShell equivalent) |
| `L756` | `cat "$(git rev-parse --show-toplevel | Out-Null)/.gstack/browse.json" | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L756` | `cat "$(git rev-parse --show-toplevel | Out-Null)/.gstack/browse.json" | Out-Null` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-pair-agent\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L280` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L287` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L290` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L293` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L711` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L712` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L908` | ``exec curl` syntax which OpenClaw understands natively. When using `--local open` | Unix network tools (use PowerShell or Python) |
| `L915` | `curl commands work directly. When using `--local codex`, credentials are written` | Unix network tools (use PowerShell or Python) |

---

### 📂 `skills\gstack-plan-ceo-review\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L282` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L289` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L292` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L295` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L694` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L779` | `grep -r "TODO\|FIXME\|HACK\|XXX" -l --exclude-dir=node_modules --exclude-dir=ven` | Unix text processing utilities (use PowerShell or Python) |
| `L789` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L790` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L798` | `HANDOFF=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-ceo-handoff-*.md | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L860` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L861` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-N` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-plan-design-review\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L279` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L292` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L691` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L980` | `- `mkdir -p ~/.gstack/projects/$SLUG/designs/...`` | Unix nested directory creation (use PowerShell equivalent) |
| `L1057` | `cat "$_DESIGN_DIR/feedback.json"` | Unix command (use PowerShell equivalent) |
| `L1060` | `cat "$_DESIGN_DIR/feedback-pending.json"` | Unix command (use PowerShell equivalent) |
| `L1089` | ``curl -s -X POST http://127.0.0.1:PORT/api/reload -H 'Content-Type: application/` | Unix network tools (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L934` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design artifacts are U` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-plan-devex-review\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L289` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L296` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L299` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L302` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L701` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L752` | `| 1 | **Usable** | Simple to install, set up, use. Intuitive APIs. Fast feedback` | Unix network tools (use PowerShell or Python) |
| `L832` | `- Getting started guides (grep README for "Getting Started", "Quick Start", "Ins` | Unix text processing utilities (use PowerShell or Python) |
| `L833` | `- CLI help text (grep for `--help`, `usage:`, `commands:`)` | Unix text processing utilities (use PowerShell or Python) |
| `L834` | `- Error message patterns (grep for `throw new Error`, `console.error`, error cla` | Unix text processing utilities (use PowerShell or Python) |
| `L842` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L843` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L902` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L903` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L1264` | `$GSTACK_ROOT/bin/gstack-review-read | Out-Null | grep plan-devex-review ; echo "` | Unix text processing utilities (use PowerShell or Python) |

---

### 📂 `skills\gstack-plan-eng-review\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L284` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L291` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L294` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L297` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L720` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L721` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L775` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L776` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L896` | `ls jest.config.* vitest.config.* playwright.config.* cypress.config.* .rspec pyt` | Unix command (use PowerShell equivalent) |
| `L897` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-plan-tune\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L289` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L296` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L299` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L302` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-qa-only\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L279` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L292` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L707` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L708` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L748` | `ls -t ~/.gstack/projects/$SLUG/*-test-plan-*.md | Out-Null | head -1` | Unix command (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L676` | `| Output dir | `.gstack/qa-reports/` | `Output to /tmp/qa` |` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-qa\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L286` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L293` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L296` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L299` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L698` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L738` | `$B status | Out-Null | grep -q "Mode: cdp" ; echo "CDP_MODE=true" ; echo "CDP_MO` | Unix text processing utilities (use PowerShell or Python) |
| `L785` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L786` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L815` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | Out-Null ; echo "FRAMEWORK:rails"` | Unix text processing utilities (use PowerShell or Python) |
| `L816` | `[ -f package.json ] ; grep -q '"next"' package.json | Out-Null ; echo "FRAMEWORK` | Unix text processing utilities (use PowerShell or Python) |
| `L818` | `ls jest.config.* vitest.config.* playwright.config.* .rspec pytest.ini pyproject` | Unix command (use PowerShell equivalent) |
| `L819` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L904` | `ls -d .github/ | Out-Null ; echo "CI:github"` | Unix command (use PowerShell equivalent) |
| `L905` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | Out-Null` | Unix command (use PowerShell equivalent) |
| `L981` | `ls -t ~/.gstack/projects/$SLUG/*-test-plan-*.md | Out-Null | head -1` | Unix command (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L725` | `| Output dir | `.gstack/qa-reports/` | `Output to /tmp/qa` |` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-retro\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L276` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L283` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L286` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L289` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L670` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L770` | `git log origin/<default> --since="<window>" --format="" --name-only | grep -v '^` | Unix text processing utilities (use PowerShell or Python) |
| `L773` | `git log origin/<default> --since="<window>" --format="%s" | grep -oE '[#!][0-9]+` | Unix text processing utilities (use PowerShell or Python) |
| `L782` | `cat ~/.gstack/greptile-history.md | Out-Null ; true` | Unix command (use PowerShell equivalent) |
| `L785` | `cat TODOS.md | Out-Null ; true` | Unix command (use PowerShell equivalent) |
| `L788` | `find . -name '*.test.*' -o -name '*.spec.*' -o -name '*_test.*' -o -name '*_spec` | Unix text processing utilities (use PowerShell or Python) |
| `L791` | `git log origin/<default> --since="<window>" --oneline --grep="test(qa):" --grep=` | Unix text processing utilities (use PowerShell or Python) |
| `L794` | `cat ~/.gstack/analytics/skill-usage.jsonl | Out-Null ; true` | Unix command (use PowerShell equivalent) |
| `L797` | `git log origin/<default> --since="<window>" --format="" --name-only | grep -E '\` | Unix text processing utilities (use PowerShell or Python) |
| `L1029` | `ls -t .context/retros/*.json | Out-Null` | Unix command (use PowerShell equivalent) |
| `L1058` | `existing=$(ls .context/retros/${today}-*.json | Out-Null | wc -l | tr -d ' ')` | Unix command (use PowerShell equivalent) |
| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Null | grep '"skill":"ship"' ` | Unix text processing utilities (use PowerShell or Python) |
| `L1181` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Null | grep '"skill":"ship"' ` | Unix command (use PowerShell equivalent) |
| `L1306` | `git -C <path> log origin/$DEFAULT --since="<start_date>T00:00:00" --format="%s" ` | Unix text processing utilities (use PowerShell or Python) |
| `L1482` | `ls -t ~/.gstack/retros/global-*.json | Out-Null | head -5` | Unix command (use PowerShell equivalent) |
| `L1501` | `existing=$(ls ~/.gstack/retros/global-${today}-*.json | Out-Null | wc -l | tr -d` | Unix command (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L1277` | `Read the stderr output from `/tmp/gstack-discover-stderr` for diagnostic info. P` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-review\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L280` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L287` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L290` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L293` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L692` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L764` | `_PLAN_SLUG=$(git remote get-url origin | Out-Null | sed 's|.*[:/]\([^/]*/[^/]*\)` | Unix text processing utilities (use PowerShell or Python) |
| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" | Out-Null | ` | Unix text processing utilities (use PowerShell or Python) |
| `L769` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$REPO` | Unix text processing utilities (use PowerShell or Python) |
| `L770` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$REPO` | Unix command (use PowerShell equivalent) |
| `L771` | `[ -z "$PLAN" ] ; PLAN=$(find "$PLAN_DIR" -name '*.md' -mmin -1440 -maxdepth 1 | ` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-scrape\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L334` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper and clearer.` | Unix text processing utilities (use PowerShell or Python) |
| `L334` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper and clearer.` | Unix command (use PowerShell equivalent) |
| `L363` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L370` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L373` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L376` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-setup-browser-cookies\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L389` | `$B status | Out-Null | grep -q "Mode: cdp" ; echo "CDP_MODE=true" ; echo "CDP_MO` | Unix text processing utilities (use PowerShell or Python) |
| `L427` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L428` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |

---

### 📂 `skills\gstack-setup-deploy\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L279` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L286` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L289` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L292` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L662` | `grep -A 20 "## Deploy Configuration" CLAUDE.md | Out-Null ; echo "NO_CONFIG"` | Unix text processing utilities (use PowerShell or Python) |
| `L681` | `[ -f fly.toml ] ; echo "PLATFORM:fly" ; cat fly.toml` | Unix command (use PowerShell equivalent) |
| `L682` | `[ -f render.yaml ] ; echo "PLATFORM:render" ; cat render.yaml` | Unix command (use PowerShell equivalent) |
| `L684` | `[ -f netlify.toml ] ; echo "PLATFORM:netlify" ; cat netlify.toml` | Unix command (use PowerShell equivalent) |
| `L690` | `[ -f "$f" ] ; grep -qiE "deploy|release|production|staging|cd" "$f" | Out-Null ;` | Unix text processing utilities (use PowerShell or Python) |
| `L694` | `[ -f package.json ] ; grep -q '"bin"' package.json | Out-Null ; echo "PROJECT_TY` | Unix text processing utilities (use PowerShell or Python) |
| `L695` | `find . -maxdepth 1 -name '*.gemspec' | Out-Null | grep -q . ; echo "PROJECT_TYPE` | Unix text processing utilities (use PowerShell or Python) |
| `L706` | `1. Extract app name: `grep -m1 "^app" fly.toml | sed 's/app = "\(.*\)"/\1/'`` | Unix text processing utilities (use PowerShell or Python) |
| `L734` | `2. If installed: `vercel ls --prod 2>/dev/null | head -3`` | Unix command (use PowerShell equivalent) |
| `L807` | `curl -sf "{health-check-url}" -o $null -w "%{http_code}" | Out-Null ; echo "UNRE` | Unix network tools (use PowerShell or Python) |

---

### 📂 `skills\gstack-ship\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L282` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L289` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L292` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L295` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L694` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L829` | `git diff origin/<base> --name-only | grep -E '(cmd/.*/main\.go|bin/|Cargo\.toml|` | Unix text processing utilities (use PowerShell or Python) |
| `L834` | `ls .github/workflows/ | Out-Null | grep -iE 'release|publish|dist'` | Unix text processing utilities (use PowerShell or Python) |
| `L834` | `ls .github/workflows/ | Out-Null | grep -iE 'release|publish|dist'` | Unix command (use PowerShell equivalent) |
| `L835` | `grep -qE 'release|publish|deploy' .gitlab-ci.yml | Out-Null ; echo "GITLAB_CI_RE` | Unix text processing utilities (use PowerShell or Python) |
| `L881` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | Out-Null ; echo "FRAMEWORK:rails"` | Unix text processing utilities (use PowerShell or Python) |
| `L882` | `[ -f package.json ] ; grep -q '"next"' package.json | Out-Null ; echo "FRAMEWORK` | Unix text processing utilities (use PowerShell or Python) |
| `L884` | `ls jest.config.* vitest.config.* playwright.config.* .rspec pytest.ini pyproject` | Unix command (use PowerShell equivalent) |
| `L885` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L970` | `ls -d .github/ | Out-Null ; echo "CI:github"` | Unix command (use PowerShell equivalent) |
| `L971` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | Out-Null` | Unix command (use PowerShell equivalent) |
| `L1176` | `grep -l "changed_file_basename" test/evals/*_eval_runner.rb` | Unix text processing utilities (use PowerShell or Python) |
| `L1183` | `- Changes to `config/system_prompts/*.txt` — grep eval runners for the prompt fi` | Unix text processing utilities (use PowerShell or Python) |
| `L1238` | `ls jest.config.* vitest.config.* playwright.config.* cypress.config.* .rspec pyt` | Unix command (use PowerShell equivalent) |
| `L1239` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L1248` | `find . -name '*.test.*' -o -name '*.spec.*' -o -name '*_test.*' -o -name '*_spec` | Unix text processing utilities (use PowerShell or Python) |
| `L1408` | `find . -name '*.test.*' -o -name '*.spec.*' -o -name '*_test.*' -o -name '*_spec` | Unix text processing utilities (use PowerShell or Python) |
| `L1511` | `_PLAN_SLUG=$(git remote get-url origin | Out-Null | sed 's|.*[:/]\([^/]*/[^/]*\)` | Unix text processing utilities (use PowerShell or Python) |
| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" | Out-Null | ` | Unix text processing utilities (use PowerShell or Python) |
| `L1516` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$REPO` | Unix text processing utilities (use PowerShell or Python) |
| `L1517` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$REPO` | Unix command (use PowerShell equivalent) |
| `L1518` | `[ -z "$PLAN" ] ; PLAN=$(find "$PLAN_DIR" -name '*.md' -mmin -1440 -maxdepth 1 | ` | Unix command (use PowerShell equivalent) |
| `L1647` | `curl -s -o $null -w '%{http_code}' http://localhost:3000 | Out-Null ; \` | Unix network tools (use PowerShell or Python) |
| `L1648` | `curl -s -o $null -w '%{http_code}' http://localhost:8080 | Out-Null ; \` | Unix network tools (use PowerShell or Python) |
| `L1649` | `curl -s -o $null -w '%{http_code}' http://localhost:5173 | Out-Null ; \` | Unix network tools (use PowerShell or Python) |
| `L1650` | `curl -s -o $null -w '%{http_code}' http://localhost:4000 | Out-Null ; echo "NO_S` | Unix network tools (use PowerShell or Python) |
| `L1660` | `cat ${CLAUDE_SKILL_DIR}/../qa-only/SKILL.md` | Unix command (use PowerShell equivalent) |
| `L1964` | `CURRENT_VERSION=$(cat VERSION | Out-Null | tr -d '\r\n[:space:]' ; echo "0.0.0.0` | Unix command (use PowerShell equivalent) |
| `L2029` | `if ! printf '%s' "$NEW_VERSION" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$'; t` | Unix text processing utilities (use PowerShell or Python) |
| `L2055` | `REPAIR_VERSION=$(cat VERSION | tr -d '\r\n[:space:]')` | Unix command (use PowerShell equivalent) |
| `L2056` | `if ! printf '%s' "$REPAIR_VERSION" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$'` | Unix text processing utilities (use PowerShell or Python) |
| `L2203` | `git commit -m "$(cat <<'EOF'` | Unix command (use PowerShell equivalent) |
| `L2366` | `gh pr create --base <base> --title "<type>: <summary>" --body "$(cat <<'EOF'` | Unix command (use PowerShell equivalent) |
| `L2375` | `glab mr create -b <base> -t "<type>: <summary>" -d "$(cat <<'EOF'` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-skillify\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L358` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper and clearer.` | Unix text processing utilities (use PowerShell or Python) |
| `L358` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper and clearer.` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-spec\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L340` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | grep -c '^gbrain ' || echo 0` | Unix text processing utilities (use PowerShell or Python) |
| `L402` | `_GBRAIN_HOST=$(jq -r '.mcpServers.gbrain.url // empty' "$HOME/.claude.json" 2>/d` | Unix text processing utilities (use PowerShell or Python) |
| `L460` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, grep). The dediGet-Conten` | Unix text processing utilities (use PowerShell or Python) |
| `L487` | `Get-ChildItem -Recurse "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.` | Unix command (use PowerShell equivalent) |
| `L491` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>/dev/null | g` | Unix text processing utilities (use PowerShell or Python) |
| `L493` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>/dev` | Unix text processing utilities (use PowerShell or Python) |
| `L496` | `_LATEST_CP=$(Get-ChildItem -Recurse "$_PROJ/checkpoints" -name "*.md" -type f 2>` | Unix command (use PowerShell equivalent) |
| `L852` | `[ -z "$REDACT_VIS" ] && REDACT_VIS=$(glab repo view -F json 2>/dev/null | grep -` | Unix text processing utilities (use PowerShell or Python) |
| `L1264` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | grep -c '^gbrain ' || echo 0` | Unix text processing utilities (use PowerShell or Python) |
| `L1326` | `_GBRAIN_HOST=$(jq -r '.mcpServers.gbrain.url // empty' "$HOME/.claude.json" 2>/d` | Unix text processing utilities (use PowerShell or Python) |
| `L1384` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, grep). The dediGet-Conten` | Unix text processing utilities (use PowerShell or Python) |
| `L1411` | `Get-ChildItem -Recurse "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.` | Unix command (use PowerShell equivalent) |
| `L1415` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>/dev/null | g` | Unix text processing utilities (use PowerShell or Python) |
| `L1417` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>/dev` | Unix text processing utilities (use PowerShell or Python) |
| `L1420` | `_LATEST_CP=$(Get-ChildItem -Recurse "$_PROJ/checkpoints" -name "*.md" -type f 2>` | Unix command (use PowerShell equivalent) |
| `L1611` | `ISSUE_NUMBER=$(echo "$ISSUE_URL" | sed -E 's|.*/issues/([0-9]+)$|\1|')` | Unix text processing utilities (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L827` | `printf '%s' "<the final draft body>" > /tmp/spec-semantic-$$.txt` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L830` | `/tmp/spec-semantic-$$.txt` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L831` | `Remove-Item -Force /tmp/spec-semantic-$$.txt` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L891` | `TMPERR_GATE=$(mktemp /tmp/spec-gate-XXXXXXXX)` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack-unfreeze\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L42` | `PREV=$(cat "$STATE_DIR/freeze-dir.txt")` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack-upgrade\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L71` | `_SNOOZED_VER=$(awk '{print $1}' "$_SNOOZE_FILE")` | Unix text processing utilities (use PowerShell or Python) |
| `L73` | `_CUR_LEVEL=$(awk '{print $2}' "$_SNOOZE_FILE")` | Unix text processing utilities (use PowerShell or Python) |
| `L127` | `OLD_VERSION=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; echo "unknown")` | Unix command (use PowerShell equivalent) |
| `L179` | `if ! grep -qF '.agents/skills/gstack/' .gitignore | Out-Null; then` | Unix text processing utilities (use PowerShell or Python) |
| `L214` | `m_ver="$(basename "$migration" .sh | sed 's/^v//')"` | Unix text processing utilities (use PowerShell or Python) |
| `L283` | `PRIMARY_VER=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; echo "unknown")` | Unix command (use PowerShell equivalent) |
| `L284` | `LOCAL_VER=$(cat "$LOCAL_GSTACK/VERSION" | Out-Null ; echo "unknown")` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L446` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L447` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L470` | `> Set them before running: `export TEST_EMAIL="..." TEST_PASSWORD="..."`` | Unix environment variable export (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths

| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L686` | `Example: `$B snapshot -i -a -C -o /tmp/annotated.png`` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L783` | `| `eval <file>` | Run JavaScript from file and return result as string (path mus` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---

### 📂 `skills\gstack\gstack-upgrade\SKILL.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L64` | `_SNOOZED_VER=$(awk '{print $1}' "$_SNOOZE_FILE")` | Unix text processing utilities (use PowerShell or Python) |
| `L66` | `_CUR_LEVEL=$(awk '{print $2}' "$_SNOOZE_FILE")` | Unix text processing utilities (use PowerShell or Python) |
| `L120` | `OLD_VERSION=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; echo "unknown")` | Unix command (use PowerShell equivalent) |
| `L172` | `if ! grep -qF '.agents/skills/gstack/' .gitignore | Out-Null; then` | Unix text processing utilities (use PowerShell or Python) |
| `L207` | `m_ver="$(basename "$migration" .sh | sed 's/^v//')"` | Unix text processing utilities (use PowerShell or Python) |
| `L276` | `PRIMARY_VER=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; echo "unknown")` | Unix command (use PowerShell equivalent) |
| `L277` | `LOCAL_VER=$(cat "$LOCAL_GSTACK/VERSION" | Out-Null ; echo "unknown")` | Unix command (use PowerShell equivalent) |

---

### 📂 `skills\gstack\review\checklist.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L63` | `- **Trace it through every consumer.** Read (don't just grep — READ) each file t` | Unix text processing utilities (use PowerShell or Python) |
| `L66` | `To do this: use Grep to find all references to the sibling values (e.g., grep fo` | Unix text processing utilities (use PowerShell or Python) |

---

### 📂 `skills\gstack\review\design-checklist.md`

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L25` | `- **[HIGH]** — Reliably detectable via grep/pattern match. Definitive findings.` | Unix text processing utilities (use PowerShell or Python) |

---

### 📂 `tests\test_context_port.ps1`

- ⚠️ **PowerShell Line Ending Warning:** Uses `LF` format. For native Windows PowerShell compatibility, saving with `CRLF` endings is recommended.

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L6` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detected in $s" }` | Unix nested directory creation (use PowerShell equivalent) |

---

### 📂 `tests\test_group1_core_port.ps1`

- ⚠️ **PowerShell Line Ending Warning:** Uses `LF` format. For native Windows PowerShell compatibility, saving with `CRLF` endings is recommended.

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L9` | `if ($content -like $mkdir_pattern) { throw "FAIL: Unix mkdir -p detected in $s" ` | Unix nested directory creation (use PowerShell equivalent) |

---

### 📂 `tests\test_group2_infra_port.ps1`

- ⚠️ **PowerShell Line Ending Warning:** Uses `LF` format. For native Windows PowerShell compatibility, saving with `CRLF` endings is recommended.

---

### 📂 `tests\test_scrape_port.ps1`

- ⚠️ **PowerShell Line Ending Warning:** Uses `LF` format. For native Windows PowerShell compatibility, saving with `CRLF` endings is recommended.

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L5` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detected in SKILL.` | Unix nested directory creation (use PowerShell equivalent) |

---

### 📂 `tests\test_skillify_port.ps1`

- ⚠️ **PowerShell Line Ending Warning:** Uses `LF` format. For native Windows PowerShell compatibility, saving with `CRLF` endings is recommended.

#### ❌ Windows-Incompatible Bashisms

| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L12` | `if ($content -like "*$unixMkdirPattern*") { throw "FAIL: Unix mkdir -p detected ` | Unix nested directory creation (use PowerShell equivalent) |

---
