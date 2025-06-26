import string

def check_password_strength(password):
    strength = 0
    tips = []

    if len(password) >= 8:
        strength += 1
    else:
        tips.append("Make it at least 8 characters long.")

    if any(char.isdigit() for char in password):
        strength += 1
    else:
        tips.append("Add some numbers.")

    if any(char in string.punctuation for char in password):
        strength += 1
    else:
        tips.append("Use symbols like !, @, #, etc.")

    if any(char.isupper() for char in password):
        strength += 1
    else:
        tips.append("Use uppercase letters.")

    if strength == 4:
        print("✅ Strong password!")
    else:
        print("⚠️ Weak password. Try this:")
        for tip in tips:
            print("- " + tip)

# Run the checker
user_password = input("Enter a password to check: ")
check_password_strength(user_password)


