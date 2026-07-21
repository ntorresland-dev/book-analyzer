def get_letter_frequency(text: str) -> dict[str, int]:
    letter_frequency = {}
    for letter in text:
        if letter.isalpha():
            letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

    return letter_frequency
