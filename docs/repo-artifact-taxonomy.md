# Báo cáo Phân loại Thành phần gstack (Artifact Taxonomy)

**Suite:** Uncle Dao Reverse Engineering Suite
**Version:** v1.1
**Phase:** Ground Truth
**Role:** Xác định nguồn gốc và độ tin cậy của dữ liệu.

---

## 1. Phân loại các lớp Artifact (Artifact Classes)

Dựa trên cấu trúc thực tế, hệ thống gstack được phân thành 5 lớp chính:

| Lớp Artifact | Đặc điểm | Độ tin cậy | Khả năng chỉnh sửa |
| :--- | :--- | :--- | :--- |
| **Authored Source** | Mã nguồn TypeScript, file `.tmpl`, script gốc. | **Tuyệt đối** | Có (Nên sửa ở đây) |
| **Generated Source** | Các file `.md` được sinh ra từ template cho từng nền tảng (Claude, Codex...). | Trung bình | **KHÔNG** (Sẽ bị ghi đè) |
| **Vendor / Third-party** | `node_modules`, các thư viện trong `lib/`. | Cao | Không |
| **Build Outputs** | Thư mục `dist/`, binary đã compile. | Thấp | Không (Xóa/Sinh lại được) |
| **Docs & Analysis** | Tài liệu nghiên cứu trong `docs/`, `CHANGELOG.md`. | Tham khảo | Có |

---

## 2. Bản đồ Thư mục & Tệp tin Quan trọng

| Đường dẫn | Lớp Artifact | Operational Guidance |
| :--- | :--- | :--- |
| `gstack/scripts/` | Authored Source | **Đọc trước**. Chứa logic điều khiển (build, gen-skill). |
| `gstack/SKILL.md.tmpl`| Authored Source | **Source of Truth** cho kỹ năng gstack chính. |
| `gstack/SKILL.md` | Generated Source | **Tránh sửa**. Chỉ dùng để đọc kết quả sau build. |
| `gstack/.agents/`, `.cursor/` | Generated Source | **Ignore**. Chứa bản sao kỹ năng cho từng host. |
| `gstack/browse/src/` | Authored Source | Core logic của Browser Bridge. |
| `gstack/browse/dist/` | Build Output | Bỏ qua khi nghiên cứu logic. |
| `skills/*/SKILL.md` | Authored Source | Source of Truth cho các kỹ năng độc lập. |
| `docs/gstack-research/`| Docs & Analysis | Lưu trữ kết quả nghiên cứu hiện tại. |

---

## 3. Rủi ro gây nhầm lẫn (Confusion Risks)

1.  **Trap: Template Clout**: Sửa nhầm vào `gstack/SKILL.md` thay vì `gstack/SKILL.md.tmpl`. Mọi thay đổi sẽ mất sạch khi chạy `bun run build`.
2.  **Trap: Shadow Skills**: Sửa kỹ năng trong các thư mục ẩn như `.agents/skills/`. Đây chỉ là các bản copy phục vụ runtime cho từng host agent.
3.  **Trap: Dual Root**: Nhầm lẫn giữa kỹ năng gstack core (trong `gstack/`) và kỹ năng mở rộng (trong `skills/`).

---

## 4. Quy tắc Xử lý Khuyến nghị (Handling Rules)

- **Khi muốn thay đổi logic gstack:** Luôn tìm file `.ts` tương ứng trong `src/` hoặc `.tmpl`.
- **Khi nghiên cứu hành vi:** Đọc `SKILL.md.tmpl` để hiểu ý đồ thiết kế, đọc `SKILL.md` để thấy Agent thực sự nhận được gì.
- **Trước khi phân tích sâu:** Chạy `bun run build` (nếu môi trường cho phép) để đảm bảo các tệp generated là mới nhất.

---

## 5. Kết luận & Bước tiếp theo

Hệ thống gstack sử dụng mô hình **"Factory-based Skills"**. Tri thức thực sự nằm ở các template và scripts sinh mã. 

**Bước tiếp theo:** Chuyển sang Giai đoạn 1: `ud-analyze-agent-loop` để xem cách các file "Generated Source" này được Agent tiêu thụ như thế nào trong thực tế.
