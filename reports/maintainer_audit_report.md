# 🛡️ gstack Maintainer Audit Report
This automated report scans active files for Windows 11 compatibility issues, Bashisms, Unix-specific behaviors, and hardcoded security secrets.

> [!WARNING]
> **AUDIT ALERT:** Detected **503 potential issues** in the workspace that could impact Windows 11 compatibility or repository security.

## 📊 Summary of Findings
| File Path | Bashisms | Hardcoded Unix Paths | Hardcoded Secrets | Line Endings (CRLF) | Total Issues |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `CONTRIBUTING.md` | 3 | 0 | 0 | ✅ CRLF | **3** |
| `docs\solution-architecture.md` | 1 | 1 | 0 | ✅ CRLF | **2** |
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
| `tests\test_context_port.ps1` | 1 | 0 | 0 | ✅ CRLF | **1** |
| `tests\test_group1_core_port.ps1` | 1 | 0 | 0 | ✅ CRLF | **1** |
| `tests\test_scrape_port.ps1` | 1 | 0 | 0 | ✅ CRLF | **1** |
| `tests\test_skillify_port.ps1` | 1 | 0 | 0 | ✅ CRLF | **1** |

## 🔍 Detailed Breakdown

### 📂 `CONTRIBUTING.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like `ls`, `grep`, `cat`, ` | Unix force-remove command (use PowerShell equivalent) |
| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like `ls`, `grep`, `cat`, ` | Unix text processing utilities (use PowerShell or Python) |
| `L13` | `1. **Strictly No Bashisms**: Never use Unix commands (like `ls`, `grep`, `cat`, ` | Unix command (use PowerShell equivalent) |

---
### 📂 `docs\solution-architecture.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L23` | `49 kỹ năng của hệ sinh thái `gstack` gốc được thích ứng và port hoàn toàn sang m` | Unix text processing utilities (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L23` | `49 kỹ năng của hệ sinh thái `gstack` gốc được thích ứng và port hoàn toàn sang m` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack-autoplan\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L297` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L304` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L307` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L310` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L732` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L796` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L797` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L969` | `- Discover design docs: `ls -t ~/.gstack/projects/$SLUG/*-design-*.md 2>/dev/nul` | Unix command (use PowerShell equivalent) |
| `L970` | `- Detect UI scope: grep the plan for view/rendering terms (component, screen, fo` | Unix text processing utilities (use PowerShell or Python) |
| `L975` | `- Detect DX scope: grep the plan for developer-facing terms (API, endpoint, REST` | Unix text processing utilities (use PowerShell or Python) |

---
### 📂 `skills\gstack-benchmark\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L429` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L430` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |

---
### 📂 `skills\gstack-browse\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L431` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L432` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L638` | `Example: `$B snapshot -i -a -C -o /tmp/annotated.png`` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L770` | `| `eval <file>` | Run JavaScript from file and return result as string (path mus` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack-canary\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L287` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L294` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L297` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L300` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L696` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L697` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L739` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |

---
### 📂 `skills\gstack-careful\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L5` | `Safety guardrails for destructive commands. Warns before rm -rf, DROP TABLE,` | Unix force-remove command (use PowerShell equivalent) |
| `L36` | `> **Safety Advisory:** This skill includes safety checks that check bash command` | Unix force-remove command (use PowerShell equivalent) |
| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/data` | Recursive delete ` | Unix force-remove command (use PowerShell equivalent) |
| `L60` | `| `docker rm -f` / `docker system prune` | `docker system prune -a` | Container/` | Unix force-remove command (use PowerShell equivalent) |
| `L66` | `- `rm -rf node_modules` / `.next` / `dist` / `__pycache__` / `.cache` / `build` ` | Unix force-remove command (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L53` | `| `rm -rf` / `rm -r` / `rm --recursive` | `rm -rf /var/data` | Recursive delete ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack-checkpoint\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L290` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L297` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L300` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L303` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L832` | `find "$CHECKPOINT_DIR" -maxdepth 1 -name "*.md" -type f | Out-Null | xargs ls -1` | Unix command (use PowerShell equivalent) |
| `L895` | `find "$CHECKPOINT_DIR" -maxdepth 1 -name "*.md" -type f | Out-Null | xargs ls -1` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-context-restore\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L358` | `_GBRAIN_VERSION_OK=$(gbrain --version  | grep -c '^gbrain ' || echo 0)` | Unix text processing utilities (use PowerShell or Python) |
| `L406` | `_BRAIN_LAST=$(cat "$_BRAIN_LAST_PULL_FILE"  || echo 0)` | Unix command (use PowerShell equivalent) |
| `L420` | `_GBRAIN_HOST=$(jq -r '.mcpServers.gbrain.url // empty' "$env:USERPROFILE\.claude` | Unix text processing utilities (use PowerShell or Python) |
| `L426` | `[ -f "$_GSTACK_HOME/.brain-last-push" ] ; _BRAIN_LAST_PUSH=$(cat "$_GSTACK_HOME/` | Unix command (use PowerShell equivalent) |
| `L476` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are cheaper and` | Unix text processing utilities (use PowerShell or Python) |
| `L476` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are cheaper and` | Unix command (use PowerShell equivalent) |
| `L503` | `Get-ChildItem "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md"  | xa` | Unix command (use PowerShell equivalent) |
| `L507` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl"  | grep '"event` | Unix text processing utilities (use PowerShell or Python) |
| `L509` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl"  | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L512` | `_LATEST_CP=$(Get-ChildItem "$_PROJ/checkpoints" -name "*.md" -type f  | xargs ls` | Unix command (use PowerShell equivalent) |
| `L783` | ``ls -1t` (filesystem mtime). Filenames are stable across file-system` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-context-save\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L357` | `_GBRAIN_VERSION_OK=$(gbrain --version  | grep -c '^gbrain ' || echo 0)` | Unix text processing utilities (use PowerShell or Python) |
| `L405` | `_BRAIN_LAST=$(cat "$_BRAIN_LAST_PULL_FILE"  || echo 0)` | Unix command (use PowerShell equivalent) |
| `L419` | `_GBRAIN_HOST=$(jq -r '.mcpServers.gbrain.url // empty' "$env:USERPROFILE\.claude` | Unix text processing utilities (use PowerShell or Python) |
| `L425` | `[ -f "$_GSTACK_HOME/.brain-last-push" ] ; _BRAIN_LAST_PUSH=$(cat "$_GSTACK_HOME/` | Unix command (use PowerShell equivalent) |
| `L475` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are cheaper and` | Unix text processing utilities (use PowerShell or Python) |
| `L475` | `equivalents (cat, sed, Get-ChildItem, grep). The dedicated tools are cheaper and` | Unix command (use PowerShell equivalent) |
| `L502` | `Get-ChildItem "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md"  | xa` | Unix command (use PowerShell equivalent) |
| `L506` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl"  | grep '"event` | Unix text processing utilities (use PowerShell or Python) |
| `L508` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl"  | gre` | Unix text processing utilities (use PowerShell or Python) |
| `L511` | `_LATEST_CP=$(Get-ChildItem "$_PROJ/checkpoints" -name "*.md" -type f  | xargs ls` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-cso\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L298` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L305` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L308` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L311` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L718` | `The bash blocks throughout this skill show WHAT patterns to search for, not HOW ` | Unix text processing utilities (use PowerShell or Python) |
| `L729` | `ls package.json tsconfig.json | Out-Null ; echo "STACK: Node/TypeScript"` | Unix command (use PowerShell equivalent) |
| `L730` | `ls Gemfile | Out-Null ; echo "STACK: Ruby"` | Unix command (use PowerShell equivalent) |
| `L731` | `ls requirements.txt pyproject.toml setup.py | Out-Null ; echo "STACK: Python"` | Unix command (use PowerShell equivalent) |
| `L732` | `ls go.mod | Out-Null ; echo "STACK: Go"` | Unix command (use PowerShell equivalent) |
| `L733` | `ls Cargo.toml | Out-Null ; echo "STACK: Rust"` | Unix command (use PowerShell equivalent) |
| `L734` | `ls pom.xml build.gradle | Out-Null ; echo "STACK: JVM"` | Unix command (use PowerShell equivalent) |
| `L735` | `ls composer.json | Out-Null ; echo "STACK: PHP"` | Unix command (use PowerShell equivalent) |
| `L736` | `find . -maxdepth 1 \( -name '*.csproj' -o -name '*.sln' \) | Out-Null | grep -q ` | Unix text processing utilities (use PowerShell or Python) |
| `L742` | `grep -q "next" package.json | Out-Null ; echo "FRAMEWORK: Next.js"` | Unix text processing utilities (use PowerShell or Python) |
| `L743` | `grep -q "express" package.json | Out-Null ; echo "FRAMEWORK: Express"` | Unix text processing utilities (use PowerShell or Python) |
| `L744` | `grep -q "fastify" package.json | Out-Null ; echo "FRAMEWORK: Fastify"` | Unix text processing utilities (use PowerShell or Python) |
| `L745` | `grep -q "hono" package.json | Out-Null ; echo "FRAMEWORK: Hono"` | Unix text processing utilities (use PowerShell or Python) |
| `L746` | `grep -q "django" requirements.txt pyproject.toml | Out-Null ; echo "FRAMEWORK: D` | Unix text processing utilities (use PowerShell or Python) |
| `L747` | `grep -q "fastapi" requirements.txt pyproject.toml | Out-Null ; echo "FRAMEWORK: ` | Unix text processing utilities (use PowerShell or Python) |
| `L748` | `grep -q "flask" requirements.txt pyproject.toml | Out-Null ; echo "FRAMEWORK: Fl` | Unix text processing utilities (use PowerShell or Python) |
| `L749` | `grep -q "rails" Gemfile | Out-Null ; echo "FRAMEWORK: Rails"` | Unix text processing utilities (use PowerShell or Python) |
| `L750` | `grep -q "gin-gonic" go.mod | Out-Null ; echo "FRAMEWORK: Gin"` | Unix text processing utilities (use PowerShell or Python) |
| `L751` | `grep -q "spring-boot" pom.xml build.gradle | Out-Null ; echo "FRAMEWORK: Spring ` | Unix text processing utilities (use PowerShell or Python) |
| `L752` | `grep -q "laravel" composer.json | Out-Null ; echo "FRAMEWORK: Laravel"` | Unix text processing utilities (use PowerShell or Python) |
| `L791` | `ls .env .env.* | Out-Null` | Unix command (use PowerShell equivalent) |
| `L835` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.example\|.sample\|.template` | Unix text processing utilities (use PowerShell or Python) |
| `L835` | `git ls-files '*.env' '.env.*' | Out-Null | grep -v '.example\|.sample\|.template` | Unix command (use PowerShell equivalent) |
| `L836` | `grep -q "^\.env$\|^\.env\.\*" .gitignore | Out-Null ; echo ".env IS gitignored" ` | Unix text processing utilities (use PowerShell or Python) |
| `L843` | `[ -f "$f" ] ; grep -n "password:\|token:\|secret:\|api_key:" "$f" | grep -v '\${` | Unix text processing utilities (use PowerShell or Python) |
| `L935` | `**Key checks (beyond grep):**` | Unix text processing utilities (use PowerShell or Python) |
| `L954` | `ls -la .agents/skills/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L959` | `- `curl`, `wget`, `fetch`, `http`, `exfiltrat` (network exfiltration)` | Unix network tools (use PowerShell or Python) |
| `L971` | `**FP rules:** gstack's own skills are trusted (check if skill path resolves to a` | Unix network tools (use PowerShell or Python) |

---
### 📂 `skills\gstack-design-consultation\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L292` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L299` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L302` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L305` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L710` | `ls DESIGN.md design-system.md | Out-Null ; echo "NO_DESIGN_FILE"` | Unix command (use PowerShell equivalent) |
| `L719` | `cat README.md | Out-Null | head -50` | Unix command (use PowerShell equivalent) |
| `L720` | `cat package.json | Out-Null | head -20` | Unix command (use PowerShell equivalent) |
| `L721` | `ls src/ app/ pages/ components/ | Out-Null | head -30` | Unix command (use PowerShell equivalent) |
| `L729` | `ls ~/.gstack/projects/$SLUG/*office-hours* | Out-Null | head -5` | Unix command (use PowerShell equivalent) |
| `L730` | `ls .context/*office-hours* .context/attachments/*office-hours* | Out-Null | head` | Unix command (use PowerShell equivalent) |
| `L764` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L765` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L1084` | `cat "$_DESIGN_DIR/feedback.json"` | Unix command (use PowerShell equivalent) |
| `L1087` | `cat "$_DESIGN_DIR/feedback-pending.json"` | Unix command (use PowerShell equivalent) |
| `L1121` | ``curl -s -X POST http://127.0.0.1:PORT/api/reload -H 'Content-Type: application/` | Unix network tools (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L822` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design artifacts are U` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack-design-html\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L297` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L304` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L307` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L310` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L861` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L862` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L886` | `_CEO=$(ls -t ~/.gstack/projects/$SLUG/ceo-plans/*.md | Out-Null | head -1)` | Unix command (use PowerShell equivalent) |
| `L892` | `_APPROVED=$(ls -t ~/.gstack/projects/$SLUG/designs/*/approved.json | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L898` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/variant-*.png | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L904` | `_FINALIZED=$(ls -t ~/.gstack/projects/$SLUG/designs/*/finalized.html | Out-Null ` | Unix command (use PowerShell equivalent) |
| `L1041` | `[ -f package.json ] ; cat package.json | grep -o '"react"\|"svelte"\|"vue"\|"@an` | Unix text processing utilities (use PowerShell or Python) |
| `L1041` | `[ -f package.json ] ; cat package.json | grep -o '"react"\|"svelte"\|"vue"\|"@an` | Unix command (use PowerShell equivalent) |
| `L1301` | `_PORT=$(lsof -i -P -n | grep "$_SERVER_PID" | grep LISTEN | awk '{print $9}' | c` | Unix text processing utilities (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L729` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design artifacts are U` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L898` | `_VARIANTS=$(ls -t ~/.gstack/projects/$SLUG/designs/*/variant-*.png | Out-Null | ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack-design-review\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L292` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L299` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L302` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L305` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L719` | `$B status | Out-Null | grep -q "Mode: cdp" ; echo "CDP_MODE=true" ; echo "CDP_MO` | Unix text processing utilities (use PowerShell or Python) |
| `L772` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L773` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L802` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | Out-Null ; echo "FRAMEWORK:rails"` | Unix text processing utilities (use PowerShell or Python) |
| `L803` | `[ -f package.json ] ; grep -q '"next"' package.json | Out-Null ; echo "FRAMEWORK` | Unix text processing utilities (use PowerShell or Python) |
| `L805` | `ls jest.config.* vitest.config.* playwright.config.* .rspec pytest.ini pyproject` | Unix command (use PowerShell equivalent) |
| `L806` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L892` | `ls -d .github/ | Out-Null ; echo "CI:github"` | Unix command (use PowerShell equivalent) |
| `L893` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | Out-Null` | Unix command (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L988` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design artifacts are U` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack-design-shotgun\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L289` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L296` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L299` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L302` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L878` | `cat DESIGN.md | Out-Null | head -80 ; echo "NO_DESIGN_MD"` | Unix command (use PowerShell equivalent) |
| `L882` | `ls src/ app/ pages/ components/ | Out-Null | head -30` | Unix command (use PowerShell equivalent) |
| `L887` | `ls ~/.gstack/projects/$SLUG/*office-hours* | Out-Null | head -5` | Unix command (use PowerShell equivalent) |
| `L897` | `curl -s -o $null -w "%{http_code}" http://localhost:3000 | Out-Null ; echo "NO_L` | Unix network tools (use PowerShell or Python) |
| `L1014` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` | Unix command (use PowerShell equivalent) |
| `L1053` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' | sed 's/,$//` | Unix text processing utilities (use PowerShell or Python) |
| `L1053` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' | sed 's/,$//` | Unix command (use PowerShell equivalent) |
| `L1099` | `cat "$_DESIGN_DIR/feedback.json"` | Unix command (use PowerShell equivalent) |
| `L1102` | `cat "$_DESIGN_DIR/feedback-pending.json"` | Unix command (use PowerShell equivalent) |
| `L1136` | ``curl -s -X POST http://127.0.0.1:PORT/api/reload -H 'Content-Type: application/` | Unix network tools (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L720` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design artifacts are U` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1004` | `Final location: {_DESIGN_DIR absolute path}/variant-{letter}.png` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1011` | `4. Copy: cp $env:TEMP\variant-{letter}.png {_DESIGN_DIR}/variant-{letter}.png` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1012` | `5. Quality check: {$D path} check --image {_DESIGN_DIR}/variant-{letter}.png --b` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1014` | `6. Verify: ls -lh {_DESIGN_DIR}/variant-{letter}.png` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1027` | `**Why /tmp/ then cp?** In observed sessions, `$D generate --output ~/.gstack/...` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1028` | `failed with "The operation was aborted" while `--output /tmp/...` succeeded. Thi` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1029` | `a sandbox restriction. Always generate to `/tmp/` first, then `cp`.` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1053` | `_IMAGES=$(ls "$_DESIGN_DIR"/variant-*.png | Out-Null | tr '\n' ',' | sed 's/,$//` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L1204` | `1. **Never save to `.context/`, `docs/designs/`, or `/tmp/`.** All design artifa` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack-devex-review\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L296` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L303` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L306` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L309` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L731` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L768` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L769` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L806` | `| 1 | **Usable** | Simple to install, set up, use. Intuitive APIs. Fast feedback` | Unix network tools (use PowerShell or Python) |
| `L885` | `$GSTACK_ROOT/bin/gstack-review-read | Out-Null | grep plan-devex-review ; echo "` | Unix text processing utilities (use PowerShell or Python) |
| `L943` | `- Deprecation warnings in code (grep for deprecated/obsolete)` | Unix text processing utilities (use PowerShell or Python) |

---
### 📂 `skills\gstack-document-generate\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L360` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | grep -c '^gbrain ' || echo 0` | Unix text processing utilities (use PowerShell or Python) |
| `L422` | `_GBRAIN_HOST=$(jq -r '.mcpServers.gbrain.url // empty' "$HOME/.claude.json" 2>/d` | Unix text processing utilities (use PowerShell or Python) |
| `L478` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, grep). The dediGet-Conten` | Unix text processing utilities (use PowerShell or Python) |
| `L505` | `Get-ChildItem -Recurse "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.` | Unix command (use PowerShell equivalent) |
| `L509` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>/dev/null | g` | Unix text processing utilities (use PowerShell or Python) |
| `L511` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>/dev` | Unix text processing utilities (use PowerShell or Python) |
| `L514` | `_LATEST_CP=$(Get-ChildItem -Recurse "$_PROJ/checkpoints" -name "*.md" -type f 2>` | Unix command (use PowerShell equivalent) |
| `L686` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L895` | `- Use ASCII diagrams for architecture. They're grep-able, diff-friendly, and ren` | Unix text processing utilities (use PowerShell or Python) |
| `L1073` | `git diff --cached --no-color | grep '^+' | sed 's/^+//' | \` | Unix text processing utilities (use PowerShell or Python) |

---
### 📂 `skills\gstack-document-release\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L289` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L296` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L299` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L302` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L703` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L997` | `git commit -m "$(cat <<'EOF'` | Unix command (use PowerShell equivalent) |
| `L1048` | `glab mr update -d "$(cat <<'MRBODY'` | Unix command (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L1045` | `Read the contents of `/tmp/gstack-pr-body-$$.md` using the Read tool, then pass ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack-freeze\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L97` | `- This prevents accidental edits, not a security boundary — Bash commands like `` | Unix text processing utilities (use PowerShell or Python) |

---
### 📂 `skills\gstack-guard\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L6` | `Combines /gs:careful (warns before rm -rf, DROP TABLE, force-push, etc.) with` | Unix force-remove command (use PowerShell equivalent) |
| `L47` | `> **Safety Advisory:** This skill includes safety checks that check bash command` | Unix force-remove command (use PowerShell equivalent) |
| `L92` | `- "1. **Destructive command warnings** — rm -rf, DROP TABLE, force-push, etc. wi` | Unix force-remove command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-health\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L289` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L296` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L299` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L302` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L704` | `ls eslint.config.* .eslintrc.* .eslintrc | Out-Null | head -1 | xargs -I{} echo ` | Unix command (use PowerShell equivalent) |
| `L705` | `[ -f .pylintrc ] ; [ -f pyproject.toml ] ; grep -q "pylint\|ruff" pyproject.toml` | Unix text processing utilities (use PowerShell or Python) |
| `L708` | `[ -f package.json ] ; grep -q '"test"' package.json | Out-Null ; echo "TEST: $(n` | Unix text processing utilities (use PowerShell or Python) |
| `L709` | `[ -f pyproject.toml ] ; grep -q "pytest" pyproject.toml | Out-Null ; echo "TEST:` | Unix text processing utilities (use PowerShell or Python) |
| `L715` | `[ -f package.json ] ; grep -q '"knip"' package.json | Out-Null ; echo "DEADCODE:` | Unix text processing utilities (use PowerShell or Python) |
| `L718` | `command -v shellcheck | Out-Null 2>&1 ; ls *.sh scripts/*.sh bin/*.sh | Out-Null` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-investigate\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L308` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L315` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L318` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L321` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-land-and-deploy\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L287` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L294` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L297` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L300` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L717` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L718` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L760` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L868` | `SAVED_HASH=$(cat ~/.gstack/projects/$SLUG/land-deploy-confirmed | Out-Null)` | Unix command (use PowerShell equivalent) |
| `L869` | `CURRENT_HASH=$(sed -n '/## Deploy Configuration/,/^## /p' CLAUDE.md | Out-Null |` | Unix text processing utilities (use PowerShell or Python) |
| `L871` | `WORKFLOW_HASH=$(find .github/workflows -maxdepth 1 \( -name '*deploy*' -o -name ` | Unix command (use PowerShell equivalent) |
| `L908` | `DEPLOY_CONFIG=$(grep -A 20 "## Deploy Configuration" CLAUDE.md | Out-Null ; echo` | Unix text processing utilities (use PowerShell or Python) |
| `L913` | `PROD_URL=$(echo "$DEPLOY_CONFIG" | grep -i "production.*url" | head -1 | sed 's/` | Unix text processing utilities (use PowerShell or Python) |
| `L914` | `PLATFORM=$(echo "$DEPLOY_CONFIG" | grep -i "platform" | head -1 | sed 's/.*: *//` | Unix text processing utilities (use PowerShell or Python) |
| `L929` | `[ -f "$f" ] ; grep -qiE "deploy|release|production|cd" "$f" | Out-Null ; echo "D` | Unix text processing utilities (use PowerShell or Python) |
| `L930` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Out-Null ; echo "STAGING_WORKFLOW:$f"` | Unix text processing utilities (use PowerShell or Python) |
| `L975` | `║  ├─ curl prod URL:      ✓ PASS (200 OK) / ⚠ UNREACHABLE   ║` | Unix network tools (use PowerShell or Python) |
| `L996` | `failed at Step 1). If `curl` fails, note "I couldn't reach that URL — might be a` | Unix network tools (use PowerShell or Python) |
| `L1010` | `grep -i "staging" CLAUDE.md | Out-Null | head -3` | Unix text processing utilities (use PowerShell or Python) |
| `L1017` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Out-Null ; echo "STAGING_WORKFLOW:$f"` | Unix text processing utilities (use PowerShell or Python) |
| `L1067` | `CURRENT_HASH=$(sed -n '/## Deploy Configuration/,/^## /p' CLAUDE.md | Out-Null |` | Unix text processing utilities (use PowerShell or Python) |
| `L1068` | `WORKFLOW_HASH=$(find .github/workflows -maxdepth 1 \( -name '*deploy*' -o -name ` | Unix command (use PowerShell equivalent) |
| `L1185` | `cat $GSTACK_ROOT/review/checklist.md | Out-Null ; echo "Checklist not found"` | Unix command (use PowerShell equivalent) |
| `L1219` | `ls -t ~/.gstack-dev/evals/*-e2e-*-$(date +%Y-%m-%d)*.json | Out-Null | head -20` | Unix command (use PowerShell equivalent) |
| `L1236` | `ls -t ~/.gstack-dev/evals/*-llm-judge-*-$(date +%Y-%m-%d)*.json | Out-Null | hea` | Unix command (use PowerShell equivalent) |
| `L1269` | `git log --oneline --all-match --grep="docs:" $(gh pr view --json baseRefName -q ` | Unix text processing utilities (use PowerShell or Python) |
| `L1435` | `DEPLOY_CONFIG=$(grep -A 20 "## Deploy Configuration" CLAUDE.md | Out-Null ; echo` | Unix text processing utilities (use PowerShell or Python) |
| `L1440` | `PROD_URL=$(echo "$DEPLOY_CONFIG" | grep -i "production.*url" | head -1 | sed 's/` | Unix text processing utilities (use PowerShell or Python) |
| `L1441` | `PLATFORM=$(echo "$DEPLOY_CONFIG" | grep -i "platform" | head -1 | sed 's/.*: *//` | Unix text processing utilities (use PowerShell or Python) |
| `L1456` | `[ -f "$f" ] ; grep -qiE "deploy|release|production|cd" "$f" | Out-Null ; echo "D` | Unix text processing utilities (use PowerShell or Python) |
| `L1457` | `[ -f "$f" ] ; grep -qiE "staging" "$f" | Out-Null ; echo "STAGING_WORKFLOW:$f"` | Unix text processing utilities (use PowerShell or Python) |
| `L1561` | `curl -sf {production-url} -o $null -w "%{http_code}" | Out-Null` | Unix network tools (use PowerShell or Python) |

---
### 📂 `skills\gstack-learn\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L289` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L296` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L299` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L302` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L799` | `cat "$LEARN_FILE" | bun -e "` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-maintainer-auditor\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L52` | `- **Tự động đề xuất đoạn mã sửa đổi** bằng PowerShell thuần túy Windows (Ví dụ: ` | Unix force-remove command (use PowerShell equivalent) |
| `L52` | `- **Tự động đề xuất đoạn mã sửa đổi** bằng PowerShell thuần túy Windows (Ví dụ: ` | Unix nested directory creation (use PowerShell equivalent) |

---
### 📂 `skills\gstack-make-pdf\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L278` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | grep -c '^gbrain ' || echo 0` | Unix text processing utilities (use PowerShell or Python) |
| `L340` | `_GBRAIN_HOST=$(jq -r '.mcpServers.gbrain.url // empty' "$HOME/.claude.json" 2>/d` | Unix text processing utilities (use PowerShell or Python) |
| `L396` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, grep). The dediGet-Conten` | Unix text processing utilities (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L487` | `$P generate letter.md                 # writes /tmp/letter.pdf` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L591` | `stdout: /tmp/letter.pdf          ← just the path, one line` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L594` | `Done in 1.5s. 43 words · 22KB · /tmp/letter.pdf` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack-office-hours\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L297` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L304` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L307` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L310` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L727` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L728` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L763` | `ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-Null` | Unix command (use PowerShell equivalent) |
| `L1029` | `Extract 3-5 significant keywords from the user's problem statement and grep acro` | Unix text processing utilities (use PowerShell or Python) |
| `L1033` | `grep -li "<keyword1>\|<keyword2>\|<keyword3>" ~/.gstack/projects/$SLUG/*-design-` | Unix text processing utilities (use PowerShell or Python) |
| `L1209` | `4. POST the new HTML to the running server via `curl -X POST http://localhost:PO` | Unix network tools (use PowerShell or Python) |
| `L1315` | `Use a 5-minute timeout (`timeout: 300000`). After completion: `cat "$TMPERR_SKET` | Unix force-remove command (use PowerShell equivalent) |
| `L1315` | `Use a 5-minute timeout (`timeout: 300000`). After completion: `cat "$TMPERR_SKET` | Unix command (use PowerShell equivalent) |
| `L1387` | `PRIOR=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head -` | Unix command (use PowerShell equivalent) |
| `L1605` | `SESSION_TIER=$(echo "$PROFILE" | grep "^TIER:" | awk '{print $2}')` | Unix text processing utilities (use PowerShell or Python) |
| `L1606` | `SESSION_COUNT=$(echo "$PROFILE" | grep "^SESSION_COUNT:" | awk '{print $2}')` | Unix text processing utilities (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L1288` | `The screenshot file at `/tmp/gstack-sketch.png` can be referenced by downstream ` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack-open-gstack-browser\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L287` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L294` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L297` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L300` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L722` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L723` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L744` | `_OLD_PID=$(cat "$(git rev-parse --show-toplevel)/.gstack/browse.json" | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L744` | `_OLD_PID=$(cat "$(git rev-parse --show-toplevel)/.gstack/browse.json" | Out-Null` | Unix command (use PowerShell equivalent) |
| `L790` | `cat "$(git rev-parse --show-toplevel | Out-Null)/.gstack/browse.json" | Out-Null` | Unix text processing utilities (use PowerShell or Python) |
| `L790` | `cat "$(git rev-parse --show-toplevel | Out-Null)/.gstack/browse.json" | Out-Null` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-pair-agent\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L291` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L298` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L301` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L304` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L744` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L745` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L949` | ``exec curl` syntax which OpenClaw understands natively. When using `--local open` | Unix network tools (use PowerShell or Python) |
| `L955` | `curl commands work directly. When using `--local codex`, credentials are written` | Unix network tools (use PowerShell or Python) |

---
### 📂 `skills\gstack-plan-ceo-review\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L293` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L300` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L303` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L306` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L728` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L821` | `grep -r "TODO\|FIXME\|HACK\|XXX" -l --exclude-dir=node_modules --exclude-dir=ven` | Unix text processing utilities (use PowerShell or Python) |
| `L832` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L833` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L842` | `HANDOFF=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-ceo-handoff-*.md | Out-Null |` | Unix command (use PowerShell equivalent) |
| `L907` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L908` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-N` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-plan-design-review\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L290` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L297` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L300` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L303` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L725` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L1045` | `- `mkdir -p ~/.gstack/projects/$SLUG/designs/...`` | Unix nested directory creation (use PowerShell equivalent) |
| `L1123` | `cat "$_DESIGN_DIR/feedback.json"` | Unix command (use PowerShell equivalent) |
| `L1126` | `cat "$_DESIGN_DIR/feedback-pending.json"` | Unix command (use PowerShell equivalent) |
| `L1160` | ``curl -s -X POST http://127.0.0.1:PORT/api/reload -H 'Content-Type: application/` | Unix network tools (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L992` | ``docs/designs/`, `/tmp/`, or any project-local directory. Design artifacts are U` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack-plan-devex-review\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L300` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L307` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L310` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L313` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L735` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L786` | `| 1 | **Usable** | Simple to install, set up, use. Intuitive APIs. Fast feedback` | Unix network tools (use PowerShell or Python) |
| `L868` | `- Getting started guides (grep README for "Getting Started", "Quick Start", "Ins` | Unix text processing utilities (use PowerShell or Python) |
| `L869` | `- CLI help text (grep for `--help`, `usage:`, `commands:`)` | Unix text processing utilities (use PowerShell or Python) |
| `L870` | `- Error message patterns (grep for `throw new Error`, `console.error`, error cla` | Unix text processing utilities (use PowerShell or Python) |
| `L879` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L880` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L943` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L944` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L1316` | `$GSTACK_ROOT/bin/gstack-review-read | Out-Null | grep plan-devex-review ; echo "` | Unix text processing utilities (use PowerShell or Python) |

---
### 📂 `skills\gstack-plan-eng-review\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L295` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L302` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L305` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L308` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L753` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L754` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L811` | `DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-$BRANCH-design-*.md | Out-Null | head ` | Unix command (use PowerShell equivalent) |
| `L812` | `[ -z "$DESIGN" ] ; DESIGN=$(ls -t ~/.gstack/projects/$SLUG/*-design-*.md | Out-N` | Unix command (use PowerShell equivalent) |
| `L940` | `ls jest.config.* vitest.config.* playwright.config.* cypress.config.* .rspec pyt` | Unix command (use PowerShell equivalent) |
| `L941` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-plan-tune\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L300` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L307` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L310` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L313` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-qa-only\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L290` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L297` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L300` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L303` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L740` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L741` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L782` | `ls -t ~/.gstack/projects/$SLUG/*-test-plan-*.md | Out-Null | head -1` | Unix command (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L707` | `| Output dir | `.gstack/qa-reports/` | `Output to /tmp/qa` |` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack-qa\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L297` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L304` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L307` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L310` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L732` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L772` | `$B status | Out-Null | grep -q "Mode: cdp" ; echo "CDP_MODE=true" ; echo "CDP_MO` | Unix text processing utilities (use PowerShell or Python) |
| `L821` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L822` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L851` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | Out-Null ; echo "FRAMEWORK:rails"` | Unix text processing utilities (use PowerShell or Python) |
| `L852` | `[ -f package.json ] ; grep -q '"next"' package.json | Out-Null ; echo "FRAMEWORK` | Unix text processing utilities (use PowerShell or Python) |
| `L854` | `ls jest.config.* vitest.config.* playwright.config.* .rspec pytest.ini pyproject` | Unix command (use PowerShell equivalent) |
| `L855` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L941` | `ls -d .github/ | Out-Null ; echo "CI:github"` | Unix command (use PowerShell equivalent) |
| `L942` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | Out-Null` | Unix command (use PowerShell equivalent) |
| `L1022` | `ls -t ~/.gstack/projects/$SLUG/*-test-plan-*.md | Out-Null | head -1` | Unix command (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L757` | `| Output dir | `.gstack/qa-reports/` | `Output to /tmp/qa` |` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack-retro\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L287` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L294` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L297` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L300` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L701` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L803` | `git log origin/<default> --since="<window>" --format="" --name-only | grep -v '^` | Unix text processing utilities (use PowerShell or Python) |
| `L806` | `git log origin/<default> --since="<window>" --format="%s" | grep -oE '[#!][0-9]+` | Unix text processing utilities (use PowerShell or Python) |
| `L815` | `cat ~/.gstack/greptile-history.md | Out-Null ; true` | Unix command (use PowerShell equivalent) |
| `L818` | `cat TODOS.md | Out-Null ; true` | Unix command (use PowerShell equivalent) |
| `L821` | `find . -name '*.test.*' -o -name '*.spec.*' -o -name '*_test.*' -o -name '*_spec` | Unix text processing utilities (use PowerShell or Python) |
| `L824` | `git log origin/<default> --since="<window>" --oneline --grep="test(qa):" --grep=` | Unix text processing utilities (use PowerShell or Python) |
| `L827` | `cat ~/.gstack/analytics/skill-usage.jsonl | Out-Null ; true` | Unix command (use PowerShell equivalent) |
| `L830` | `git log origin/<default> --since="<window>" --format="" --name-only | grep -E '\` | Unix text processing utilities (use PowerShell or Python) |
| `L1072` | `ls -t .context/retros/*.json | Out-Null` | Unix command (use PowerShell equivalent) |
| `L1103` | `existing=$(ls .context/retros/${today}-*.json | Out-Null | wc -l | tr -d ' ')` | Unix command (use PowerShell equivalent) |
| `L1239` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Null | grep '"skill":"ship"' ` | Unix text processing utilities (use PowerShell or Python) |
| `L1239` | `cat ~/.gstack/projects/$SLUG/*-reviews.jsonl | Out-Null | grep '"skill":"ship"' ` | Unix command (use PowerShell equivalent) |
| `L1378` | `git -C <path> log origin/$DEFAULT --since="<start_date>T00:00:00" --format="%s" ` | Unix text processing utilities (use PowerShell or Python) |
| `L1575` | `ls -t ~/.gstack/retros/global-*.json | Out-Null | head -5` | Unix command (use PowerShell equivalent) |
| `L1595` | `existing=$(ls ~/.gstack/retros/global-${today}-*.json | Out-Null | wc -l | tr -d` | Unix command (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L1349` | `Read the stderr output from `/tmp/gstack-discover-stderr` for diagnostic info. P` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack-review\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L291` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L298` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L301` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L304` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L726` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L803` | `_PLAN_SLUG=$(git remote get-url origin | Out-Null | sed 's|.*[:/]\([^/]*/[^/]*\)` | Unix text processing utilities (use PowerShell or Python) |
| `L808` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" | Out-Null | ` | Unix text processing utilities (use PowerShell or Python) |
| `L808` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L809` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$REPO` | Unix text processing utilities (use PowerShell or Python) |
| `L809` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$REPO` | Unix command (use PowerShell equivalent) |
| `L810` | `[ -z "$PLAN" ] ; PLAN=$(find "$PLAN_DIR" -name '*.md' -mmin -1440 -maxdepth 1 | ` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-scrape\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L349` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper and clearer.` | Unix text processing utilities (use PowerShell or Python) |
| `L349` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper and clearer.` | Unix command (use PowerShell equivalent) |
| `L378` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L385` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L388` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L391` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-setup-browser-cookies\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L407` | `$B status | Out-Null | grep -q "Mode: cdp" ; echo "CDP_MODE=true" ; echo "CDP_MO` | Unix text processing utilities (use PowerShell or Python) |
| `L447` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L448` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |

---
### 📂 `skills\gstack-setup-deploy\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L290` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L297` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L300` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L303` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L691` | `grep -A 20 "## Deploy Configuration" CLAUDE.md | Out-Null ; echo "NO_CONFIG"` | Unix text processing utilities (use PowerShell or Python) |
| `L710` | `[ -f fly.toml ] ; echo "PLATFORM:fly" ; cat fly.toml` | Unix command (use PowerShell equivalent) |
| `L711` | `[ -f render.yaml ] ; echo "PLATFORM:render" ; cat render.yaml` | Unix command (use PowerShell equivalent) |
| `L713` | `[ -f netlify.toml ] ; echo "PLATFORM:netlify" ; cat netlify.toml` | Unix command (use PowerShell equivalent) |
| `L719` | `[ -f "$f" ] ; grep -qiE "deploy|release|production|staging|cd" "$f" | Out-Null ;` | Unix text processing utilities (use PowerShell or Python) |
| `L723` | `[ -f package.json ] ; grep -q '"bin"' package.json | Out-Null ; echo "PROJECT_TY` | Unix text processing utilities (use PowerShell or Python) |
| `L724` | `find . -maxdepth 1 -name '*.gemspec' | Out-Null | grep -q . ; echo "PROJECT_TYPE` | Unix text processing utilities (use PowerShell or Python) |
| `L735` | `1. Extract app name: `grep -m1 "^app" fly.toml | sed 's/app = "\(.*\)"/\1/'`` | Unix text processing utilities (use PowerShell or Python) |
| `L763` | `2. If installed: `vercel ls --prod 2>/dev/null | head -3`` | Unix command (use PowerShell equivalent) |
| `L837` | `curl -sf "{health-check-url}" -o $null -w "%{http_code}" | Out-Null ; echo "UNRE` | Unix network tools (use PowerShell or Python) |

---
### 📂 `skills\gstack-ship\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L293` | `find "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.md" | Out-Null | x` | Unix command (use PowerShell equivalent) |
| `L300` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-Null | gr` | Unix text processing utilities (use PowerShell or Python) |
| `L303` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" | Out-` | Unix text processing utilities (use PowerShell or Python) |
| `L306` | `_LATEST_CP=$(find "$_PROJ/checkpoints" -name "*.md" -type f | Out-Null | xargs l` | Unix command (use PowerShell equivalent) |
| `L728` | `1. `git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's|refs/remotes/` | Unix text processing utilities (use PowerShell or Python) |
| `L869` | `git diff origin/<base> --name-only | grep -E '(cmd/.*/main\.go|bin/|Cargo\.toml|` | Unix text processing utilities (use PowerShell or Python) |
| `L875` | `ls .github/workflows/ | Out-Null | grep -iE 'release|publish|dist'` | Unix text processing utilities (use PowerShell or Python) |
| `L875` | `ls .github/workflows/ | Out-Null | grep -iE 'release|publish|dist'` | Unix command (use PowerShell equivalent) |
| `L876` | `grep -qE 'release|publish|deploy' .gitlab-ci.yml | Out-Null ; echo "GITLAB_CI_RE` | Unix text processing utilities (use PowerShell or Python) |
| `L924` | `[ -f Gemfile ] ; grep -q "rails" Gemfile | Out-Null ; echo "FRAMEWORK:rails"` | Unix text processing utilities (use PowerShell or Python) |
| `L925` | `[ -f package.json ] ; grep -q '"next"' package.json | Out-Null ; echo "FRAMEWORK` | Unix text processing utilities (use PowerShell or Python) |
| `L927` | `ls jest.config.* vitest.config.* playwright.config.* .rspec pytest.ini pyproject` | Unix command (use PowerShell equivalent) |
| `L928` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L1014` | `ls -d .github/ | Out-Null ; echo "CI:github"` | Unix command (use PowerShell equivalent) |
| `L1015` | `ls .gitlab-ci.yml .circleci/ bitrise.yml | Out-Null` | Unix command (use PowerShell equivalent) |
| `L1233` | `grep -l "changed_file_basename" test/evals/*_eval_runner.rb` | Unix text processing utilities (use PowerShell or Python) |
| `L1241` | `- Changes to `config/system_prompts/*.txt` — grep eval runners for the prompt fi` | Unix text processing utilities (use PowerShell or Python) |
| `L1297` | `ls jest.config.* vitest.config.* playwright.config.* cypress.config.* .rspec pyt` | Unix command (use PowerShell equivalent) |
| `L1298` | `ls -d test/ tests/ spec/ __tests__/ cypress/ e2e/ | Out-Null` | Unix command (use PowerShell equivalent) |
| `L1307` | `find . -name '*.test.*' -o -name '*.spec.*' -o -name '*_test.*' -o -name '*_spec` | Unix text processing utilities (use PowerShell or Python) |
| `L1474` | `find . -name '*.test.*' -o -name '*.spec.*' -o -name '*_test.*' -o -name '*_spec` | Unix text processing utilities (use PowerShell or Python) |
| `L1581` | `_PLAN_SLUG=$(git remote get-url origin | Out-Null | sed 's|.*[:/]\([^/]*/[^/]*\)` | Unix text processing utilities (use PowerShell or Python) |
| `L1586` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" | Out-Null | ` | Unix text processing utilities (use PowerShell or Python) |
| `L1586` | `PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$BRANCH" | Out-Null | ` | Unix command (use PowerShell equivalent) |
| `L1587` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$REPO` | Unix text processing utilities (use PowerShell or Python) |
| `L1587` | `[ -z "$PLAN" ] ; PLAN=$(ls -t "$PLAN_DIR"/*.md | Out-Null | xargs grep -l "$REPO` | Unix command (use PowerShell equivalent) |
| `L1588` | `[ -z "$PLAN" ] ; PLAN=$(find "$PLAN_DIR" -name '*.md' -mmin -1440 -maxdepth 1 | ` | Unix command (use PowerShell equivalent) |
| `L1723` | `curl -s -o $null -w '%{http_code}' http://localhost:3000 | Out-Null ; \` | Unix network tools (use PowerShell or Python) |
| `L1724` | `curl -s -o $null -w '%{http_code}' http://localhost:8080 | Out-Null ; \` | Unix network tools (use PowerShell or Python) |
| `L1725` | `curl -s -o $null -w '%{http_code}' http://localhost:5173 | Out-Null ; \` | Unix network tools (use PowerShell or Python) |
| `L1726` | `curl -s -o $null -w '%{http_code}' http://localhost:4000 | Out-Null ; echo "NO_S` | Unix network tools (use PowerShell or Python) |
| `L1736` | `cat ${CLAUDE_SKILL_DIR}/../qa-only/SKILL.md` | Unix command (use PowerShell equivalent) |
| `L2052` | `CURRENT_VERSION=$(cat VERSION | Out-Null | tr -d '\r\n[:space:]' ; echo "0.0.0.0` | Unix command (use PowerShell equivalent) |
| `L2117` | `if ! printf '%s' "$NEW_VERSION" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$'; t` | Unix text processing utilities (use PowerShell or Python) |
| `L2143` | `REPAIR_VERSION=$(cat VERSION | tr -d '\r\n[:space:]')` | Unix command (use PowerShell equivalent) |
| `L2144` | `if ! printf '%s' "$REPAIR_VERSION" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$'` | Unix text processing utilities (use PowerShell or Python) |
| `L2300` | `git commit -m "$(cat <<'EOF'` | Unix command (use PowerShell equivalent) |
| `L2465` | `gh pr create --base <base> --title "<type>: <summary>" --body "$(cat <<'EOF'` | Unix command (use PowerShell equivalent) |
| `L2474` | `glab mr create -b <base> -t "<type>: <summary>" -d "$(cat <<'EOF'` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-skillify\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L374` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper and clearer.` | Unix text processing utilities (use PowerShell or Python) |
| `L374` | `equivalents (cat, sed, find, grep). The dedicated tools are cheaper and clearer.` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack-spec\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L355` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | grep -c '^gbrain ' || echo 0` | Unix text processing utilities (use PowerShell or Python) |
| `L417` | `_GBRAIN_HOST=$(jq -r '.mcpServers.gbrain.url // empty' "$HOME/.claude.json" 2>/d` | Unix text processing utilities (use PowerShell or Python) |
| `L473` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, grep). The dediGet-Conten` | Unix text processing utilities (use PowerShell or Python) |
| `L500` | `Get-ChildItem -Recurse "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.` | Unix command (use PowerShell equivalent) |
| `L504` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>/dev/null | g` | Unix text processing utilities (use PowerShell or Python) |
| `L506` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>/dev` | Unix text processing utilities (use PowerShell or Python) |
| `L509` | `_LATEST_CP=$(Get-ChildItem -Recurse "$_PROJ/checkpoints" -name "*.md" -type f 2>` | Unix command (use PowerShell equivalent) |
| `L884` | `[ -z "$REDACT_VIS" ] && REDACT_VIS=$(glab repo view -F json 2>/dev/null | grep -` | Unix text processing utilities (use PowerShell or Python) |
| `L1330` | `_GBRAIN_VERSION_OK=$(gbrain --version 2>/dev/null | grep -c '^gbrain ' || echo 0` | Unix text processing utilities (use PowerShell or Python) |
| `L1392` | `_GBRAIN_HOST=$(jq -r '.mcpServers.gbrain.url // empty' "$HOME/.claude.json" 2>/d` | Unix text processing utilities (use PowerShell or Python) |
| `L1448` | `equivalents (Get-Content, sed, Get-ChildItem -Recurse, grep). The dediGet-Conten` | Unix text processing utilities (use PowerShell or Python) |
| `L1475` | `Get-ChildItem -Recurse "$_PROJ/ceo-plans" "$_PROJ/checkpoints" -type f -name "*.` | Unix command (use PowerShell equivalent) |
| `L1479` | `_LAST=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>/dev/null | g` | Unix text processing utilities (use PowerShell or Python) |
| `L1481` | `_RECENT_SKILLS=$(grep "\"branch\":\"${_BRANCH}\"" "$_PROJ/timeline.jsonl" 2>/dev` | Unix text processing utilities (use PowerShell or Python) |
| `L1484` | `_LATEST_CP=$(Get-ChildItem -Recurse "$_PROJ/checkpoints" -name "*.md" -type f 2>` | Unix command (use PowerShell equivalent) |
| `L1685` | `ISSUE_NUMBER=$(echo "$ISSUE_URL" | sed -E 's|.*/issues/([0-9]+)$|\1|')` | Unix text processing utilities (use PowerShell or Python) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L859` | `printf '%s' "<the final draft body>" > /tmp/spec-semantic-$$.txt` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L862` | `/tmp/spec-semantic-$$.txt` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L863` | `Remove-Item -Force /tmp/spec-semantic-$$.txt` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L928` | `TMPERR_GATE=$(mktemp /tmp/spec-gate-XXXXXXXX)` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

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
| `L75` | `_SNOOZED_VER=$(awk '{print $1}' "$_SNOOZE_FILE")` | Unix text processing utilities (use PowerShell or Python) |
| `L77` | `_CUR_LEVEL=$(awk '{print $2}' "$_SNOOZE_FILE")` | Unix text processing utilities (use PowerShell or Python) |
| `L132` | `OLD_VERSION=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; echo "unknown")` | Unix command (use PowerShell equivalent) |
| `L186` | `if ! grep -qF '.agents/skills/gstack/' .gitignore | Out-Null; then` | Unix text processing utilities (use PowerShell or Python) |
| `L223` | `m_ver="$(basename "$migration" .sh | sed 's/^v//')"` | Unix text processing utilities (use PowerShell or Python) |
| `L295` | `PRIMARY_VER=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; echo "unknown")` | Unix command (use PowerShell equivalent) |
| `L296` | `LOCAL_VER=$(cat "$LOCAL_GSTACK/VERSION" | Out-Null ; echo "unknown")` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L466` | `curl -fsSL "https://bun.sh/install" -o "$tmpfile"` | Unix network tools (use PowerShell or Python) |
| `L467` | `actual_sha=$(shasum -a 256 "$tmpfile" | awk '{print $1}')` | Unix text processing utilities (use PowerShell or Python) |
| `L490` | `> Set them before running: `export TEST_EMAIL="..." TEST_PASSWORD="..."`` | Unix environment variable export (use PowerShell equivalent) |

#### ⚠️ Unix-Centric Paths
| Line | Code Snippet | Recommendation |
| :--- | :--- | :--- |
| `L706` | `Example: `$B snapshot -i -a -C -o /tmp/annotated.png`` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |
| `L811` | `| `eval <file>` | Run JavaScript from file and return result as string (path mus` | Hardcoded Unix path prefix (use relative paths or standard environment variables) |

---
### 📂 `skills\gstack\gstack-upgrade\SKILL.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L68` | `_SNOOZED_VER=$(awk '{print $1}' "$_SNOOZE_FILE")` | Unix text processing utilities (use PowerShell or Python) |
| `L70` | `_CUR_LEVEL=$(awk '{print $2}' "$_SNOOZE_FILE")` | Unix text processing utilities (use PowerShell or Python) |
| `L125` | `OLD_VERSION=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; echo "unknown")` | Unix command (use PowerShell equivalent) |
| `L179` | `if ! grep -qF '.agents/skills/gstack/' .gitignore | Out-Null; then` | Unix text processing utilities (use PowerShell or Python) |
| `L216` | `m_ver="$(basename "$migration" .sh | sed 's/^v//')"` | Unix text processing utilities (use PowerShell or Python) |
| `L288` | `PRIMARY_VER=$(cat "$INSTALL_DIR/VERSION" | Out-Null ; echo "unknown")` | Unix command (use PowerShell equivalent) |
| `L289` | `LOCAL_VER=$(cat "$LOCAL_GSTACK/VERSION" | Out-Null ; echo "unknown")` | Unix command (use PowerShell equivalent) |

---
### 📂 `skills\gstack\review\checklist.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L70` | `- **Trace it through every consumer.** Read (don't just grep — READ) each file t` | Unix text processing utilities (use PowerShell or Python) |
| `L74` | `To do this: use Grep to find all references to the sibling values (e.g., grep fo` | Unix text processing utilities (use PowerShell or Python) |

---
### 📂 `skills\gstack\review\design-checklist.md`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L25` | `- **[HIGH]** — Reliably detectable via grep/pattern match. Definitive findings.` | Unix text processing utilities (use PowerShell or Python) |

---
### 📂 `tests\test_context_port.ps1`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L6` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detected in $s" }` | Unix nested directory creation (use PowerShell equivalent) |

---
### 📂 `tests\test_group1_core_port.ps1`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L9` | `if ($content -like $mkdir_pattern) { throw "FAIL: Unix mkdir -p detected in $s" ` | Unix nested directory creation (use PowerShell equivalent) |

---
### 📂 `tests\test_scrape_port.ps1`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L5` | `if ($content -like "*mkdir -p*") { throw "FAIL: Unix mkdir -p detected in SKILL.` | Unix nested directory creation (use PowerShell equivalent) |

---
### 📂 `tests\test_skillify_port.ps1`

#### ❌ Windows-Incompatible Bashisms
| Line | Code Snippet | Compatibility Issue Description |
| :--- | :--- | :--- |
| `L13` | `if ($content -like "*$unixMkdirPattern*") { throw "FAIL: Unix mkdir -p detected ` | Unix nested directory creation (use PowerShell equivalent) |

---