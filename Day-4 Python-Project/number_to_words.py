from num2words import num2words

def number_to_words():
    try:
        num = int(input("Enter a number: "))  # Get user input
        words = num2words(num, lang='en').replace("-", " ").title()  # Convert number to words
        print(f"📌 Output: \"{words}\"")
    except ValueError:
        print("❌ Please enter a valid number.")

number_to_words()
