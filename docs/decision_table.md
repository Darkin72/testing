# Bảng Quyết định (Decision Table)

Giả sử input đều là hợp lệ (Valid Input). Bài toán quy định **Miễn phí vận chuyển** cho khách hàng đặc thù dựa vào 3 điều kiện đồng thời. Khách VIP cũng nhận được chiết khấu `10%` áp dụng lên tổng (Base + Surcharge) cho quy tắc thông thường.

## DT1: Quy tắc Miễn phí (Free Shipping Override)

| Rule                      | DT1          | DT2                   | DT3                   | DT4                   |
| ------------------------- | ------------ | --------------------- | --------------------- | --------------------- |
| Khách hàng là `VIP`       | T            | T                     | T                     | T                     |
| Khoảng cách ≤ 5 km        | T            | T                     | F                     | T                     |
| Khối lượng ≤ 2 kg         | T            | F                     | T                     | T                     |
| Customer != VIP           | F            | F                     | F                     | T                     |
| **Kết quả Phí cuối cùng** | **0** (Free) | Tính theo Rule thường | Tính theo Rule thường | Tính theo Rule thường |

## DT2: Bảng đại diện cấu hình hệ thống tính phí thông thường

Công thức bên dưới tính toán logic theo Base Fee (`BF`), Surcharge (`SC`) và Discount (`DC`).
Tổng kết hợp các điều kiện hợp lệ là: 3 khoảng cách × 2 khoảng cân nặng × 2 loại KH = **12 trường hợp**.

Dưới đây chỉ ra mẫu đại diện tương trưng cho từng nhánh trong bảng quyết định:

| ID  | Dải khoảng cách (BF) | Dải khối lượng (SC) | Customer Type | Quy định áp dụng (`(BF+SC)*DC`) | Kết quả (Fee) |
| --- | -------------------- | ------------------- | ------------- | ------------------------------- | ------------- |
| R1  | d ≤ 5 (15k)          | w ≤ 2 (0k)          | NORM          | (15k + 0) \* 1.0                | 15,000        |
| R2  | d ≤ 5 (15k)          | w > 2 (20k)         | VIP           | (15k + 20k) \* 0.9              | 31,500        |
| R3  | 5 < d ≤ 10 (20k)     | w ≤ 2 (0k)          | VIP           | (20k + 0) \* 0.9                | 18,000        |
| R4  | 5 < d ≤ 10 (20k)     | w > 2 (20k)         | NORM          | (20k + 20k) \* 1.0              | 40,000        |
| R5  | d > 10 (30k)         | w ≤ 2 (0k)          | VIP           | (30k + 0) \* 0.9                | 27,000        |
| R6  | d > 10 (30k)         | w > 2 (20k)         | NORM          | (30k + 20k) \* 1.0              | 50,000        |
