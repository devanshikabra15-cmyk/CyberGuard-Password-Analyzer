def generate_recommendations(
    length,
    has_uppercase,
    has_lowercase,
    has_number,
    has_special,
):
    recommendations = []

    if length < 8:
        recommendations.append("Use at least 8 characters.")

    if not has_uppercase:
        recommendations.append("Add at least one uppercase letter.")

    if not has_lowercase:
        recommendations.append("Add at least one lowercase letter.")

    if not has_number:
        recommendations.append("Add at least one number.")

    if not has_special:
        recommendations.append("Add at least one special character.")

    if not recommendations:
        recommendations.append(
            "Your password meets all basic composition requirements."
        )

    return recommendations
