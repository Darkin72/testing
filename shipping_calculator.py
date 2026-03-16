def calculate_shipping_fee(distance_km, weight_kg, customer_type):
    # Validate inputs
    if distance_km < 0 or weight_kg < 0:
        return "INVALID_INPUT"
    if customer_type not in ["NORMAL", "VIP"]:
        return "INVALID_INPUT"

    # Free shipping rule
    if customer_type == "VIP" and distance_km <= 5 and weight_kg <= 2:
        return 0

    # 1. Base fee (Distance)
    if distance_km <= 5:
        base_fee = 15000
    elif distance_km <= 10:
        base_fee = 20000
    else:
        base_fee = 30000

    # 2. Weight surcharge
    if weight_kg <= 2:
        surcharge = 0
    else:
        surcharge = 20000

    # Calculate subtotal
    subtotal = base_fee + surcharge

    # 3. Apply customer discount
    if customer_type == "VIP":
        discount = 0.1
    else:
        discount = 0.0

    final_fee = subtotal * (1 - discount)
    return int(final_fee)
