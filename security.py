COMMON_PASSWORDS = {
    "password",
    "123456",
    "12345678",
    "qwerty",
    "password123",
    "admin",
}


def calculate_score(length, has_uppercase, has_lowercase, has_number, has_special):
    score = 0
    score += length >= 8
    score += has_uppercase
    score += has_lowercase
    score += has_number
    score += has_special
    return int(score)


def get_strength(score):
    if score <= 2:
        return "WEAK"
    if score == 3:
        return "MODERATE"
    if score == 4:
        return "STRONG"
    return "VERY STRONG"


def get_security_level(score):
    # Kept aligned with the strength scale so the report is not contradictory.
    if score <= 2:
        return "LOW"
    if score == 3:
        return "MODERATE"
    if score == 4:
        return "HIGH"
    return "VERY HIGH"


def check_common_password(password):
    return password.lower() in COMMON_PASSWORDS
