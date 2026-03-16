# Phân tích giá trị biên (Boundary Value Analysis)

Bài toán yêu cầu phân tích các giá trị biên quan trọng trên số thực của khoảng cách (`distance_km`) và khối lượng (`weight_kg`).

## 1. Giới hạn tham số

- `distance_km` ≥ 0. Giá trị kiểm thử: `-0.1` (Invalid), `0` (Valid).
- `weight_kg` ≥ 0. Giá trị kiểm thử: `-0.1` (Invalid), `0` (Valid).
- Loại khách hàng được chấp nhận: `NORMAL`, `VIP`. Bất kỳ giá trị nào khác (ví dụ: `GUEST`) đều trả về lỗi `INVALID_INPUT`.

## 2. Các điểm biên sinh phí (Logic Boundaries)

### Theo từng Khoảng cách (Base Fee)

Khoảng cách có lợi mức thay đổi tại `5 km` và `10 km`. Khởi tạo các điểm khảo sát liền kề:

| Mục tiêu biên     | Giá trị test | Kỳ vọng phân loại    | Phí cơ bản |
| ----------------- | ------------ | -------------------- | ---------- |
| distance ≤ 5      | 4.9          | ≤ 5 km               | 15,000     |
| distance ≤ 5      | 5.0          | ≤ 5 km               | 15,000     |
| 5 < distance ≤ 10 | 5.1          | 5 < distance ≤ 10 km | 20,000     |
| 5 < distance ≤ 10 | 9.9          | 5 < distance ≤ 10 km | 20,000     |
| 5 < distance ≤ 10 | 10.0         | 5 < distance ≤ 10 km | 20,000     |
| distance > 10     | 10.1         | distance > 10 km     | 30,000     |

### Theo số Khối lượng (Weight Surcharge)

Khối lượng bị áp phụ phí nhảy vọt mức `2 kg`. Khởi tạo các điểm khảo sát:

| Mục tiêu biên | Giá trị test | Kỳ vọng phân loại | Phụ phí |
| ------------- | ------------ | ----------------- | ------- |
| weight ≤ 2    | 1.9          | ≤ 2 kg            | 0       |
| weight ≤ 2    | 2.0          | ≤ 2 kg            | 0       |
| weight > 2    | 2.1          | > 2 kg            | 20,000  |
