def encrypt(text: str, shift: int = 3) -> str:
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Sirf letters ko shift karega
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters same rahenge
    return encrypted_text

def decrypt(text: str, shift: int = 3) -> str:
    decrypted_text = ""
    for char in text:
        if char.isalpha():  
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

# 🚀 User input le kar encrypt aur decrypt karega
message = input("Enter your message: ")
encrypted_msg = encrypt(message)
decrypted_msg = decrypt(encrypted_msg)

print(f"Encrypted: {encrypted_msg}")
print(f"Decrypted: {decrypted_msg}")
