import re
from deep_translator import GoogleTranslator


def remove_timing_and_empty_lines(text):
    text_without_timing = re.sub(r'\d{1,2}:\d{2}(?::\d{2})?', '', text)
    text_cleaned = re.sub(r'\n\s*\n', '\n', text_without_timing)
    return text_cleaned.strip()


def split_text(text, max_length=5000):
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]


def translate_text(text, target_lang=' '):
    translator = GoogleTranslator(source='auto', target=target_lang)
    return translator.translate(text)

transcript = """ 



"""


cleaned_text = remove_timing_and_empty_lines(transcript)


count = len(cleaned_text)
print(f"Numb of simbols: {count}")


if cleaned_text:
    if count > 5000:
        parts = split_text(cleaned_text)  
        translated_parts = [translate_text(part, target_lang='ru') for part in parts]  
        translated_text = ' '.join(translated_parts)  
    else:
        translated_text = translate_text(cleaned_text, target_lang='ru')  
    
    print(translated_text)
else:
    print("No text to translate.")