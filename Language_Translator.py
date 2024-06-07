from googletrans import Translator

def translate_text(text, source_lang, target_lang):
  translator = Translator()
  translation = translator.translate(text, src=source_lang, dest=target_lang)
  return translation.text
text_to_translate = "Hello, how are you?"
source_language = 'en'  # English
target_language = 'es'  # Spanish

translated_text = translate_text(text_to_translate, source_language, target_language)
print(f"Translated text: {translated_text}")
