# ScanSort

Hi! This is a small project I made called **ScanSort**. It takes an image of a receipt, pulls out the text using OCR, figures out what kind of expense it is (like Food or Travel), and saves it to a database. You can also see a graph of your monthly spending!

---

##  Need:

I always lose track of where my money goes — especially with tiny spends like snacks, rides, etc. So I thought, why not make a tool that can scan receipts and sort them for me? Also, it was a fun way to play with OCR and LLMs.

---

## Tech-stack

- **Tesseract OCR** – to read text from images
- **FLAN-T5 (via HuggingFace)** – to classify the expense
- **SQLite** – to save the data
- **Matplotlib** – to plot a monthly expense graph
- Python libraries: `pytesseract`, `PIL`, `transformers`, `sqlite3`, `matplotlib`

---

## Working

1. Upload your receipt (image file like JPG/PNG/WEBP)
2. Extract the text from it using OCR
3. Ask a language model: “Hey, what type of expense is this?”
4. Save the result (text, category, amount, date) into an SQLite database
5. Plot a graph of how much you’ve spent each month
