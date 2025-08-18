from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import tempfile
import os
import sys
from datetime import datetime
import io
from PIL import Image
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pytesseract

# importing my existing functions from the project files
from db import init_db, insert_receipt, fetch_all_receipts


# Import your existing OCR and classification functions
from ocrllm import extract_text, classify_cat, extract_amount, classifier



def extract_text_from_bytes(image_bytes):
    """modified version of my extract_text function to work with bytes"""
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)
    return text.strip()

# fastapi app setup
app = FastAPI(title="ScanSort Receipt API")

# init database on startup
init_db()

@app.get("/")
def home():
    return {"message": "ScanSort API - using my existing functions!"}

@app.post("/test-upload")
async def test_upload(file: UploadFile = File(None)):
    """test endpoint to debug file upload issues"""
    if file is None:
        return {"error": "No file received", "tip": "Use form-data with key 'file' in Postman"}
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(await file.read()),
        "status": "File received successfully!"
    }

@app.post("/upload")
async def upload_receipt(file: UploadFile = File(..., description="Receipt image file")):
    """upload receipt and process using my existing functions"""
    
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Please upload an image file")
    
    try:
        # read image bytes
        image_bytes = await file.read()
        
        # use my existing OCR function (modified for bytes)
        raw_text = extract_text_from_bytes(image_bytes)
        
        if not raw_text.strip():
            raise HTTPException(status_code=400, detail="No text found in image")
        
        # use my existing classification function
        category = classify_cat(raw_text)
        
        # use my existing amount extraction
        amount = extract_amount(raw_text)
        
        # get current date
        date = datetime.now().date().isoformat()
        
        print("Extracted:", raw_text[:100], "...")
        print("Category:", category)
        print("Amount:", amount)
        
        # use my existing database function
        if amount is not None:
            insert_receipt(raw_text, category, date, amount)
            print("Inserted into DB.")
            
            return {
                "status": "success",
                "text": raw_text[:200] + "..." if len(raw_text) > 200 else raw_text,
                "category": category,
                "amount": amount,
                "date": date,
                "message": "Receipt processed and saved!"
            }
        else:
            return {
                "status": "partial_success",
                "text": raw_text[:200] + "..." if len(raw_text) > 200 else raw_text,
                "category": category,
                "amount": None,
                "date": date,
                "message": "Amount not found, but receipt processed"
            }
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing receipt: {str(e)}")

@app.get("/receipts")
def get_all_receipts():
    """get all receipts using my existing database function"""
    try:
        rows = fetch_all_receipts()
        receipts = []
        for row in rows:
            receipts.append({
                "id": row[0],
                "text": row[1][:100] + "..." if len(row[1]) > 100 else row[1],
                "category": row[2],
                "date": row[3],
                "amount": row[4]
            })
        
        return {"receipts": receipts, "total": len(receipts)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching receipts: {str(e)}")

@app.get("/chart/category")
def category_chart():
    """generate category expense chart using my existing plotting code"""
    try:
        # using my existing database connection and pandas code
        conn = sqlite3.connect("receipts.db")
        df = pd.read_sql_query("SELECT * FROM receipts", conn)
        conn.close()
        
        if df.empty:
            raise HTTPException(status_code=404, detail="No data available")
        
        # use my existing data processing
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        df = df.dropna(subset=['date', 'category', 'amount'])
        
        # use my existing plotting style
        plt.rcParams['font.family'] = 'DejaVu Sans'
        sns.set_theme(style="darkgrid", palette="pastel")
        
        # create the same category chart from my notebook
        plt.figure(figsize=(10, 6))
        df.groupby('category')['amount'].sum().sort_values(ascending=False).plot(
            kind='bar', color='skyblue', edgecolor='black'
        )
        plt.title("Total Expense by Category", fontsize=14)
        plt.ylabel("Total Amount")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        # save to temp file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        plt.savefig(temp_file.name, dpi=150, bbox_inches='tight')
        plt.close()
        
        return FileResponse(temp_file.name, media_type='image/png', filename='category_chart.png')
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating chart: {str(e)}")

@app.get("/chart/monthly")
def monthly_chart():
    """generate monthly trend chart using my existing code"""
    try:
        conn = sqlite3.connect("receipts.db")
        df = pd.read_sql_query("SELECT * FROM receipts", conn)
        conn.close()
        
        if df.empty:
            raise HTTPException(status_code=404, detail="No data available")
        
        # same data processing as my notebook
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        df = df.dropna(subset=['date', 'category', 'amount'])
        df['month'] = df['date'].dt.to_period('M')
        
        # use my existing monthly trend plot
        monthly_expense = df.groupby(df['month'].dt.to_timestamp())['amount'].sum()
        plt.figure(figsize=(10,6))
        monthly_expense.plot(marker='o', color='green')
        plt.title("Monthly Spending Trend", fontsize=14)
        plt.ylabel("Total Amount")
        plt.grid(True)
        plt.tight_layout()
        
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        plt.savefig(temp_file.name, dpi=150, bbox_inches='tight')
        plt.close()
        
        return FileResponse(temp_file.name, media_type='image/png', filename='monthly_chart.png')
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating monthly chart: {str(e)}")

@app.get("/test-ocr")
def test_ocr():
    """test if tesseract is working"""
    try:
        # Check if tesseract file exists
        tesseract_path = pytesseract.pytesseract.tesseract_cmd
        file_exists = os.path.exists(tesseract_path) if tesseract_path else False
        
        # Try to run tesseract
        import subprocess
        try:
            result = subprocess.run([tesseract_path, '--version'], capture_output=True, text=True, timeout=10)
            version_info = result.stdout
            working = True
        except:
            version_info = "Failed to run tesseract"
            working = False
        
        return {
            "tesseract_cmd": tesseract_path,
            "file_exists": file_exists,
            "tesseract_working": working,
            "version_info": version_info,
            "status": "working" if working else "not working"
        }
    except Exception as e:
        return {
            "error": str(e),
            "tesseract_cmd": getattr(pytesseract.pytesseract, 'tesseract_cmd', 'Not set'),
            "status": "error"
        }

@app.get("/stats")
def get_stats():
    """basic stats using my database"""
    try:
        conn = sqlite3.connect("receipts.db")
        df = pd.read_sql_query("SELECT * FROM receipts", conn)
        conn.close()
        
        if df.empty:
            return {"message": "No data available"}
        
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
        
        total_receipts = len(df)
        total_amount = df['amount'].sum()
        avg_amount = df['amount'].mean()
        categories = df['category'].value_counts().to_dict()
        
        return {
            "total_receipts": total_receipts,
            "total_spent": round(total_amount, 2),
            "average_spend": round(avg_amount, 2),
            "categories": categories
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating stats: {str(e)}")

