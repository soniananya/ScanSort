
---

# 🧾 ScanSort – FastAPI-Powered Receipt Parser with OCR + LLM

ScanSort is what happens when OCR meets actual backend engineering.

You upload a receipt image. It reads the text (Tesseract), understands it (FLAN-T5), figures out what category it belongs to, saves it in a SQLite database, and gives you usable stats and graphs — all behind a FastAPI interface.

Useful, minimal, and built to behave like a real backend system. No UI. No toy notebooks. Just clean I/O.

---

## ⚙️ Stack That Actually Does Stuff

| What               | Tool                                     |
| ------------------ | ---------------------------------------- |
| OCR                | `Tesseract` via `pytesseract`            |
| LLM Classification | `FLAN-T5` from HuggingFace               |
| API Layer          | `FastAPI`                                |
| Storage            | `SQLite` (because Postgres was overkill) |
| Plotting           | `Matplotlib`, `Seaborn`                  |
| Image Parsing      | `PIL`                                    |
| DataOps            | `pandas`                                 |

---

## 🧠 Flow

1. Upload receipt image (`.webp`, `.png`, whatever).
2. OCR reads the raw text.
3. FLAN-T5 infers the expense category.
4. Parsed data (text, category, amount, date) gets saved to SQLite.
5. Visualizations are generated on the fly when requested — not precomputed.

---

## 🚀 API Endpoints (Fully functional, not just placeholders)

| Method | Route             | Description                                       |
| ------ | ----------------- | ------------------------------------------------- |
| `GET`  | `/`               | Root check                                        |
| `POST` | `/upload`         | Upload and process a receipt                      |
| `GET`  | `/receipts`       | Get all saved records                             |
| `GET`  | `/chart/category` | Bar chart of category-wise spend                  |
| `GET`  | `/chart/monthly`  | Monthly spend trend                               |
| `GET`  | `/stats`          | Total receipts, average spend, and category count |
| `GET`  | `/test-ocr`       | Checks if Tesseract is installed and working      |
| `POST` | `/test-upload`    | Verifies file uploads (debug tool)                |

Docs at: `http://localhost:8000/docs`

---

## 🗃️ Structure

```
ScanSort/
├── main.py            # FastAPI routes
├── ocrllm.py          # OCR + FLAN-T5 logic
├── db.py              # SQLite insert / fetch / init
├── receipt.db         # Local database
├── sampleReceipt.webp # Test image
└── graph.png          # Auto-generated chart
```

---

## 🏁 Setup

```bash
git clone https://github.com/soniananya/ScanSort.git
cd ScanSort

# Optional: venv
python -m venv venv && source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🎯 Why This Exists

Most “receipt scanners” are either:

* 90% frontend with fake data,
* or Jupyter notebooks that never leave Colab.

This is a backend system:

* Routes are modular and tested.
* OCR + LLM flow is functional, not hardcoded.
* Graphs are generated per request, not cached.
* All logic is isolated in clean Python files.

You could deploy it. Extend it. Integrate it. That was the point.

---

## 📌 TODOs

* [ ] Batch upload support
* [ ] Auth for user-level expense tracking
* [ ] PDF support
* [ ] Hugging Face Spaces / Render deployment

---

## 👤 Author

Built by [Ananya Soni](https://github.com/soniananya)
Ping me if you’re building something with real-world data.

---


