# Shipping Fee Calculator – Testing Exercise

## 1. Overview

This project defines a **shipping fee calculation system** for an e-commerce platform.
The purpose of this exercise is to practice **black-box testing techniques**, specifically:

- Decision Table Testing
- Boundary Value Analysis

Students must implement the system and then design test cases using these techniques.

---

# 2. Problem Description

Create a program that calculates the **final shipping fee** for an order based on the following inputs:

Input parameters:

- `distance_km` : distance between warehouse and customer
- `weight_kg` : package weight
- `customer_type` : NORMAL | MEMBER | VIP
- `order_value` : total order value in VND

The program returns:

```
final_shipping_fee
```

---

# 3. Shipping Fee Rules

The shipping fee is calculated in four stages:

1. Base fee (based on distance)
2. Weight surcharge
3. Customer discount
4. Free shipping rule

---

# 4. Base Fee (Distance)

| Distance              | Base Fee |
| --------------------- | -------- |
| distance ≤ 5 km       | 15,000   |
| 5 < distance ≤ 10 km  | 20,000   |
| 10 < distance ≤ 20 km | 30,000   |
| distance > 20 km      | 50,000   |

---

# 5. Weight Surcharge

| Weight            | Surcharge |
| ----------------- | --------- |
| weight ≤ 2 kg     | 0         |
| 2 < weight ≤ 5 kg | 10,000    |
| weight > 5 kg     | 20,000    |

---

# 6. Customer Discount

| Customer Type | Discount |
| ------------- | -------- |
| NORMAL        | 0%       |
| MEMBER        | 10%      |
| VIP           | 20%      |

The discount is applied **after base fee and weight surcharge are added**.

---

# 7. Free Shipping Rule

Free shipping is applied when:

```
order_value ≥ 500000 AND distance ≤ 10 km
```

If this condition is met:

```
final_shipping_fee = 0
```

All other rules are ignored.

---

# 8. Input Constraints

Valid ranges:

```
0 ≤ distance_km ≤ 100
0 ≤ weight_kg ≤ 50
0 ≤ order_value ≤ 10,000,000
```

Invalid inputs should return:

```
INVALID_INPUT
```

Examples of invalid inputs:

- negative values
- unsupported customer type

---

# 9. Example Calculation

Example 1

Input

```
distance = 8 km
weight = 3 kg
customer = MEMBER
order_value = 200000
```

Steps

Base fee = 20,000
Weight surcharge = 10,000

Subtotal

```
30,000
```

Member discount (10%)

```
30,000 × 0.9 = 27,000
```

Final fee

```
27,000
```

---

Example 2

Input

```
distance = 6 km
weight = 4 kg
customer = NORMAL
order_value = 600000
```

Condition

```
order_value ≥ 500000 AND distance ≤ 10
```

Result

```
Free shipping
```

Final fee

```
0
```

---

# 10. Required Implementation

Implement a function:

```
calculate_shipping_fee(
    distance_km,
    weight_kg,
    customer_type,
    order_value
)
```

Return the final shipping fee.

---

# 11. Testing Tasks

Students must perform testing using:

### 1. Decision Table Testing

Construct a decision table based on:

- Free shipping condition
- Distance ranges
- Weight ranges
- Customer types

Generate test cases that cover the decision rules.

---

### 2. Boundary Value Analysis

Identify boundaries for:

Distance

```
5 km
10 km
20 km
```

Weight

```
2 kg
5 kg
```

Order value

```
500000
```

Create boundary test cases such as:

```
4.9
5
5.1
```

```
499999
500000
500001
```

---

# 12. Expected Deliverables

The project submission should include:

1. Source code implementation
2. Decision table
3. Boundary value test cases
4. Test results
5. Bug report (if any)

---

# 13. Suggested Extensions (Optional)

To extend the system later for more advanced testing:

Possible additional rules:

- Surge pricing during peak hours
- Weather surcharge
- Express shipping option
- Promo code discounts

These extensions allow practice with:

- Pairwise testing
- State transition testing
- Combinatorial testing

---
