# Decision Table Testing

This decision table captures the combinational logic that applies to the shipping fee calculator. Rather than combining all inputs into one giant matrix, we factor the Free Shipping condition as overriding the subsequent calculations.

## Table 1: Free Shipping Override (Stage 4 check first)

| Condition / Rule                | DT1 | DT2 | DT3 | DT4 |
| ------------------------------- | --- | --- | --- | --- |
| `order_value ≥ 500000`          | T   | T   | F   | F   |
| `distance_km ≤ 10`              | T   | F   | T   | F   |
| **Action**                      |     |     |     |     |
| Applicable for Free Shipping    | Yes | No  | No  | No  |
| Final Fee is 0?                 | Yes | No  | No  | No  |
| Proceeds to regular fee config? | No  | Yes | Yes | Yes |

_If Free Shipping applies, the variables `weight_kg` and `customer_type` do not affect the outcome._

## Table 2: Regular Fee Configuration (When Free Shipping is False)

Since Distance has 4 cases, Weight has 3 cases, and Customer Type has 3 cases, the full logical domain is 4 _ 3 _ 3 = 36 combinations.
Below represents key test scenarios reflecting each rule's execution mathematically:

| Case ID | Distance Range  | Base Fee | Weight Range | Surcharge | Customer | Discount | Final Formula               |
| ------- | --------------- | -------- | ------------ | --------- | -------- | -------- | --------------------------- |
| R1      | d <= 5 (e.g. 4) | 15,000   | w <= 2       | 0         | NORMAL   | 0%       | (15K + 0) \* 1.0 = 15,000   |
| R2      | d <= 5 (e.g. 4) | 15,000   | 2 < w <= 5   | 10,000    | MEMBER   | 10%      | (15K + 10K) \* 0.9 = 22,500 |
| R3      | d <= 5 (e.g. 4) | 15,000   | w > 5        | 20,000    | VIP      | 20%      | (15K + 20K) \* 0.8 = 28,000 |
| R4      | 5 < d <= 10     | 20,000   | w <= 2       | 0         | VIP      | 20%      | (20K + 0) \* 0.8 = 16,000   |
| R5      | 10 < d <= 20    | 30,000   | 2 < w <= 5   | 10,000    | MEMBER   | 10%      | (30K + 10K) \* 0.9 = 36,000 |
| R6      | d > 20          | 50,000   | w > 5        | 20,000    | NORMAL   | 0%       | (50K + 20K) \* 1.0 = 70,000 |

_Note: R4 assumes `order_value < 500,000` since `d <= 10` would trigger Free Shipping if the order value was high._
