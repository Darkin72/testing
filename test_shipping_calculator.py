import pytest
from shipping_calculator import calculate_shipping_fee

class TestShippingFeeCalculator:
    @pytest.mark.parametrize('distance_km, weight_kg, customer_type, expected_output', [
        (3, 1, 'NORMAL', 15000),
        (7, 1, 'NORMAL', 20000),
        (12, 1, 'NORMAL', 30000),
        (3, 3, 'NORMAL', 35000),
        (7, 3, 'NORMAL', 40000),
        (12, 3, 'NORMAL', 50000),
        (3, 1, 'VIP', 0),
        (7, 1, 'VIP', 18000),
        (12, 1, 'VIP', 27000),
        (3, 3, 'VIP', 31500),
        (7, 3, 'VIP', 36000),
        (12, 3, 'VIP', 45000),
    ])
    def test_general_cases(self, distance_km, weight_kg, customer_type, expected_output):
        assert calculate_shipping_fee(distance_km, weight_kg, customer_type) == expected_output

    @pytest.mark.parametrize('distance_km, weight_kg, customer_type, expected_output', [
        (4.9, 1, 'NORMAL', 15000),
        (5, 1, 'NORMAL', 15000),
        (5.1, 1, 'NORMAL', 20000),
        (9.9, 1, 'NORMAL', 20000),
        (10, 1, 'NORMAL', 20000),
        (10.1, 1, 'NORMAL', 30000),
    ])
    def test_distance_boundaries(self, distance_km, weight_kg, customer_type, expected_output):
        assert calculate_shipping_fee(distance_km, weight_kg, customer_type) == expected_output

    @pytest.mark.parametrize('distance_km, weight_kg, customer_type, expected_output', [
        (6, 1.9, 'NORMAL', 20000),
        (6, 2, 'NORMAL', 20000),
        (6, 2.1, 'NORMAL', 40000),
    ])
    def test_weight_boundaries(self, distance_km, weight_kg, customer_type, expected_output):
        assert calculate_shipping_fee(distance_km, weight_kg, customer_type) == expected_output

    @pytest.mark.parametrize('distance_km, weight_kg, customer_type, expected_output', [
        (6, 1, 'NORMAL', 20000),
        (3, 1, 'VIP', 0),
    ])
    def test_customer_type_boundaries(self, distance_km, weight_kg, customer_type, expected_output):
        assert calculate_shipping_fee(distance_km, weight_kg, customer_type) == expected_output
