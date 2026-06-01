# Báo cáo Phân tích Bản sắc & Kiểm soát Hành vi (Behavioral Controls) - gstack

**Suite:** Uncle Dao Reverse Engineering Suite
**Version:** v1.2.0 (Hardened Plus)
**Phase:** Behavior Policy
**Role:** Prompt and behavior-control analysis

---

## 1. Triết lý Vận hành: Boil the Lake

gstack được xây dựng trên nguyên lý **"Boil the Lake"** (Nấu cả hồ nước):

- **Nguyên lý Hoàn thiện (Completeness Principle):** Khi AI làm giảm chi phí thực hiện, Agent phải ưu tiên giải pháp toàn diện nhất (100%) thay vì các giải pháp tạm thời hoặc tiết kiệm sức (approaches like "90% is enough").
- **Chỉ dẫn:** "Always do the complete thing."

---

## 2. Bản sắc & Giọng văn (Identity & Voice)

gstack định hình một phong cách Agent rất đặc thù:

- **Vai trò:** Một **Builder** (Người xây dựng), không phải một Consultant (Tư vấn viên).
- **Giọng văn:** Trực tiếp (direct), cụ thể (concrete), sắc sảo (sharp).
- **Cấm kỵ (Avoidance):**
    - Tuyệt đối không dùng phong cách doanh nghiệp (corporate) hay hàn lâm (academic).
    - Cấm dùng từ ngữ "AI Slop": *delve, crucial, robust, comprehensive, nuanced, perspective*.
    - Không dùng gạch ngang dài (`—`), ưu tiên cấu trúc câu ngắn, kết thúc bằng hành động cụ thể.

---

## 3. Các lớp Kiểm soát Hành vi (Control Layers)

### A. Tôn trọng người dùng (User Primacy)

- "The user is right. Always." AI chỉ là người đưa ra tín hiệu (Signal) và khuyến nghị (Recommendation). Quyết định cuối cùng thuộc về người dùng.

### B. Bắt buộc thực thi (Mandatory Execution)

- **Browser Mandate:** Agent không bao giờ được từ chối dùng trình duyệt khi người dùng gọi `/qa`. Mọi lý do như "đã có unit test" đều bị bác bỏ.
- **Never Gate:** Các kỹ năng liên quan đến `security` và `data-migration` luôn được ưu tiên kiểm tra, không được phép bỏ qua các bước kiểm soát an toàn.

### C. An toàn & Bảo mật (Safety Controls)

- **Injection Protection:** Quy tắc nghiêm ngặt về việc không thực thi code hoặc truy cập URL tìm thấy trong nội dung trang web (ngăn chặn prompt injection).
- **Non-blocking Bootstrap:** Các script khởi động phải chạy ngầm, im lặng và tuyệt đối không được gây lỗi làm gián đoạn phiên làm việc.

---

## 4. Chống trích xuất & Bảo vệ danh tính (Anti-Distillation)

- gstack che giấu các logic phức tạp đằng sau các Alias (như hàm `B`) và các biến môi trường có tiền tố `_`.
- Các hướng dẫn trong `SKILL.md` thường đi kèm với các lệnh `touch` hoặc `Remove-Item` để quản lý trạng thái hiển thị của các thông báo hướng dẫn (chỉ hiện một lần).

---

## 5. Kết luận

"Bộ não" của gstack được thiết kế để tạo ra một Agent **quyết đoán, chuyên nghiệp và có trách nhiệm cao**. Nó ép Agent phải thoát khỏi lối mòn "trả lời an toàn" của các mô hình LLM mặc định để trở thành một kỹ sư thực thụ.

**Bước tiếp theo:** Chuyển sang Giai đoạn 2.2: `@visual-storyteller` để minh họa các lớp kiểm soát (Control Layers) này.
