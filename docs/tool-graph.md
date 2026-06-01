# Báo cáo Đồ thị Kết nối Kỹ năng (Tool/Skill Graph) - gstack

**Suite:** Uncle Dao Reverse Engineering Suite
**Version:** v1.2.0 (Hardened Plus)
**Phase:** Execution Model
**Role:** Tool system analysis

---

## 1. Kiến trúc Mạng lưới Kỹ năng (Skill Mesh)

gstack không vận hành như các công cụ rời rạc. Nó là một hệ sinh thái được kết nối thông qua 2 cơ chế chính:

### A. Composable Invocation (`{{INVOKE_SKILL}}`)

Các kỹ năng lớn có thể nạp (inline) nội dung của các kỹ năng nhỏ hơn để tận dụng logic.

- **Ví dụ:** `plan-ceo-review` -> `INVOKE_SKILL:office-hours`.
- **Lợi ích:** Tránh trùng lặp mã nguồn (DRY) và đảm bảo tính nhất quán trong quy trình xử lý.

### B. Proactive Routing (Điều hướng Chủ động)

Preamble của mọi kỹ năng gstack đều chứa "Bảng điều hướng" để chuyển giao nhiệm vụ:

- **Product Ideation** -> `/office-hours`
- **Bug/Error Tracking** -> `/investigate`
- **Quality Assurance** -> `/qa`
- **Deployment/Shipping** -> `/ship`
- **Security/Safety** -> `/guard` hoặc `/careful`

---

## 2. Phân nhóm Kỹ năng (Capability Groups)

Dựa trên phân tích, 37+ kỹ năng được chia thành các nhóm chức năng:

| Nhóm | Kỹ năng tiêu biểu | Rủi ro | Đặc điểm |
| :--- | :--- | :--- | :--- |
| **Strategy & Planning** | `plan-ceo-review`, `office-hours` | Thấp | Tập trung vào tư duy và thiết kế. |
| **Quality & QA** | `qa`, `qa-only`, `design-review` | Trung bình | Sử dụng trình duyệt để xác thực. |
| **Debug & Investigate** | `investigate`, `health` | Trung bình | Truy tìm nguyên nhân gốc rễ. |
| **Execution & Shipping**| `ship`, `land-and-deploy` | **Cao** | Tương tác với Git, PR, và Production. |
| **Safety & Control** | `guard`, `careful`, `freeze` | Thấp | Thiết lập rào chắn và bảo vệ hệ thống. |
| **Creative & Design** | `design-shotgun`, `design-html` | Thấp | Sinh mã UI và trực quan hóa ý tưởng. |

---

## 3. Các cổng kiểm soát (Safety Gates)

- **Sensitive Flag**: Các kỹ năng `sensitive: true` yêu cầu xác nhận rõ ràng từ người dùng, không được tự động thực thi bởi các "Factory Droids".
- **Proactive Toggle**: Người dùng có thể tắt tính năng điều hướng chủ động qua `gstack-config set proactive false`.

---

## 4. Kết luận

Đồ thị kỹ năng của gstack là một mạng lưới **tự điều hướng (self-routing)**. Nó biến Agent từ một người thực thi lệnh đơn lẻ thành một "Quản lý dự án" biết khi nào cần gọi chuyên gia nào.

**Bước tiếp theo:** Chuyển sang Giai đoạn 1.4: `@visual-storyteller` để vẽ đồ thị kết nối (Tool Graph) giữa các nhóm kỹ năng này.
