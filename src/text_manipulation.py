def get_letter_frequency(text: str) -> dict[str, int]:
    letter_frequency = {}
    for letter in text.lower():
        if letter.isalpha():
            letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

    return letter_frequency


def sort_on(letter: tuple[str, int]) -> int:
    return letter[1]

def dict_to_sorted_list(dict_frequency) -> list[tuple[str, int]]:
    tuple_list = []
    for letter in dict_frequency:
        tuple_list.append((letter, dict_frequency[letter]))

    sorted_list = sorted(tuple_list, key=sort_on, reverse=True)
    return sorted_list
