# Contributing to gstack-windows-port

Thank you for your interest in contributing to **gstack-windows-port**! This project aims to bring the robust `gstack` agent skill ecosystem to Windows 11 users designed for native PowerShell and Python compatibility.

Please take a moment to review this guide to make the contribution process smooth and effective.

---

## 🧭 Core Principles (Guidelines)

We maintain strict rules to preserve Windows 11 compatibility and maintain high-end agent automation quality:

1. **Strictly No Bashisms**: Never use Unix commands (like `ls`, `grep`, `cat`, `rm -rf`, `export`) in scripts, prompt templates, or documentation commands. Instead, use PowerShell equivalents (e.g. `Get-ChildItem`, `Remove-Item -Recurse -Force`) or cross-platform Python scripts.
2. **PowerShell-First & Python-Driven**: PowerShell is the primary orchestration environment. For complex tasks, write Python helper scripts and run them via PowerShell.
3. **Boil-the-Lake / Full Output Policy**: AI prompts and system commands must enforce complete, production-ready outputs instead of placeholders or truncated code.
4. **Safety & Grounding**: All actions must be auditable and safe. For terminal integrations or system interactions, provide validation layers.

---

## 🛠️ How to Contribute

### 1. Reporting Bugs / Requesting Features

- Before creating a new issue, search the existing issues to ensure it hasn't been reported.
- Use our **Issue Templates** to provide clear, actionable descriptions:
  - For bugs: Include your OS version (Windows 11 build), PowerShell version, step-by-step reproduction, and error logs.
  - For features: Describe the use case, why this helps Windows agent builders, and a proposed implementation design.

### 2. Developing & Modifying Skills

- All agent skills are stored inside the `skills/` directory.
- Each skill must contain a `SKILL.md` acting as the instruction core.
- If a skill makes system or terminal calls, ensure it detects and uses PowerShell commands natively under Windows.
- Clean up all temporary files created in `tmp/` during tool execution.

### 3. Pull Request (PR) Workflow

1. **Fork & Branch**: Create a branch from `main` with a descriptive name (e.g., `feature/add-win-security-skill` or `fix/powershell-encoding`).
2. **Format**: Follow standard Python (PEP 8) style and clean PowerShell formatting.
3. **Verify Locally**: Run `.\setup.ps1` and test your modified skills to confirm no regression occurs.
4. **Document**: Update the `README.md` or corresponding documentation inside `docs/` if you introduce structural changes.
5. **Open PR**: Provide a detailed description of what you changed, the testing done, and any manual verification steps.

---

## ⚖️ Code of Conduct

We are committed to fostering a welcoming, inclusive, and safe environment for all contributors, regardless of experience level. Please be respectful, professional, and collaborative in all communication.

---

*Thank you for helping make Windows AI Agent tooling robust and accessible for everyone!*
