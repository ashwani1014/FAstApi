
# ==========================================
# PYTHON DATA TRANSFORMATION - ALL SOLUTIONS
# ==========================================


# LEVEL 1: BASIC TRANSFORMATIONS

users = [
    {"id": 1, "name": "  aman ", "age": 22, "is_active": True, "salary": 50000},
    {"id": 2, "name": "RIYA", "age": 17, "is_active": True, "salary": 30000},
    {"id": 3, "name": "karan", "age": 25, "is_active": False, "salary": 60000},
    {"id": 4, "name": "neha ", "age": 21, "is_active": True, "salary": 45000},
]

# Exercise 1: Filter active users
active_users = [
    user for user in users
    if user["is_active"]
]
print("1. Active Users:", active_users)


# Exercise 2: Normalize all user names
names = [
    user["name"].strip().title()
    for user in users
]
print("\n2. Normalized Names:", names)


# Exercise 3: Select specific fields from active users
selected_users = [
    {
        "id": user["id"],
        "name": user["name"].strip().title(),
        "age": user["age"]
    }
    for user in users
    if user["is_active"]
]
print("\n3. Selected Users:", selected_users)


# Exercise 4: Active users aged 18 or above
eligible_users = [
    {
        "id": user["id"],
        "name": user["name"].strip().title()
    }
    for user in users
    if user["is_active"] and user["age"] >= 18
]
print("\n4. Eligible Users:", eligible_users)


# ==========================================
# LEVEL 2: INTERMEDIATE TRANSFORMATIONS
# ==========================================

orders = [
    {"order_id": 101, "user_id": 1, "amount": 1200, "status": "completed"},
    {"order_id": 102, "user_id": 2, "amount": 800, "status": "pending"},
    {"order_id": 103, "user_id": 1, "amount": 2500, "status": "completed"},
    {"order_id": 104, "user_id": 3, "amount": 500, "status": "cancelled"},
]


# Exercise 5: Filter completed orders
completed_orders = [
    order for order in orders
    if order["status"] == "completed"
]
print("\n5. Completed Orders:", completed_orders)


# Exercise 6: Calculate revenue from completed orders
total_revenue = sum(
    order["amount"]
    for order in orders
    if order["status"] == "completed"
)
print("\n6. Total Revenue:", total_revenue)


# Exercise 7: Find unique user IDs
unique_user_ids = {
    order["user_id"]
    for order in orders
}
print("\n7. Unique User IDs:", unique_user_ids)


# Exercise 8: Create order lookup dictionary
orders_by_id = {
    order["order_id"]: order
    for order in orders
}
print("\n8. Orders By ID:", orders_by_id)


# Exercise 9: High-value completed orders
high_value_orders = [
    order for order in orders
    if order["status"] == "completed"
    and order["amount"] > 1000
]
print("\n9. High-Value Orders:", high_value_orders)


# ==========================================
# LEVEL 3: PRODUCTION-STYLE TRANSFORMATION
# ==========================================

# Exercise 10: Reusable user response function

def prepare_user_response(users: list[dict]) -> list[dict]:
    """
    Return active adult users with selected, normalized fields.
    Does not modify the original user dictionaries.
    """
    result = []

    for user in users:
        if user["is_active"] and user["age"] >= 18:
            result.append({
                "id": user["id"],
                "name": user["name"].strip().title(),
                "age": user["age"]
            })

    return result


api_response = prepare_user_response(users)

print("\n10. Production-Style API Response:", api_response)
