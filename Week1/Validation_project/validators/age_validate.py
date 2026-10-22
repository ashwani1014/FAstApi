def validate_age(age: int) -> int:
    if isinstance(age, bool) or not isinstance(age, int):
        raise TypeError("Age must be an integer")

    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120")

    return age