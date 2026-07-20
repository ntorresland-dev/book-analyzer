def get_words_count(text: str) -> int:
    return len(text.split())

def get_character_count(text: str) -> int:
    total_characters = 0

    for character in text:
        if character == " " or character == "\n":
            continue

        total_characters += 1

    return total_characters
