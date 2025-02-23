#!/usr/local/bin/python
from googletrans import Translator

translator = Translator()

input_file = "locale_string.txt"
output_file = "locale_string"

src_lang = input("Enter the source language code (e.g., 'en' for English): ").strip()
dest_lang = input("Enter the target language code (e.g., 'es' for Spanish): ").strip()

valid_languages = ['en', 'es', 'fr', 'de', 'it', 'pt', 'ko', 'ja', 'zh-cn', 'zh-tw', 'ru']
if src_lang not in valid_languages or dest_lang not in valid_languages:
    print("Invalid language code entered. Please use valid language codes (e.g., 'en', 'es', 'fr').")
    exit()

with open(input_file, "r", encoding="utf-8") as infile, open(output_file+"_"+dest_lang+".txt", "w", encoding="utf-8") as outfile:
    lines = infile.readlines()
    

    for i in range(0, len(lines), 2):
        source_text = lines[i].strip()
        
        if i + 1 < len(lines):
            translated_text = lines[i + 1].strip()
        else:
            translated_text = "" 
        
        if not translated_text:
            translated_text = translator.translate(source_text, src=src_lang, dest=dest_lang).text
        
        outfile.write(f'{source_text} -> {translated_text}\n')
        print(f'{source_text} -> {translated_text}') 

print("Translation processing complete. Output written to 'translated_locale.txt'.")
