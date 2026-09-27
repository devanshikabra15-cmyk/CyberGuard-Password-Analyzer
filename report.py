from analyzer import PasswordAnalysis


def _yes_no(value):
    return "YES" if value else "NO"


def display_report(result: PasswordAnalysis):
    print("\n" + "-" * 50)
    print("                 PASSWORD REPORT")
    print("-" * 50)

    print(f"Password Length       : {result.length}")
    print(f"Uppercase Present     : {_yes_no(result.has_uppercase)}")
    print(f"Lowercase Present     : {_yes_no(result.has_lowercase)}")
    print(f"Number Present        : {_yes_no(result.has_number)}")
    print(f"Special Character     : {_yes_no(result.has_special)}")
    print(f"Password Score        : {result.score}/5")
    print(f"Password Strength     : {result.strength}")
    print(f"Security Level        : {result.security_level}")
    print(f"Password Entropy      : {result.entropy:.2f} bits")
    print(f"Entropy Level         : {result.entropy_level}")
    print(f"Common Password       : {_yes_no(result.common_password)}")

    if result.common_password:
        print("WARNING: This password is commonly used.")

    print("\nSecurity Recommendations:")
    for item in result.recommendations:
        print(f"- {item}")

    print("-" * 50)
