def validate_price(price: int | float) -> int | float:
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise TypeError("Price must be numeric")

    if price < 0:
        raise ValueError("Price cannot be negative")

    return price