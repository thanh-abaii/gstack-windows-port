---
module: gstack-windows-port
date: 2026-04-19
problem_type: best_practice
component: tooling
severity: high
applies_when:
  - "Porting gstack logic to Windows 11 environments"
  - "Handling environment variables in PowerShell sessions"
  - "Replacing legacy browser automation with browser_agent"
tags:
  - windows-11
  - python-bridge
  - shell-injection
  - browser-agent
  - porting
---

# Porting 49 Gstack Skills to Windows Native (Python Bridge)

## Context

49 kỹ năng của hệ sinh thái `gstack` gốc được thích ứng và port hoàn toàn sang môi trường Windows 11. Khi chạy trên Windows 11/PowerShell, các kỹ năng này gặp lỗi nghiêm trọng do cú pháp shell (`&&`, `||`), đường dẫn không hợp lệ (`/tmp`, `~`) và sự thiếu hụt các công cụ như `sed`, `awk`. Cần một giải pháp "Native" để giữ nguyên sức mạnh của gstack mà không phụ thuộc vào Bash.

## Guidance

Sử dụng kiến trúc **Python Bridge** để thay thế lớp "Plumbing" của gstack. Giải pháp này chuyển dịch logic từ shell script sang Python script và sử dụng cơ chế gán biến môi trường động cho PowerShell.

### 1. Unified Bootstrapper (`gstack-boot.py`)

Thay thế khối Preamble Bash (50+ dòng) trong `SKILL.md` bằng một lệnh gọi duy nhất:
`python bin/gstack-boot.py --skill [name] | iex`

- **Cơ chế:** Python tính toán môi trường và in ra mã PowerShell (`$env:VAR = '...'`). Lệnh `iex` (Invoke-Expression) thực thi mã này để nạp biến vào shell cha.
- **Bảo mật:** Luôn escape giá trị bằng hàm `escape_ps()` để chống Shell Injection qua tên nhánh Git hoặc Slug dự án.

### 2. Browser Bridge (`browse_bridge.py`)

Thay vì khởi động binary `browse.exe` cũ (thường lỗi server start trên Windows), sử dụng Bridge để chuyển hướng lệnh `$B` sang **`browser_agent`** của Gemini CLI.

- **Tín hiệu:** In ra `[GS-BRIDGE-SIGNAL] ACTION: Navigate to...` để Agent nhận diện và kích hoạt công cụ browser native.

### 3. Safe Logging (`gstack_utils.py`)

Xử lý lỗi File Lock trên Windows bằng cơ chế retry khi ghi tệp JSONL:

```python
for i in range(retries):
    try:
        with open(file_path, "a") as f: f.write(line)
        return True
    except PermissionError:
        time.sleep(0.2)
```

### 4. Bulk Migration

- Đổi tên kỹ năng sang định danh `gs:<name>` (ví dụ: `gs:health`).
- Cập nhật tất cả tham chiếu chéo (`/ship` -> `/gs:ship`) để đảm bảo tính nhất quán của hệ sinh thái.

## Why This Matters

- **Tính ổn định:** Loại bỏ hoàn toàn lỗi `Unrecognized token` của PowerShell.
- **Tính di động:** Mã nguồn Python chạy tốt trên cả Windows, macOS và Linux.
- **Tận dụng sức mạnh native:** Kết hợp khả năng lập kế hoạch của gstack với "đôi mắt" hiện đại của `browser_agent`.

## When to Apply

- Khi nạp các kỹ năng mới từ hệ sinh thái gstack vào dự án trên Windows.
- Khi cần quản lý biến môi trường xuyên suốt nhiều bước lệnh trong một Turn.

## Examples

### Trước (Unix-only):

```bash
GSTACK_BIN="$GSTACK_ROOT/bin"
_SESSION_ID="$$-$(date +%s)"
$GSTACK_BIN/gstack-config get proactive
```

### Sau (Windows Native):

```bash
python "bin/gstack-boot.py" --skill health | iex
# Biến $_SESSION_ID và $env:GSTACK_BIN đã sẵn sàng trong PowerShell
```

## Related Solutions

- `ud-windows-11-powershell-compatibility.md`: Quy tắc shell cơ bản.
- `_active-gotchas.md`: Các lưu ý quan trọng về Windows 11.
