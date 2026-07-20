import sys

def get_text_content(path: str) -> str:
    try:
        with open(path, encoding="utf-8") as file:
            text_content = file.read()
        return text_content

    except FileNotFoundError:
        return "Archivo no encontrado. Vuelve a intentarlo."

def main():
    if len(sys.argv) < 2:
        print("Error: Se requiere al menos un argumento.")
        sys.exit(1)

    path = sys.argv[1]
    text_content = get_text_content(path)
    print(text_content)

if __name__ == "__main__":
    main()
