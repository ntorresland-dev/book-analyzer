import sys
def get_text_content(path: str) -> str | None:
    try:
        with open(path, encoding="utf-8") as file:
            text_content = file.read()
        return text_content

    except FileNotFoundError:
        print(f"Error: File {path} not found.")
        sys.exit(1)
