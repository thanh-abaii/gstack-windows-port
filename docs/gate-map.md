# Báo cáo Bản đồ Cổng kiểm soát (Feature Gate Map) - gstack

**Suite:** Uncle Dao Reverse Engineering Suite
**Version:** v1.1
**Phase:** Control Plane
**Role:** Gate discovery and classification

---

## 1. Cơ chế Lưu trữ & Truy xuất

gstack quản lý các cổng kiểm soát thông qua:

- **Cấu hình tĩnh:** `~/.gstack/config.yaml` (Quản lý bởi `gstack_config.py`).
- **Trạng thái runtime:** Các biến môi trường có tiền tố `_` (Gán bởi `gstack-boot.py`).
- **Marker Files:** Các tệp tin ẩn trong `~/.gstack/` (ví dụ `.completeness-intro-seen`).

---

## 2. Ma trận Cổng kiểm soát (Gate Matrix)

| Tên Gate | Phạm vi | Điều khiển | Logic Phản ứng |
| :--- | :--- | :--- | :--- |
| **`PROACTIVE`** | Runtime | Tự động gợi ý/điều hướng. | Nếu `true`: Dùng Skill tool. Nếu `false`: Trả lời ad-hoc. |
| **`LAKE_INTRO`** | One-time | Chào mừng người dùng mới. | Nếu chưa thấy: In thông báo "Boil the Lake". |
| **`TEAM_MODE`** | Workspace | Tính năng cộng tác. | Nếu `1`: Kích hoạt code review đồng cấp, git-hooks. |
| **`SKILL_PREFIX`**| Persona | Tên lệnh (Namespacing). | Nếu `true`: Dùng `/gstack-qa`. Nếu `false`: Dùng `/qa`. |
| **`EXPLAIN_LEVEL`**| Voice | Độ chi tiết của giọng văn. | `terse` (ngắn gọn) vs `default` (hỗ trợ). |
| **`TELEMETRY`** | Logistics | Thu thập dữ liệu sử dụng. | `on` vs `off`. Không gửi mã nguồn/đường dẫn file. |

---

## 3. Các loại Gate đặc biệt

### A. One-way Doors (Sensitive Gates)

Các kỹ năng như `ship`, `land-and-deploy`, `guard` được coi là các "One-way Doors" (cửa một chiều). gstack yêu cầu xác nhận của người dùng ngay cả khi `PROACTIVE` đang bật.

### B. Progression Gates

gstack sử dụng các marker files để theo dõi lộ trình học của người dùng:

- `.writing-style-prompted`
- `.completeness-intro-seen`
- `.telemetry-prompted`

---

## 4. Kết luận

Hệ thống Gate của gstack được thiết kế để **giảm thiểu sự phiền toái** (Onboarding mượt mà) nhưng vẫn giữ được sự **an toàn và kiểm soát** (User Primacy). Nó chuyển đổi Agent từ trạng thái "trắng" ban đầu sang trạng thái "chuyên gia được cấu hình" theo sở thích của người dùng.

**Bước tiếp theo:** Chuyển sang Giai đoạn 2.4: `@visual-storyteller` để vẽ sơ đồ các cổng điều hướng (Feature Gates) này.
