#!/usr/local/bin/python
# -*- coding: utf-8 -*-

## we can also make it async and send the translation asynchronously but they will not come ordered.. And that's not good.

import asyncio
from googletrans import Translator

translator = Translator()

input_file = "locale_string.txt"
output_file = "locale_string"

src_lang = input("Enter the source language code (e.g., 'en' for English): ").strip()
dest_lang = input("Enter the target language code (e.g., 'es' for Spanish): ").strip()

valid_languages = ['en', 'es', 'fr', 'de', 'it', 'pt', 'ko', 'ja', 'zh-cn', 'zh-tw', 'ru', 'ro']
if src_lang not in valid_languages or dest_lang not in valid_languages:
    print("Invalid language code entered. Please use valid language codes (e.g., 'en', 'es', 'fr').")
    exit()
    
def clean_translation(text):
    text = text.replace("„", "").replace("”", "").strip()
    return text

def is_an_empty_line(line):
    return not line.strip()

async def translate_text():
    with open(input_file, "r", encoding="utf-8") as infile, open(f"{output_file}_{dest_lang}.txt", "w", encoding="utf-8") as outfile:
        lines = infile.readlines()

        tasks = []
        for i in range(0, len(lines), 2):
            source_text = lines[i].strip()

            if is_an_empty_line(source_text):
                continue
            
            translation = await translator.translate(source_text, src=src_lang, dest=dest_lang)
            translated_text = translation.text
            
			#clean text.
            translated_text = clean_translation(translated_text)

            outfile.write(f'{source_text}\n')
            outfile.write(f'"{translated_text}"\n')

            print(f'"{source_text}"\n')
            print(f'"{translated_text}"\n')

asyncio.run(translate_text())

print(f"Translation processing complete. Output written to '{output_file}_{dest_lang}.txt'.")
