from dataclasses import dataclass
from entropy import calculate_entropy, get_entropy_level
from security import (
    calculate_score,
    check_common_password,
    get_security_level,
    get_strength,
)
from recommendations import generate_recommendations


@dataclass
class PasswordAnalysis:
    length: int
    has_uppercase: bool
    has_lowercase: bool
    has_number: bool
    has_special: bool
    score: int
    strength: str
    security_level: str
    entropy: float
    entropy_level: str
    common_password: bool
    recommendations: list[str]


class PasswordAnalyzer:
    """Coordinates the different password-security analysis operations."""

    def analyze(self, password: str) -> PasswordAnalysis:
        if not isinstance(password, str):
            raise TypeError("Password must be text.")

        if password == "":
            raise ValueError("Password cannot be empty.")

        length = len(password)
        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)
        has_number = any(char.isdigit() for char in password)
        has_special = any(not char.isalnum() for char in password)

        score = calculate_score(
            length,
            has_uppercase,
            has_lowercase,
            has_number,
            has_special,
        )

        entropy = calculate_entropy(password)

        return PasswordAnalysis(
            length=length,
            has_uppercase=has_uppercase,
            has_lowercase=has_lowercase,
            has_number=has_number,
            has_special=has_special,
            score=score,
            strength=get_strength(score),
            security_level=get_security_level(score),
            entropy=entropy,
            entropy_level=get_entropy_level(entropy),
            common_password=check_common_password(password),
            recommendations=generate_recommendations(
                length,
                has_uppercase,
                has_lowercase,
                has_number,
                has_special,
            ),
        )
