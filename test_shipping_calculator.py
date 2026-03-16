import pytest
from shipping_calculator import calculate_shipping_fee


class TestShippingFeeCalculator:
    # ---------------------------
    # 1. Input Constraints
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
    # 2. Free Shipping Conditions
    # ---------------------------
    def test_free_shipping(self):
        assert calculate_shipping_fee(3, 1, "VIP") == 0
        assert calculate_shipping_fee(5, 2, "VIP") == 0

    def test_no_free_shipping(self):
        assert calculate_shipping_fee(5.1, 2, "VIP") != 0  # wrong dist
        assert calculate_shipping_fee(5, 2.1, "VIP") != 0  # wrong weight
        assert calculate_shipping_fee(5, 2, "NORMAL") != 0  # wrong customer

    # ---------------------------
    # 3. Boundary Value Analysis
    # ---------------------------
    @pytest.mark.parametrize(
        "distance, expected_base",
        [
            (4.9, 15000),
            (5.0, 15000),
            (5.1, 20000),
            (9.9, 20000),
            (10.0, 20000),
            (10.1, 30000),
        ],
    )
    def test_distance_boundaries(self, distance, expected_base):
        # NORMAL, weight=1 -> surchage=0, discount=0
        assert calculate_shipping_fee(distance, 1, "NORMAL") == expected_base

    @pytest.mark.parametrize(
        "weight, expected_total", [(1.9, 30000), (2.0, 30000), (2.1, 50000)]
    )
    def test_weight_boundaries(self, weight, expected_total):
        # distance=11 (base=30000), NORMAL
        assert calculate_shipping_fee(11, weight, "NORMAL") == expected_total

    # ---------------------------
    # 4. Provided Examples Validation
    # ---------------------------
    def test_example_1(self):
        # distance = 7 km, weight = 1 kg, customer = NORMAL -> 20000
        assert calculate_shipping_fee(7, 1, "NORMAL") == 20000

    def test_example_2(self):
        # distance = 3 km, weight = 3 kg, customer = VIP -> 31500
        assert calculate_shipping_fee(3, 3, "VIP") == 31500

    def test_example_3(self):
        # distance = 3 km, weight = 1 kg, customer = VIP -> 0
        assert calculate_shipping_fee(3, 1, "VIP") == 0
