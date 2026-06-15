import re
import getpass

# ==========================================
#      ADVANCED PASSWORD STRENGTH CHECKER
# ==========================================

def check_password_strength(password):

    score = 0
    feedback = []

    # Minimum Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should contain at least 8 characters.")

    # Uppercase Letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase Letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special Character
    if re.search(r"[!@#$%^&*()_+=<>?/{}~|-]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # No Spaces
    if " " not in password:
        score += 1
    else:
        feedback.append("Password should not contain spaces.")

    # Strength Result
    print("\n" + "=" * 45)
    print("        PASSWORD STRENGTH RESULT")
    print("=" * 45)

    if score == 6:
        print("Strength Level : VERY STRONG")
        print("Security Score : 10/10")

    elif score >= 4:
        print("Strength Level : MEDIUM")
        print("Security Score : 6/10")

    else:
        print("Strength Level : WEAK")
        print("Security Score : 3/10")

    # Feedback
    if feedback:
        print("\nSuggestions to Improve Password:")
        for item in feedback:
            print("•", item)

    else:
        print("\nExcellent Password Security!")

# ==============================
#            MAIN
# ==============================

print("=" * 50)
print("     ADVANCED PASSWORD CHECKER")
print("=" * 50)

while True:

    # Hidden password input
    password = getpass.getpass("\nEnter Password: ")

    check_password_strength(password)

    choice = input("\nDo you want to check another password? (yes/no): ").lower()

    if choice != "yes":
        print("\nProgram Closed.")
        break