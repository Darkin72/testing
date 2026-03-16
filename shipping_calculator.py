def calculate_shipping_fee(distance_km, weight_kg, customer_type, order_value):
    # Validate input constraints
    if not (0 <= distance_km <= 100):
        return "INVALID_INPUT"
    if not (0 <= weight_kg <= 50):
        return "INVALID_INPUT"
    if customer_type not in ["NORMAL", "MEMBER", "VIP"]:
        return "INVALID_INPUT"
    if not (0 <= order_value <= 10000000):
        return "INVALID_INPUT"

    # Free Shipping Rule
    if order_value >= 500000 and distance_km <= 10:
        return 0

    # 1. Base Fee (Distance)
    if distance_km <= 5:
        base_fee = 15000
    elif distance_km <= 10:
        base_fee = 20000
    elif distance_km <= 20:
        base_fee = 30000
    else:
        base_fee = 50000

    # 2. Weight Surcharge
    if weight_kg <= 2:
        surcharge = 0
    elif weight_kg <= 5:
        surcharge = 10000
    else:
        surcharge = 20000

    subtotal = base_fee + surcharge

    # 3. Customer Discount
    if customer_type == "MEMBER":
        discount = 0.1
    elif customer_type == "VIP":
        discount = 0.2
    else:
        discount = 0.0

    final_fee = subtotal * (1 - discount)
    return int(final_fee)
