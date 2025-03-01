def is_binary_palindrome():
    while True:
        user_input = input("Enter an integer (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Goodbye! 👋")
            break
        
        if not user_input.isdigit():
            print("⚠️ Error: Please enter a valid integer!")
            continue
        
        number = int(user_input)
        binary_representation = bin(number)[2:]
        
        print(f"📌 Binary: {binary_representation}")
        
        if binary_representation == binary_representation[::-1]:
            print("✅ Palindrome")
        else:
            print("❌ Not a Palindrome")

is_binary_palindrome()