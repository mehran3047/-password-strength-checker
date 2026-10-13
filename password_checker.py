import re
import getpass

def check_password(password):

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add a number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add a special character.")

    print("\n----- PASSWORD SECURITY REPORT -----")

    if score <= 2:
        print("Password Strength: WEAK")
    elif score <= 4:
        print("Password Strength: MEDIUM")
    else:
        print("Password Strength: STRONG")

    print("Score:", score, "/ 5")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("-", item)

    print("------------------------------------")

print("PASSWORD STRENGTH CHECKER")
password = getpass.getpass("Enter your password: ")

check_password(password)