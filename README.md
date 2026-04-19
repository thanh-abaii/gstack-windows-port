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
This is a **"Hardened"** version of the gstack skill ecosystem, 100% optimized for Windows 11 and PowerShell. The "Plumbing" layer has been migrated from Unix Bash to a native Python Bridge.

- **Original Creator:** [Garry Tan](https://github.com/garrytan)
- **Repo Source:** [github.com/garrytan/gstack](https://github.com/garrytan/gstack)
- **Port Version:** `v1.1.2.1` (April 2026)

### 🚀 Key Features
- **Python-Native Preamble:** Replaces 50+ lines of complex Bash with an efficient Python bootstrapper.
- **PowerShell Injection:** Seamlessly injects environment variables into active sessions using `iex`.
- **Browser Bridge:** Integrated with Gemini's `browser_agent`, bypassing unstable Windows binaries.
- **Safe Logging:** Reliable JSONL logging with retry logic for Windows file locking.

### 🛠 Installation
Run the following command in PowerShell:
```powershell
# To test the installation without making changes:
.\setup.ps1 -DryRun

# To install:
.\setup.ps1
```

### 📜 Skills List (Prefix `gs:`)
`autoplan`, `health`, `ship`, `review`, `qa`, `investigate`, `browse`, `learn`, `office-hours`, `retro`, `checkpoint`, `canary`, `benchmark`, `guard`, `freeze`, ...

[Top ^](#gstack-windows-11-native-port-ud-re-suite)

---

<a name="-tiếng-việt"></a>
## 🇻🇳 Tiếng Việt

### 🌟 Tổng quan
Đây là phiên bản **"Hardened"** của hệ sinh thái kỹ năng gstack, được tối ưu hóa 100% cho Windows 11 và PowerShell. Toàn bộ lớp "Plumbing" đã được chuyển dịch từ Unix Bash sang Python Bridge native.

- **Tác giả gốc:** [Garry Tan](https://github.com/garrytan)
- **Kho lưu trữ gốc:** [github.com/garrytan/gstack](https://github.com/garrytan/gstack)
- **Phiên bản Port:** `v1.1.2.1` (Tháng 4, 2026)

### 🚀 Tính năng nổi bật
- **Python-Native Preamble:** Thay thế 50+ dòng Bash phức tạp bằng trình khởi động Python hiệu quả.
- **PowerShell Injection:** Nạp biến môi trường mượt mà vào phiên làm việc qua cơ chế `iex`.
- **Browser Bridge:** Tích hợp trực tiếp với `browser_agent` của Gemini, loại bỏ binary cũ lỗi thời.
- **Safe Logging:** Ghi log JSONL tin cậy với cơ chế retry chống lỗi File Lock trên Windows.

### 🛠 Cài đặt
Chạy lệnh sau trong PowerShell:
```powershell
# Chạy thử để kiểm tra môi trường:
.\setup.ps1 -DryRun

# Cài đặt chính thức:
.\setup.ps1
```

### 📜 Danh sách Kỹ năng (Prefix `gs:`)
`autoplan`, `health`, `ship`, `review`, `qa`, `investigate`, `browse`, `learn`, `office-hours`, `retro`, `checkpoint`, `canary`, `benchmark`, `guard`, `freeze`, ...

[Đầu trang ^](#gstack-windows-11-native-port-ud-re-suite)

---
*Developed & Refined by Uncle Dao Reverse Engineering Suite - 2026*
