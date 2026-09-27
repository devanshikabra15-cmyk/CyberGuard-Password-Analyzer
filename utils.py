def get_password_input():
    while True:
        password = input("\nEnter your password: ")
        if password.strip() == "":
            print("Password cannot be empty. Please try again.")
        else:
            return password


def ask_continue():
    while True:
        choice = input("\nAnalyse another password? (y/n): ").strip().lower()

        if choice == "y":
            return True
        if choice == "n":
            return False

        print("Please enter only 'y' or 'n'.")
