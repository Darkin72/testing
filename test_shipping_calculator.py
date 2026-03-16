import pytest
from shipping_calculator import calculate_shipping_fee


class TestShippingFeeCalculator:
    # ---------------------------
    # Các test case xử lý ngoại lệ cơ bản
    # ---------------------------
    def test_invalid_distance(self):
        assert calculate_shipping_fee(-1, 2, "NORMAL") == "INVALID_INPUT"

    def test_invalid_weight(self):
        assert calculate_shipping_fee(5, -1, "NORMAL") == "INVALID_INPUT"

    def test_invalid_customer(self):
        assert calculate_shipping_fee(5, 2, "GUEST") == "INVALID_INPUT"
        assert calculate_shipping_fee(5, 2, 123) == "INVALID_INPUT"

    def test_valid_zero_inputs(self):
        assert calculate_shipping_fee(0, 0, "NORMAL") == 15000
        assert calculate_shipping_fee(0, 0, "VIP") == 0

    # ---------------------------
    # 2.1.3 Test case chung
    # ---------------------------
    @pytest.mark.parametrize(
        "distance_km, weight_kg, customer_type, expected_output",
        [
            (3, 1, "NORMAL", 15000),
            (7, 1, "NORMAL", 20000),
            (12, 1, "NORMAL", 30000),
            (3, 3, "NORMAL", 35000),
            (7, 3, "NORMAL", 40000),
            (12, 3, "NORMAL", 50000),
            (3, 1, "VIP", 0),
            (7, 1, "VIP", 18000),
            (12, 1, "VIP", 27000),
            (3, 3, "VIP", 31500),
            (7, 3, "VIP", 36000),
            (12, 3, "VIP", 45000),
        ],
    )
    def test_general_cases(
        self, distance_km, weight_kg, customer_type, expected_output
    ):
        assert (
            calculate_shipping_fee(distance_km, weight_kg, customer_type)
            == expected_output
        )

    # ---------------------------
    # 2.2 Phương pháp giá trị biên
    # ---------------------------

    # 2.2.1 Giá trị biên của khoảng cách
    @pytest.mark.parametrize(
        "distance_km, weight_kg, customer_type, expected_output",
        [
            (4.9, 1, "NORMAL", 15000),
            (5, 1, "NORMAL", 15000),
            (5.1, 1, "NORMAL", 20000),
            (9.9, 1, "NORMAL", 20000),
            (10, 1, "NORMAL", 20000),
            (10.1, 1, "NORMAL", 30000),
        ],
    )
    def test_distance_boundaries(
        self, distance_km, weight_kg, customer_type, expected_output
    ):
        assert (
            calculate_shipping_fee(distance_km, weight_kg, customer_type)
            == expected_output
        )

    # 2.2.2 Giá trị biên của trọng lượng
    @pytest.mark.parametrize(
        "distance_km, weight_kg, customer_type, expected_output",
        [
            (6, 1.9, "NORMAL", 20000),
            (6, 2, "NORMAL", 20000),
            (6, 2.1, "NORMAL", 40000),
        ],
    )
    def test_weight_boundaries(
        self, distance_km, weight_kg, customer_type, expected_output
    ):
        assert (
            calculate_shipping_fee(distance_km, weight_kg, customer_type)
            == expected_output
        )

    # 2.2.3 Giá trị biên của loại khách hàng
    @pytest.mark.parametrize(
        "distance_km, weight_kg, customer_type, expected_output",
        [
            (6, 1, "NORMAL", 20000),
            (3, 1, "VIP", 0),
        ],
    )
    def test_customer_type_boundaries(
        self, distance_km, weight_kg, customer_type, expected_output
    ):
        assert (
            calculate_shipping_fee(distance_km, weight_kg, customer_type)
            == expected_output
        )
