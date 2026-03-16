# Boundary Value Analysis (BVA)

This document contains the Boundary Value Analysis for the main variables in the `calculate_shipping_fee` function. This analysis ensures our test cases adequately cover edge cases exactly AT, slightly BELOW, and slightly ABOVE the logical boundaries defined by the requirements.

## 1. Input Parameter Constraints (Valid vs Invalid)

| Parameter     | Valid Range        | Just Below | Min Val | Normal | Max Val    | Just Above  |
| ------------- | ------------------ | ---------- | ------- | ------ | ---------- | ----------- |
| `distance_km` | 0 ≤ x ≤ 100        | -0.1 (-1)  | 0       | 50     | 100        | 100.1 (101) |
| `weight_kg`   | 0 ≤ x ≤ 50         | -0.1 (-1)  | 0       | 25     | 50         | 50.1 (51)   |
| `order_value` | 0 ≤ x ≤ 10,000,000 | -1         | 0       | 10^5   | 10,000,000 | 10,000,001  |

## 2. Business Logic Boundaries

### Distance (km) Boundaries

The rules dictate steps at `5`, `10`, and `20`.

| Boundary Target | Test Value | Expected Base Fee Classification |
| --------------- | ---------- | -------------------------------- |
| Distance ≤ 5    | 4.9        | ≤ 5 km (15,000)                  |
| Distance ≤ 5    | 5          | ≤ 5 km (15,000)                  |
| 5 < d ≤ 10      | 5.1        | 5 < distance ≤ 10 km (20,000)    |
| 5 < d ≤ 10      | 10         | 5 < distance ≤ 10 km (20,000)    |
| 10 < d ≤ 20     | 10.1       | 10 < distance ≤ 20 km (30,000)   |
| 10 < d ≤ 20     | 20         | 10 < distance ≤ 20 km (30,000)   |
| d > 20          | 20.1       | distance > 20 km (50,000)        |

### Weight (kg) Boundaries

The rules dictate steps at `2` and `5`.

| Boundary Target | Test Value | Expected Surcharge Classification |
| --------------- | ---------- | --------------------------------- |
| weight ≤ 2      | 1.9        | ≤ 2 kg (0)                        |
| weight ≤ 2      | 2          | ≤ 2 kg (0)                        |
| 2 < w ≤ 5       | 2.1        | 2 < weight ≤ 5 kg (10,000)        |
| 2 < w ≤ 5       | 5          | 2 < weight ≤ 5 kg (10,000)        |
| w > 5           | 5.1        | weight > 5 kg (20,000)            |

### Free Shipping Boundaries

Triggered when `order_value ≥ 500000` AND `distance_km ≤ 10`.

| Variable      | Test Value | Rule Satisfaction          | Result Expected         |
| ------------- | ---------- | -------------------------- | ----------------------- |
| `order_value` | 499999     | Not over 500k              | Normal Calculate        |
| `order_value` | 500000     | Matches rule limit exactly | Free (if dist <= 10)    |
| `order_value` | 500001     | Over 500k                  | Free (if dist <= 10)    |
| `distance`    | 9.9        | Less than 10               | Free (if value >= 500k) |
| `distance`    | 10         | Matches rule limit exactly | Free (if value >= 500k) |
| `distance`    | 10.1       | Over 10                    | Normal Calculate        |
