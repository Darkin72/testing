# Trình tính phí vận chuyển - Bài tập Kiểm thử (V2)

Đây là bản triển khai chính thức mã nguồn Python dựa theo các tham số mới nhất của bài toán **Hệ thống tính phí vận chuyển**. Project bao gồm cả thiết kế test chuẩn hóa áp dụng các kiểm thử thiết yếu từ lý thuyết Kiểm thử Hộp Đen: **Boundary Value Analysis (BVA)** & **Decision Table Testing**.

## 📁 Cấu trúc dự án

- `shipping_calculator.py`: Logic cốt lõi tính toán phí vận chuyển sử dụng chính xác 3 tham số đầu vào (`distance_km`, `weight_kg`, và `customer_type`).
- `test_shipping_calculator.py`: Bộ test Pytest chứa list toàn bộ các Test Cases, bao gồm test exception, logic miễn phí, và BVA checks.
- `docs/boundary_value_analysis.md`: Bảng kỹ thuật khảo sát các điểm biên trên giới hạn của số thực (Khoảng cách & Khối lượng).
- `docs/decision_table.md`: Bảng tham khảo thể hiện tập hợp các quy tắc giao miễn phí và tổ hợp phí vận chuyển thông thường.
- `quest.md`: Yêu cầu bài toán ban đầu (Mới).

## 🚀 Tính năng

Việc tính toán mức phí vận chuyển áp dụng như sau:

1. **Phí cơ bản:** Tính dựa trên mốc khoảng cách giao (`<=5km`: 15k, `5->10km`: 20k, `>10km`: 30k).
2. **Phụ phí khối lượng:** Tính thêm nếu hàng nặng hơn quy định (`>2kg`: 20k, `<=`2kg: 0 VND).
3. **Chiết khấu loại K/hàng:** Áp dụng `-10%` vào tổng chi phí gốc cho `VIP`. `NORMAL` chịu tối đa 100%.
4. **Miễn chi phí hoàn toàn:** Miễn phí trọn vẹn (Final = 0VND) nếu khách là loại `VIP`, kèm `khoảng cách ≤ 5 km`, và `khối lượng ≤ 2 kg`.

## 💻 Cài đặt & Sử dụng

1. **Yêu cầu hệ thống:** Có cài sẵn **Python 3.8+**
2. **Setup trình Test `pytest`:**
   ```bash
   pip install pytest
   ```
3. **Thực thi:**
   Chạy lệnh terminal sau để xác thực sự logic giữa codebase và design specifications:
   ```bash
   pytest -v
   ```
