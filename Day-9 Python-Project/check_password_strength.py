import re

def validate_password_security(password: str) -> str:
    MINIMUM_LENGTH = 6
    RECOMMENDED_LENGTH = 8
    SPECIAL_CHARACTERS_PATTERN = r"[!@#$%^&*(),.?\":{}|<>]"
    UPPERCASE_PATTERN = r"[A-Z]"
    LOWERCASE_PATTERN = r"[a-z]"
    DIGIT_PATTERN = r"\d"

    # Check for basic password requirements
    if len(password) < MINIMUM_LENGTH or password.isalpha():
        return "Weak ❌"
    
    # Check for moderate password strength
    if len(password) >= RECOMMENDED_LENGTH and not re.search(SPECIAL_CHARACTERS_PATTERN, password):
        return "Moderate ⚠️"

    # Check for strong password criteria
    has_sufficient_length = len(password) >= RECOMMENDED_LENGTH
    has_uppercase = re.search(UPPERCASE_PATTERN, password)
    has_lowercase = re.search(LOWERCASE_PATTERN, password)
    has_digit = re.search(DIGIT_PATTERN, password)
    has_special_char = re.search(SPECIAL_CHARACTERS_PATTERN, password)

    if (has_sufficient_length and 
        has_uppercase and 
        has_lowercase and 
        has_digit and 
        has_special_char):
        return "Strong ✅"
    
    return "Weak ❌"

def main():
    user_password = input("Enter your password: ")
    password_strength = validate_password_security(user_password)
    print(f"Password Strength: {password_strength}")

if __name__ == "__main__":
    main()
