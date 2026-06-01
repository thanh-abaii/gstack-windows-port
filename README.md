# gstack Windows 11 Native Port (ud-re-suite)

<p align="left">
  <a href="https://github.com/thanh-abaii/gstack-windows-port/actions/workflows/ci.yml"><img src="https://github.com/thanh-abaii/gstack-windows-port/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-8b5cf6.svg" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/python-3.8%2B-6366f1" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/deps-stdlib%20only-a855f7" alt="deps: stdlib only">
  <img src="https://img.shields.io/badge/platforms-Windows%2011%20only-0078d4" alt="platforms: Windows 11 only">
</p>

> [!CAUTION]
> **WINDOWS ONLY:** This suite is built with PowerShell and Python. It is **NOT** compatible with macOS or Linux.
> **CHỈ DÀNH CHO WINDOWS:** Bộ công cụ này được xây dựng bằng PowerShell và Python. **KHÔNG** tương thích với macOS hoặc Linux.

---

| [🇺🇸 English Version](#-english-version) | [🇻🇳 Phiên bản Tiếng Việt](#-tiếng-việt) |
| :--- | :--- |

---

<a name="-english-version"></a>

## 🇺🇸 English Version

### 🌟 Overview

This is the **Official v1.2.0 "Hardened Plus"** release of the gstack skill ecosystem, adapted for Windows 11. This port represents a practical architectural shift from the Unix-centric original to a high-performance **Hybrid Orchestration** model.

- **Original Creator:** [Garry Tan](https://github.com/garrytan)
- **Repo Source:** [github.com/garrytan/gstack](https://github.com/garrytan/gstack)
- **Port Version:** `v1.2.0` (May 2026 - Hardened Plus)
- **Primary Maintainer & Educational Hub:** Maintained by an administrator of the [Bình Dân Học AI Facebook Group](https://www.facebook.com/groups/binhdanhocai), widely recognized as Vietnam’s largest AI learning community with 650k+ members, as a practical reference for Windows-native agent workflows.

### 🌍 Why Windows Native Agent Tooling Matters

Most modern AI coding agents (such as Claude Code, Aider, and custom agent harnesses) are heavily biased towards Unix/Linux environments. When executing commands on Windows, they frequently inject Bashisms, fail to parse paths correctly, or crash due to Shell compatibility issues. `gstack-windows-port` directly addresses this systemic ecosystem gap by providing a reliable, hardened, and PowerShell-first sandbox with 49 Windows adapted agent skills, turning Windows 11 into a first-class Windows-oriented host for autonomous AI developer agents.

### 🚀 Technical Highlights (Port Features)

- **Hybrid Orchestration (IEX Pattern):** Utilizes `python | iex` to bypass Windows Shell limitations, designed to improve command fidelity.
- **Boil the Lake Philosophy:** Hardcoded completeness checks that encourage broader test coverage, reducing incomplete agent outputs.
- **Surgical Refactor v2.4:** All 49 skills have been stripped of Bashisms and "Hardened" with Python logic.
- **Reality Grounding:** Browser verification using Gemini's native `browser_agent` integration.

### 📚 Research & Documentation

Deep-dive into the port's anatomy:

- [Strategic Synthesis (McKinsey Style)](docs/strategic-synthesis-gstack-v2.md)
- [Technical Deep-Dive & System Intent](docs/system-intent.md)
- [Artifact Taxonomy & Safety Gates](docs/repo-artifact-taxonomy.md)
- [Full Skill Network Graph](assets/diagrams/gstack_skill_network_graph.jpg)
- [v1.2.0 Automated Windows Compatibility & Secrets Audit Report](reports/maintainer_audit_report_v1.2.0.md)
- [gstack Maintainer Auditor Skill Instruction Core](skills/gstack-maintainer-auditor/SKILL.md)

#### 📊 Visual System Architecture & Pipelines

Here are the visual representations of gstack's Windows native hybrid architecture and pipelines:

![Hybrid Orchestration Flow](assets/diagrams/visual_1776585736073.jpg)

*Figure 1: gstack Windows Native Hybrid Orchestration Flow.*

![Surgical Refactor Pipeline](assets/diagrams/visual_1776588424229.jpg)

*Figure 2: Unix-to-Windows Surgical Refactor Pipeline.*

![Feature Gate Logic](assets/diagrams/visual_1776591125261.jpg)

*Figure 3: Hardened Control Gates & Security Logic.*

### 🛠️ Active Skills Directory (49 Hardened Skills)

To ensure maximum transparency, here is the complete directory of the **49 active skills** fully ported and covered by current static checks on Windows 11:

| Category | Skills | Description |
| :--- | :--- | :--- |
| **Core Dev & Automation** | `scrape`, `skillify`, `spec`, `document-generate`, `make-pdf` | Web scraping, automated skill creation, spec writing, and PDF reporting pipelines. |
| **Context & State** | `context-save`, `context-restore`, `freeze`, `unfreeze` | Agent state capture, workspace freeze boundary logic, and session state recovery. |
| **Infra & Knowledge** | `setup-gbrain`, `sync-gbrain`, `codex`, `benchmark-models`, `landing-report`, `upgrade` | Global database setup, benchmark analysis, release report generation, and updates. |
| **UI/UX & Design** | `design-consultation`, `design-html`, `design-review`, `design-shotgun`, `devex-review` | Beautiful UI design auditing, HTML/CSS generation pipelines, and dev experience reviews. |
| **QA & Diagnostics** | `qa`, `qa-only`, `canary`, `health`, `checkpoint`, `investigate`, `office-hours`, `retro` | Test harnesses, canary deployments, system diagnostics, and retro reviews. |
| **Git & PR Workflows** | `ship`, `land-and-deploy`, `setup-deploy`, `setup-browser-cookies`, `open-gstack-browser` | Safe commit packaging, interactive PR land-and-verify loops, and secure browser setups. |
| **System Security** | `maintainer-auditor` | Static analysis pipeline to eliminate Unix Bashisms and secure code secrets. |
| **Core Orchestration** | `autoplan`, `benchmark`, `browse`, `careful`, `cso`, `guard`, `learn`, `pair-agent`, `plan-ceo-review`, `plan-design-review`, `plan-devex-review`, `plan-eng-review`, `plan-tune`, `review` | Master agent planning, safety guardrails, peer review loops, and autonomous strategy. |

### 🛡️ Compliance & Security Auditing

To guarantee reliability and secure execution under Windows 11, this repository utilizes an automated static audit pipeline powered by the **`gs:maintainer-auditor`** skill. All generated compliance records are stored transparently in the [/reports](reports/) directory.

Key audit checkpoints include:

- **Bashism Detection:** Scans all python/powershell scripts to eliminate incompatible Unix operators and shell commands.
- **Path Verification:** Hardens file actions against absolute Unix paths, ensuring proper Windows filesystem syntax.
- **Codex Security Leak Prevention:** Scans codebase recursively for hardcoded secrets, passwords, or API keys.
- **Line Ending Standards:** Verifies CRLF integrity across all PowerShell scripts.

### 🛠 Installation

```powershell
.\setup.ps1
```

### 🗺️ Roadmap 2026

- **Q2 2026 (Enhance Core):** Add more hardened PowerShell-native system diagnostics tools; achieve broader test coverage for path resolution across multiple Windows drives.
- **Q3 2026 (Codex Integration):** Build native Codex-assisted PR review & release checklist pipelines optimized specifically for Windows maintainer environments.
- **Q4 2026 (Telemetry & Auditing):** Implement local telemetry dashboards to track agent tool-calling performance and API token spend directly on Windows.

### 📜 Changelog

- **v1.2.0 (2026-05-31):** Hardened Plus release. Ported 12 new high-value/infrastructure skills (`scrape`, `skillify`, `spec`, `make-pdf`, `document-generate`, etc.), added the automated `gstack-maintainer-auditor` skill for Windows compatibility auditing, integrated visual architecture flowcharts, and set up PowerShell integration tests.
- **v1.0.0 (2026-04-19):** Official stable release. Completed Phase 4 of UD-Re-Suite.
- **v0.9.x (2026-04-14):** Initial compliance audit and Bash-to-Python bridge prototyping.

---

<a name="-tiếng-việt"></a>

## 🇻🇳 Tiếng Việt

### 🌟 Tổng quan

Đây là phiên bản **v1.2.0 "Hardened Plus" (Chính thức)** của hệ sinh thái gstack, được thích ứng chuyên biệt cho Windows 11. Bản port này đánh dấu sự chuyển đổi kiến trúc thực tế từ nguyên bản Unix sang mô hình **Hybrid Orchestration** hiệu suất cao.

- **Tác giả gốc:** [Garry Tan](https://github.com/garrytan)
- **Kho lưu trữ gốc:** [github.com/garrytan/gstack](https://github.com/garrytan/gstack)
- **Phiên bản Port:** `v1.2.0` (Tháng 5, 2026 - Hardened Plus)
- **Nhà duy trì & Định hướng Giáo dục:** Được bảo trì bởi quản trị viên của [Cộng đồng Facebook Bình Dân Học AI](https://www.facebook.com/groups/binhdanhocai), được biết đến rộng rãi như cộng đồng học tập AI lớn nhất Việt Nam với hơn 650.000 thành viên, làm tài liệu tham khảo thực tế cho các luồng vận hành tác nhân AI trên Windows.

### 🌍 Tại sao Công cụ Agent Nguyên bản Windows lại quan trọng

Hầu hết các tác nhân lập trình AI hiện đại (như Claude Code, Aider và các khung agent tùy chỉnh) đều bị thiên lệch sâu sắc về môi trường Unix/Linux. Khi chạy lệnh trên Windows, chúng thường xuyên đưa vào các lệnh Bashisms, phân tích đường dẫn sai hoặc bị lỗi do bất tương thích Shell. `gstack-windows-port` giải quyết trực tiếp khoảng trống hệ sinh thái này bằng cách cung cấp một môi trường hộp cát (sandbox) PowerShell-first đáng tin cậy, đã được tôi luyện và sẵn sàng chạy 49 kỹ năng agent thích ứng Windows, biến Windows 11 thành một môi trường vận hành chuyên biệt và an toàn cho các tác nhân AI.

### 🚀 Đặc sắc kỹ thuật (Tính năng bản Port)

- **Hybrid Orchestration (IEX Pattern):** Sử dụng `python | iex` để vượt qua giới hạn của Windows Shell, thiết kế nhằm cải thiện độ chính xác lệnh.
- **Triết lý Boil the Lake:** Các ràng buộc kiểm tra tính hoàn thiện giúp khuyến khích độ phủ kiểm thử rộng hơn, giảm thiểu các kết quả chưa hoàn tất của tác nhân AI.
- **Surgical Refactor v2.4:** Toàn bộ 49 kỹ năng đã được loại bỏ Bashisms và "Hardened" bằng logic Python.
- **Thực chứng (Reality Grounding):** Xác thực qua Trình duyệt nhờ tích hợp trực tiếp với `browser_agent` của Gemini.

### 📚 Tài liệu Nghiên cứu

Đi sâu vào giải phẫu bản port:

- [Báo cáo Chiến lược (Phong cách McKinsey)](docs/strategic-synthesis-gstack-v2.md)
- [Phân tích Kỹ thuật & Ý đồ Hệ thống](docs/system-intent.md)
- [Phân loại Artifact & Cổng Kiểm soát](docs/repo-artifact-taxonomy.md)
- [Sơ đồ Mạng lưới Kỹ năng (Mindmap)](assets/diagrams/gstack_skill_network_graph.jpg)
- [Báo cáo Kiểm toán Tương thích Windows & Secrets v1.2.0 Tự động](reports/maintainer_audit_report_v1.2.0.md)
- [Tài liệu Hướng dẫn Skill Kiểm toán Maintainer gstack](skills/gstack-maintainer-auditor/SKILL.md)

#### 📊 Sơ đồ Kiến trúc & Vận hành Hệ thống

Dưới đây là các hình ảnh trực quan mô tả kiến trúc lai (hybrid native) và quy trình vận hành của gstack trên Windows 11:

![Hybrid Orchestration Flow](assets/diagrams/visual_1776585736073.jpg)

*Hình 1: Luồng xử lý điều phối lai (Hybrid Orchestration Flow) trên Windows.*

![Surgical Refactor Pipeline](assets/diagrams/visual_1776588424229.jpg)

*Hình 2: Quy trình phẫu thuật tái cấu trúc mã nguồn (Surgical Refactor Pipeline) từ Unix sang Windows.*

![Feature Gate Logic](assets/diagrams/visual_1776591125261.jpg)

*Hình 3: Logic kiểm soát cổng bảo mật (Feature Gate Logic) và an toàn hệ thống.*

### 🛠️ Danh mục Kỹ năng Hoạt động (49 Kỹ năng Hardened)

Để đảm bảo tính minh bạch tối đa, dưới đây là danh sách đầy đủ **49 kỹ năng** đã được port và được bảo vệ bởi các kịch bản kiểm toán tương thích tĩnh trên Windows 11:

| Phân nhóm | Danh sách Kỹ năng | Vai trò / Chức năng |
| :--- | :--- | :--- |
| **Phát triển Cốt lõi & Cào dữ liệu** | `scrape`, `skillify`, `spec`, `document-generate`, `make-pdf` | Cào dữ liệu web, tự động tạo kỹ năng mới, viết đặc tả và xuất báo cáo PDF tự động. |
| **Quản lý Context & Trạng thái** | `context-save`, `context-restore`, `freeze`, `unfreeze` | Lưu trữ trạng thái agent, thiết lập ranh giới đóng băng workspace, phục hồi phiên làm việc. |
| **Hạ tầng & Đồng bộ tri thức** | `setup-gbrain`, `sync-gbrain`, `codex`, `benchmark-models`, `landing-report`, `upgrade` | Thiết lập cơ sở dữ liệu toàn cục, phân tích benchmark, xuất báo cáo landing, cập nhật gstack. |
| **Thiết kế UI/UX & Đánh giá** | `design-consultation`, `design-html`, `design-review`, `design-shotgun`, `devex-review` | Kiểm toán UI/UX cao cấp, tạo mã HTML/CSS tự động, đánh giá trải nghiệm nhà phát triển. |
| **QA & Chẩn đoán hệ thống** | `qa`, `qa-only`, `canary`, `health`, `checkpoint`, `investigate`, `office-hours`, `retro` | Khung kiểm thử tự động, triển khai canary, kiểm tra sức khỏe hệ thống và họp rút kinh nghiệm. |
| **Quy trình Git & Pull Request** | `ship`, `land-and-deploy`, `setup-deploy`, `setup-browser-cookies`, `open-gstack-browser` | Đóng gói commit an toàn, tự động merge & xác thực PR trên production, cấu hình cookie trình duyệt. |
| **Bảo mật & Kiểm toán Hệ thống** | `maintainer-auditor` | Tự động quét kiểm toán tĩnh loại bỏ Bashisms và bảo mật mã nguồn khỏi rò rỉ secret keys. |
| **Điều phối Cốt lõi** | `autoplan`, `benchmark`, `browse`, `careful`, `cso`, `guard`, `learn`, `pair-agent`, `plan-ceo-review`, `plan-design-review`, `plan-devex-review`, `plan-eng-review`, `plan-tune`, `review` | Điều phối lập kế hoạch lớn, thiết lập cổng bảo vệ, cơ chế review chéo và tự động hóa học tập. |

### 🛡️ Kiểm toán & An toàn Hệ thống

Để đảm bảo tính vận hành an toàn tối đa trên Windows 11, repository này tích hợp một quy trình kiểm toán tĩnh tự động được điều phối bởi Skill **`gs:maintainer-auditor`**. Tất cả báo cáo kiểm toán được lưu trữ minh bạch tại thư mục [/reports](reports/).

Các hạng mục kiểm duyệt chính bao gồm:

- **Phát hiện Bashisms:** Quét toàn bộ mã nguồn để loại bỏ các cú pháp Unix bất tương thích trên Windows.
- **Kiểm tra Đường dẫn:** Đảm bảo toàn bộ thao tác tệp tin sử dụng cú pháp thư mục chuẩn PowerShell/Windows.
- **Chống lộ lọt Secrets (Codex Security):** Quét đệ quy phát hiện và ngăn chặn việc gán cứng các API keys nhạy cảm trong mã nguồn.
- **Định dạng xuống dòng:** Xác thực chuẩn CRLF trên toàn bộ các tệp kịch bản PowerShell.

### 🛠 Cài đặt

```powershell
.\setup.ps1
```

### 🗺️ Lộ trình Phát triển 2026 (Roadmap)

- **Quý 2/2026 (Củng cố Cốt lõi):** Bổ sung thêm các công cụ chẩn đoán hệ thống thuần PowerShell; hướng tới mở rộng độ phủ kiểm thử việc phân tích đường dẫn trên các ổ đĩa Windows.
- **Quý 3/2026 (Tích hợp Codex):** Xây dựng các luồng PR review và release checklist tự động qua Codex, được tối ưu riêng cho môi trường bảo trì trên Windows.
- **Quý 4/2026 (Giám sát & Đo lường):** Triển khai bảng điều khiển giám sát cục bộ (local telemetry) để theo dõi hiệu năng gọi tool của agent và chi phí API token trực tiếp trên Windows.

### 📜 Nhật ký thay đổi (Changelog)

- **v1.2.0 (2026-05-31):** Bản phát hành Hardened Plus. Port hàng loạt 12 kỹ năng mới (`scrape`, `skillify`, `spec`, `make-pdf`...), triển khai Skill kiểm toán tự động `gstack-maintainer-auditor` phát hiện Bashisms & API secrets, tích hợp các sơ đồ trực quan và cài đặt hệ thống kịch bản kiểm thử PowerShell.
- **v1.0.0 (2026-04-19):** Phát hành bản ổn định chính thức. Hoàn tất Giai đoạn 4 của UD-Re-Suite.
- **v0.9.x (2026-04-14):** Kiểm toán tuân thủ ban đầu và thử nghiệm Bridge Bash-to-Python.

---

*Developed & Refined by Uncle Dao Reverse Engineering Suite - 2026*
