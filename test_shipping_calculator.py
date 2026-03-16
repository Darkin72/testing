import pytest
from shipping_calculator import calculate_shipping_fee


class TestShippingFeeCalculator:
    # ---------------------------
    # 1. Input Validation Tests
    # ---------------------------
    @pytest.mark.parametrize("distance", [-1, 101])
    def test_invalid_distance(self, distance):
        assert calculate_shipping_fee(distance, 3, "NORMAL", 100000) == "INVALID_INPUT"

    @pytest.mark.parametrize("weight", [-1, 51])
    def test_invalid_weight(self, weight):
        assert calculate_shipping_fee(10, weight, "NORMAL", 100000) == "INVALID_INPUT"

    def test_invalid_customer_type(self):
        assert calculate_shipping_fee(10, 3, "GUEST", 100000) == "INVALID_INPUT"
        assert calculate_shipping_fee(10, 3, 123, 100000) == "INVALID_INPUT"

    @pytest.mark.parametrize("order_val", [-1, 10000001])
    def test_invalid_order_value(self, order_val):
        assert calculate_shipping_fee(10, 3, "NORMAL", order_val) == "INVALID_INPUT"

    # ---------------------------
    # 2. Free Shipping Rule Tests
    # ---------------------------
    def test_free_shipping_conditions(self):
        # order >= 500K AND distance <= 10
        assert calculate_shipping_fee(10, 4, "NORMAL", 500000) == 0
        assert calculate_shipping_fee(5, 10, "VIP", 600000) == 0

    def test_no_free_shipping_if_distance_gt_10(self):
        # order >= 500K BUT distance > 10
        assert calculate_shipping_fee(11, 2, "NORMAL", 500000) != 0

    def test_no_free_shipping_if_order_lt_500k(self):
        # distance <= 10 BUT order < 500K
        assert calculate_shipping_fee(10, 2, "NORMAL", 499999) != 0

    # ---------------------------
    # 3. Boundary Value Analysis & Decision Table Tests
    # ---------------------------

    # Distance boundaries (weight=1, normal, order=0)
    # Expected base fees: <=5(15K), 5-10(20K), 10-20(30K), >20(50K)
    @pytest.mark.parametrize(
        "distance, expected",
        [
            (4.9, 15000),
            (5.0, 15000),
            (5.1, 20000),
            (10.0, 20000),
            (10.1, 30000),
            (20.0, 30000),
            (20.1, 50000),
            (100.0, 50000),  # Max valid distance
        ],
    )
    def test_distance_boundaries(self, distance, expected):
        assert calculate_shipping_fee(distance, 1, "NORMAL", 0) == expected

    # Weight boundaries (dist=11 -> 30K base, normal, order=0)
    # Expected surcharge: <=2(0), 2-5(10K), >5(20K)
    @pytest.mark.parametrize(
        "weight, expected_total",
        [
            (1.9, 30000 + 0),
            (2.0, 30000 + 0),
            (2.1, 30000 + 10000),
            (5.0, 30000 + 10000),
            (5.1, 30000 + 20000),
            (50.0, 30000 + 20000),  # Max valid weight
        ],
    )
    def test_weight_boundaries(self, weight, expected_total):
        assert calculate_shipping_fee(11, weight, "NORMAL", 0) == expected_total

    # Customer discounts (dist=11 -> 30K, weight=3 -> 10K => Subtotal: 40K)
    # Expected: NORMAL(40K), MEMBER(36K), VIP(32K)
    @pytest.mark.parametrize(
        "customer, expected_total",
        [("NORMAL", 40000), ("MEMBER", 36000), ("VIP", 32000)],
    )
    def test_customer_discounts(self, customer, expected_total):
        assert calculate_shipping_fee(11, 3, customer, 0) == expected_total

    # ---------------------------
    # 4. Provided Example Validations
    # ---------------------------
    def test_example_1(self):
        # distance = 8 km, weight = 3 kg, customer = MEMBER, order_value = 200000 -> 27000
        assert calculate_shipping_fee(8, 3, "MEMBER", 200000) == 27000

    def test_example_2(self):
        # distance = 6 km, weight = 4 kg, customer = NORMAL, order_value = 600000 -> 0 (Free shipping)
        assert calculate_shipping_fee(6, 4, "NORMAL", 600000) == 0
