import sys
from file_management import get_text_content
from text_manipulation import dict_to_sorted_list, get_letter_frequency
from stats import get_character_count, get_words_count



def main():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text_content = get_text_content(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")

    print("----------- Word Count ----------")
    words_counted = get_words_count(text_content)
    print(f"Found {words_counted} total words")

    print("-------- Character Count --------")
    character_counted = get_character_count(text_content)
    print(f"Total characters: {character_counted}")

    print("-------- Letter Frequency --------")
    letter_frequency = get_letter_frequency(text_content)
    ordered_frequency = dict_to_sorted_list(letter_frequency)
    for i in ordered_frequency:
        print(f"{i[0]}: {i[1]}")

if __name__ == "__main__":
    main()
