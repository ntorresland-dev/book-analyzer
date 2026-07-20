import sys
from file_management import get_text_content
from stats import get_character_count, get_words_count



def main():
    if len(sys.argv) < 2:
        print("Error: Se requiere al menos un argumento.")
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

if __name__ == "__main__":
    main()
