# Shipping Fee Calculator – Testing Exercise

## 1. Overview

This project defines a **shipping fee calculation system** for a delivery service.
The purpose of this exercise is to practice **black-box testing techniques**, including:

- Decision Table Testing
- Boundary Value Analysis

Students are required to implement the system and design test cases based on the provided rules.

---

# 2. Problem Description

Create a program that calculates the **shipping fee** for a delivery order.

The shipping cost depends on three parameters:

- distance between the warehouse and the customer
- weight of the package
- customer type

The program must return the **final shipping fee in Vietnamese Dong (VND).**

---

# 3. Input Parameters

The system receives the following inputs:

| Parameter     | Description                             | Data Type | Unit |
| ------------- | --------------------------------------- | --------- | ---- |
| distance_km   | Distance between warehouse and customer | Float     | Km   |
| weight_kg     | Weight of the package                   | Float     | Kg   |
| customer_type | Type of customer (NORMAL, VIP)          | String    |      |

---

# 4. Output

The system must return **one integer value**:

```
final_shipping_fee
```

The value represents the shipping fee in **Vietnamese Dong (VND)**.

---

# 5. Shipping Fee Calculation Rules

The final shipping fee is determined through the following steps:

1. Determine the **base fee based on distance**
2. Add **weight surcharge**
3. Apply **customer discount**
4. Check for **free shipping condition**

---

# 6. Base Fee (Distance)

The base shipping fee depends on the delivery distance.

| Distance             | Base Fee (VND) |
| -------------------- | -------------- |
| distance ≤ 5 km      | 15000          |
| 5 < distance ≤ 10 km | 20000          |
| distance > 10 km     | 30000          |

---

# 7. Weight Surcharge

Additional cost may apply depending on package weight.

| Weight        | Surcharge (VND) |
| ------------- | --------------- |
| weight ≤ 2 kg | 0               |
| weight > 2 kg | 20000           |

---

# 8. Customer Discount

Some customers receive a discount.

| Customer Type | Discount |
| ------------- | -------- |
| NORMAL        | 0%       |
| VIP           | 10%      |

The discount is applied **after the base fee and weight surcharge are added**.

---

# 9. Free Shipping Condition

Shipping is **free** when all of the following conditions are satisfied:

- Customer type is **VIP**
- distance ≤ 5 km
- weight ≤ 2 kg

If all three conditions are met:

```
final_shipping_fee = 0
```

---

# 10. Input Constraints

Valid input ranges:

```
distance_km ≥ 0
weight_kg ≥ 0
```

Customer type must be one of the following:

```
NORMAL
VIP
```

Invalid inputs should return:

```
INVALID_INPUT
```

Examples of invalid inputs:

- negative distance
- negative weight
- unsupported customer type

---

# 11. Example Calculation

### Example 1

Input

```
distance = 7 km
weight = 1 kg
customer = NORMAL
```

Base fee = 20000
Weight surcharge = 0

Final fee

```
20000
```

---

### Example 2

Input

```
distance = 3 km
weight = 3 kg
customer = VIP
```

Base fee = 15000
Weight surcharge = 20000

Subtotal

```
35000
```

VIP discount (10%)

```
35000 × 0.9 = 31500
```

Final fee

```
31500
```

---

### Example 3 (Free Shipping)

Input

```
distance = 3 km
weight = 1 kg
customer = VIP
```

Conditions satisfied:

- VIP customer
- distance ≤ 5
- weight ≤ 2

Result

```
final_shipping_fee = 0
```

---

# 12. Required Implementation

Implement the following function:

```
calculate_shipping_fee(
    distance_km,
    weight_kg,
    customer_type
)
```

The function must return the **final shipping fee in VND**.

---

# 13. Testing Tasks

Students must test the system using **black-box testing techniques**.

---

## 13.1 Decision Table Testing

Construct a **decision table** based on:

- distance ranges
- weight ranges
- customer types
- free shipping condition

Generate test cases that cover all decision rules.

---

## 13.2 Boundary Value Analysis

Identify important boundary values.

### Distance boundaries

```
5 km
10 km
```

Example boundary tests:

```
4.9
5
5.1
9.9
10
10.1
```

---

### Weight boundaries

```
2 kg
```

Example boundary tests:

```
1.9
2
2.1
```

---

# 14. Expected Deliverables

The final submission should include:

1. Source code implementation
2. Decision table
3. Designed test cases
4. Test execution results
5. Bug report (if any)

---

# 15. Purpose of the Exercise

This exercise helps students understand how to apply **systematic test design techniques** to verify the correctness of a software system.

It demonstrates how **decision tables and boundary value testing** can be used to ensure that a system behaves correctly under different input conditions.
