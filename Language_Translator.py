from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

# Function to take user input for translation
def main():
    text_to_translate = input("Enter the text to translate: ")
    source_language = input("Enter the source language code (e.g., 'en' for English): ")
    target_language = input("Enter the target language code (e.g., 'es' for Spanish): ")

    translated_text = translate_text(text_to_translate, source_language, target_language)
    print(f"Translated text: {translated_text}")

if __name__ == "__main__":
    main()
