# Create a variable name with your name, and a variable age with your age. Print both.

from typing import Dict

FIRST_NAME: str = "Tristán"
LAST_NAME: str = "Nouwens"
AGE: int = 18

LOCALES: Dict[str, Dict[str, str]] = {
    "nl": {"text": "Mijn naam is {firstName} {lastName} en ik ben {age} jaar oud."},
    "en": {"text": "My name is {firstName} {lastName} and I am {age} years old."},
    "de": {"text": "Mein Name ist {firstName} {lastName} und ich bin {age} Jahre alt."},
    "es": {"text": "Me llamo {firstName} {lastName} y tengo {age} años."}
}

def main() -> None:
    available_langs = list(LOCALES.keys())
    default_lang = available_langs[0]
    prompt = f"Choose language ({'/'.join(available_langs)}) [{default_lang}]: "
    lang = input(prompt).strip().lower() or default_lang

    if lang not in LOCALES:
        print("Language not supported.")
        return

    print(
        LOCALES[lang]["text"].format(
            firstName=FIRST_NAME,
            lastName=LAST_NAME,
            age=AGE
        )
    )

if __name__ == "__main__":
    main()
