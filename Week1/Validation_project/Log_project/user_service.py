 


import logging

logger = logging.getLogger(__name__)


def register_user(name: str, age: int):
    # Check if age is negative
    if age < 0:
        # Log a warning and raise ValueError
        logger.warning(f"Invalid age: {age}. Age cannot be negative.")
        raise ValueError("Age cannot be negative")

    # Log successful registration at INFO level
    logger.info(f"User '{name}' registered successfully with age {age}.")