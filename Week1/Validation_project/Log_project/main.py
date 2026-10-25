import logging

from user_service import register_user

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

try:
    register_user("Aman", 500)
    register_user("Riya", 10)

except ValueError as exc:
    # TODO 4: Log the validation failure
    print("yes err", exc)
    logging.error(f"validation failed {exc}")
   