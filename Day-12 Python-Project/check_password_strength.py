def check_password_strength(password: str) -> str:
    if len(password) < 6:
        return "Strength: Weak"
    
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_special = any(char in "!@#$%^&*()" for char in password)

    if len(password) > 10 and has_digit and has_upper and has_special:
        return "Strength: Strong"
    elif 6 <= len(password) <= 10 and has_digit:
        return "Strength: Medium"
    
    return "Strength: Weak"

# 🚀 User input le kar strength check karna
password = input("Enter your password: ")
print(check_password_strength(password))
