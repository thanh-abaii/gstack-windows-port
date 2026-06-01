# Báo cáo Phân tích Vòng đời Agent (Agent Loop) - gstack Windows

**Suite:** Uncle Dao Reverse Engineering Suite
**Version:** v1.2.0 (Hardened Plus)
**Phase:** Execution Model
**Role:** Runtime flow analysis

---

## 1. Điểm khởi đầu (Entry Points)

Mọi kỹ năng gstack trên Windows đều bắt đầu bằng một lệnh bootstrap đồng nhất:
`python "bin/gstack-boot.py" --skill [skill_name] | iex`

- **Nhiệm vụ:** Thiết lập biến môi trường, định nghĩa Alias và khởi tạo ID phiên (Session ID).
- **Cơ chế:** Sử dụng `iex` (Invoke-Expression) của PowerShell để thực thi trực tiếp output từ Python vào session hiện tại.

---

## 2. Vòng lặp Vận hành Chính (Main Runtime Loop)

Vòng lặp không nằm trong một file code duy nhất mà là sự phối hợp giữa:

1.  **Preamble (SKILL.md)**: Thiết lập các quy tắc kiểm soát (`PROACTIVE`, `LAKE_INTRO`).
2.  **Bridge Function (browse_bridge.py)**: Định nghĩa hàm `B` (alias cho Browse).
3.  **Subagent Delegation**: Chuyển giao quyền thực thi cho `browser_agent`.

### Luồng thực thi từ Input đến Action:

`Người dùng gọi /gs:qa` -> `gstack-boot.py (Set Env)` -> `Agent đọc SKILL.md` -> `Agent thực hiện các bước QA` -> `Agent gọi hàm B (Bridge)` -> `Bridge tạo Signal` -> `Agent gọi browser_agent` -> `Thực thi trên Browser thực` -> `Kết quả trả về cho Agent chính`.

---

## 3. Các đối tượng Trạng thái (State Objects)

Trạng thái được lưu trữ và truyền đi qua:

- **Biến môi trường**: `_PROACTIVE`, `_SESSION_ID`, `_TEL`, `_EXPLAIN_LEVEL`.
- **Session Files**: Lưu tại `~/.gstack/sessions/` sử dụng PID của PowerShell làm định danh.
- **Marker Files**: `.writing-style-prompted`, `.completeness-intro-seen` để kiểm soát các thông báo "chỉ xuất hiện một lần".

---

## 4. Cơ chế Dừng, Thử lại & Fallback (Stop, Retry, Fallback)

- **Stop**: Dựa trên các check `PROACTIVE` và `LAKE_INTRO`. Nếu người dùng từ chối, Agent sẽ dừng hoặc chuyển sang chế độ manual.
- **Retry/Fallback**: gstack sử dụng nguyên lý **"Boil the Lake"**. Nếu một bước thất bại, nó không chỉ thử lại mà thường mở rộng phạm vi điều tra (ví dụ: gọi `/investigate` nếu QA tìm thấy lỗi).
- **Windows Fallback**: Sử dụng Python REPL và file tạm để tránh các lỗi shell `&&` hay `||` của Windows.

---

## 5. Kết luận & Điểm sáng Kiến trúc

Kiến trúc **"Hybrid Orchestration"** giúp gstack cực kỳ linh hoạt:

- **Tương thích cao**: Dùng Python làm bridge giúp chạy ổn định trên Windows.
- **Tận dụng sức mạnh Subagent**: Không cố gắng code lại browser driver mà tận dụng `browser_agent` có sẵn.
- **Tính cách nhất quán**: Các quy tắc trong `SKILL.md` định hình hành vi (Boil the Lake) rất rõ nét.

**Bước tiếp theo:** Chuyển sang Giai đoạn 1.2: `@visual-storyteller` để vẽ sơ đồ luồng thực thi này.
