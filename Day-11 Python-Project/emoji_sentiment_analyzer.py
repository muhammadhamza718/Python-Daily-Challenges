import re

# Emoji dictionary mood mapping
emoji_moods = {
    "😊": "Happy Mood!", "😃": "Happy Mood!", "😍": "Happy Mood!",
    "😢": "Sad Mood!", "😭": "Sad Mood!", "☹": "Sad Mood!",
    "😡": "Angry Mood!", "🤬": "Angry Mood!", "😠": "Angry Mood!",
    "😐": "Neutral Mood!", "😶": "Neutral Mood!", "🤔": "Neutral Mood!"
}

def detect_mood(message: str) -> str:
    # Emojis extract karne ke liye regex pattern
    emojis = re.findall(r'[\U0001F600-\U0001F64F]', message)  # Emoji range

    if not emojis:
        return "No emoji found, can't detect mood! 🤷‍♂️"

    # Pehla matching emoji mood detect karna
    for emoji in emojis:
        if emoji in emoji_moods:
            return f"Detected Mood: {emoji_moods[emoji]}"

    return "No relevant emoji found for mood detection! 🤔"

# User se input lena
message = input("Enter your message: ").strip()

# Mood detect karna aur print karna
print(detect_mood(message))
