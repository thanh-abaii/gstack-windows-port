# gstack Windows 11 Native Port (ud-re-suite)

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
This is the **Official v1.0.0 "Hardened"** release of the gstack skill ecosystem, 100% optimized for Windows 11. This port represents a fundamental architectural shift from the Unix-centric original to a high-performance **Hybrid Orchestration** model.

- **Original Creator:** [Garry Tan](https://github.com/garrytan)
- **Repo Source:** [github.com/garrytan/gstack](https://github.com/garrytan/gstack)
- **Port Version:** `v1.0.0` (April 2026 - Stable)

### 🚀 Technical Highlights (Port Features)
- **Hybrid Orchestration (IEX Pattern):** Utilizes `python | iex` to bypass Windows Shell limitations, ensuring 100% command fidelity.
- **Boil the Lake Philosophy:** Hardcoded completeness checks that force the AI to provide 100% coverage, eliminating "AI Laziness."
- **Surgical Refactor v2.4:** All 37+ skills have been stripped of Bashisms and "Hardened" with Python logic.
- **Reality Grounding:** Mandatory Browser verification using Gemini's native `browser_agent` integration.

### 📚 Research & Documentation
Deep-dive into the port's anatomy:
- [Strategic Synthesis (McKinsey Style)](docs/strategic-synthesis-gstack-v2.md)
- [Technical Deep-Dive & System Intent](docs/system-intent.md)
- [Artifact Taxonomy & Safety Gates](docs/repo-artifact-taxonomy.md)
- [Full Skill Network Graph](docs/gstack_skill_network_graph.jpg)

### 🛠 Installation
```powershell
.\setup.ps1
```

### 📜 Changelog
- **v1.0.0 (2026-04-19):** Official stable release. Completed Phase 4 of UD-Re-Suite.
- **v0.9.x (2026-04-14):** Initial compliance audit and Bash-to-Python bridge prototyping.

---

<a name="-tiếng-việt"></a>
## 🇻🇳 Tiếng Việt

### 🌟 Tổng quan
Đây là phiên bản **v1.0.0 "Hardened" (Chính thức)** của hệ sinh thái gstack, được tối ưu hóa 100% cho Windows 11. Bản port này đánh dấu sự chuyển đổi kiến trúc toàn diện từ nguyên bản Unix sang mô hình **Hybrid Orchestration** hiệu suất cao.

- **Tác giả gốc:** [Garry Tan](https://github.com/garrytan)
- **Kho lưu trữ gốc:** [github.com/garrytan/gstack](https://github.com/garrytan/gstack)
- **Phiên bản Port:** `v1.0.0` (Tháng 4, 2026 - Stable)

### 🚀 Đặc sắc kỹ thuật (Tính năng bản Port)
- **Hybrid Orchestration (IEX Pattern):** Sử dụng `python | iex` để vượt qua giới hạn của Windows Shell, đảm bảo độ chính xác lệnh 100%.
- **Triết lý Boil the Lake:** Các ràng buộc kiểm tra tính hoàn thiện ép AI phải cung cấp giải pháp 100% coverage, triệt tiêu sự lười biếng.
- **Surgical Refactor v2.4:** Toàn bộ 37+ kỹ năng đã được loại bỏ Bashisms và "Hardened" bằng logic Python.
- **Thực chứng (Reality Grounding):** Bắt buộc xác thực qua Trình duyệt nhờ tích hợp trực tiếp với `browser_agent` của Gemini.

### 📚 Tài liệu Nghiên cứu
Đi sâu vào giải phẫu bản port:
- [Báo cáo Chiến lược (Phong cách McKinsey)](docs/strategic-synthesis-gstack-v2.md)
- [Phân tích Kỹ thuật & Ý đồ Hệ thống](docs/system-intent.md)
- [Phân loại Artifact & Cổng Kiểm soát](docs/repo-artifact-taxonomy.md)
- [Sơ đồ Mạng lưới Kỹ năng (Mindmap)](docs/gstack_skill_network_graph.jpg)

### 🛠 Cài đặt
```powershell
.\setup.ps1
```

### 📜 Nhật ký thay đổi (Changelog)
- **v1.0.0 (2026-04-19):** Phát hành bản ổn định chính thức. Hoàn tất Giai đoạn 4 của UD-Re-Suite.
- **v0.9.x (2026-04-14):** Kiểm toán tuân thủ ban đầu và thử nghiệm Bridge Bash-to-Python.

---
*Developed & Refined by Uncle Dao Reverse Engineering Suite - 2026*
