# Báo cáo Phân tích Build Pipeline & Surgical Refactor - gstack

**Suite:** Uncle Dao Reverse Engineering Suite
**Version:** v1.1
**Phase:** Ground Truth
**Role:** Build-system and shipped-surface analysis

---

## 1. Điểm khởi đầu (Build Entrypoints)

gstack không có một quy trình build CI/CD truyền thống kiểu "compile once, ship everywhere". Thay vào đó, nó sử dụng:

- **`setup` (Entrypoint chính):** Một script Bash thực hiện mọi việc từ cài đặt phụ thuộc, biên dịch binary đến "phẫu thuật" mã nguồn để tương thích với máy chủ đích (host).
- **`bin/gstack-boot.py`:** Bridge động thực hiện "refactor" môi trường tại thời điểm thực thi.

---

## 2. Các giai đoạn Pipeline (Stages)

| Giai đoạn | Công cụ | Đầu vào | Đầu ra | Mục đích |
| :--- | :--- | :--- | :--- | :--- |
| **Prepare** | Bash | Flags (`--host`, `--prefix`) | Biến môi trường | Xác định đích đến và sở thích người dùng. |
| **Build** | `bun run build` | `browse/src` | `browse/dist/browse` | Biên dịch trình duyệt điều khiển từ mã nguồn TypeScript. |
| **Refactor** | `bin/gstack-patch-names` | `SKILL.md` (Original) | `SKILL.md` (Patched) | Sửa đổi frontmatter để đổi tên lệnh theo ý người dùng. |
| **Overlay** | `ln -s` / `mkdir` | Thư mục gstack | `~/.claude/skills/` | Đăng ký kỹ năng vào hệ thống của Agent. |
| **Initialize** | `gstack-session-update` | Git state | `~/.gstack/` | Đồng bộ trạng thái session và thực hiện auto-upgrade. |

---

## 3. Surgical Refactor trên Windows

Do các hạn chế kỹ thuật của Windows (đặc biệt là lỗi xử lý pipe của Bun), gstack thực hiện các điều chỉnh "phẫu thuật" (Surgical Refactor) quan trọng:

- **Node.js Bridge:** Thay thế Bun bằng Node.js khi tương tác với Playwright/Chromium trên Windows.
- **Path Transformation:** Chuyển đổi các đường dẫn kiểu POSIX sang Windows-friendly path trong quá trình khởi động session.

---

## 4. Cơ chế tự sửa lỗi (Self-healing & Recovery)

gstack tích hợp sẵn các cơ chế tự phục hồi trong quá trình build/setup:

- **`gstack-relink`:** Tự động sửa lại các liên kết (links) nếu người dùng lỡ tay xóa hoặc cấu hình bị sai lệch.
- **`确保 Chromium`:** Nếu không thể khởi chạy trình duyệt, `setup` sẽ tự động tải xuống phiên bản Playwright Chromium phù hợp.

---

## 5. Kết luận

Build Pipeline của gstack không chỉ là cài đặt phần mềm; đó là một **hệ thống thích ứng** (Adaptive System). Nó thực hiện "phẫu thuật" ngay trên mã nguồn để đảm bảo trải nghiệm người dùng cuối là mượt mà nhất, bất kể hệ điều hành hay loại Agent nào đang sử dụng.

**Bước tiếp theo:** Chuyển sang Giai đoạn 3.2: `@visual-storyteller` để vẽ sơ đồ quy trình "Phẫu thuật" mã nguồn (Surgical Refactor Pipeline) này.
