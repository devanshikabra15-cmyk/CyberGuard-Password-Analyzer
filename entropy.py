import math


def calculate_entropy(password):
    """Estimate password entropy from its character-set size."""
    if not password:
        return 0.0

    charset_size = 0

    if any(char.islower() for char in password):
        charset_size += 26
    if any(char.isupper() for char in password):
        charset_size += 26
    if any(char.isdigit() for char in password):
        charset_size += 10
    if any(not char.isalnum() for char in password):
        charset_size += 32

    if charset_size == 0:
        return 0.0

    return len(password) * math.log2(charset_size)


def get_entropy_level(entropy):
    if entropy < 40:
        return "LOW"
    if entropy < 60:
        return "MODERATE"
    return "HIGH"
