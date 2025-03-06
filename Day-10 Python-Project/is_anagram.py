def is_anagram(word1: str, word2: str) -> bool:
    # Whitespace aur special characters ignore karne ke liye filter aur lower()
    clean_word1 = "".join(filter(str.isalnum, word1.lower()))
    clean_word2 = "".join(filter(str.isalnum, word2.lower()))

    # Sorted letters compare karke check karna
    return sorted(clean_word1) == sorted(clean_word2)

# User se input lena
word1 = input("Enter first word: ").strip()
word2 = input("Enter second word: ").strip()

# Result print karna
if is_anagram(word1, word2):
    print("✅ Yes, it's an anagram!")
else:
    print("❌ No, it's not an anagram!")
