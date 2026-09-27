from analyzer import PasswordAnalyzer
from report import display_report
from utils import get_password_input, ask_continue


def main():
    print("=" * 50)
    print("        CYBERGUARD PASSWORD ANALYZER")
    print("=" * 50)

    analyzer = PasswordAnalyzer()

    while True:
        password = get_password_input()
        result = analyzer.analyze(password)
        display_report(result)

        if not ask_continue():
            print("\nThank you for using CyberGuard.")
            break


if __name__ == "__main__":
    main()
