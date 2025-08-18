



import pytesseract
from PIL import Image
from transformers import pipeline
from datetime import datetime
from db import insert_receipt



#LLM pipeline
classifier = pipeline("text2text-generation", model="google/flan-t5-small")





def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()


def classify_cat(text):
    prompt = f"""Classify the following expense text into one of these categories: Groceries, Food, Transport, Healthcare, Shopping, Entertainment, Utilities, Other.
    Text: {text}
    Category:"""       #llm fills in the blank.
    result = classifier(prompt, max_length=10, do_sample=False)[0]['generated_text']   #returns list with one dict. do sample (f) returns deterministic ans.
    return result.strip()

def extract_amount(text): #ex largest fp no.
    import re
    amounts = re.findall(r'\d+\.\d{2}', text)
    if amounts:
        return float(max(amounts, key=lambda x: float(x)))
    return None


def process_receipt(image_path, date_str):
   
    print(f"Processing {image_path}...")
    raw_text = extract_text(image_path)
    category = classify_cat(raw_text)
    amount = extract_amount(raw_text)
    date = datetime.strptime(date_str, "%Y-%m-%d").date()

    print("Extracted:", raw_text[:100], "...")
    print("Category:", category)
    print("Amount:", amount)
    print("Date:", date)

    if amount is not None:
        insert_receipt(raw_text, category, date.isoformat(), amount)
        print("Inserted into DB.")
    else:
        print("Amount not found. Skipping DB insert.")
# uploading sample img and using all func manually

