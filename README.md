# DDR AI Generator

An AI-powered Detailed Diagnostic Report (DDR) Generator that automatically analyzes Inspection Reports and Thermal Reports using Google's Gemini API and generates a professional Word report.

---

## Features

- Extracts text from Inspection PDF
- Extracts text from Thermal PDF
- Extracts inspection images
- Uses Gemini AI to structure inspection data
- Uses Gemini AI to structure thermal data
- Merges both reports into a final DDR JSON
- Generates a professional Microsoft Word (.docx) report

---

## Project Structure

```
DDR-AI-Generator/
│
├── input/
│   ├── inspection_report.pdf
│   └── thermal_report.pdf
│
├── extracted_images/
│
├── modules/
│   ├── pdf_reader.py
│   ├── image_extractor.py
│   ├── llm.py
│   ├── workflow.py
│   └── report_generator.py
│
├── prompts/
│   ├── extraction_prompt.txt
│   ├── merge_prompt.txt
│   └── ddr_prompt.txt
│
├── output/
│   ├── inspection.json
│   ├── thermal.json
│   ├── final_ddr.json
│   └── DDR_Report.docx
│
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Ssps28/DDR-AI-Generator.git
```

Move into the project

```bash
cd DDR-AI-Generator
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a file named `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY
```

You can obtain a Gemini API key from:

https://aistudio.google.com/app/apikey

---

## Run

Place the two PDFs inside

```
input/
```

Run

```bash
python app.py
```

Generated files

```
output/
│
├── inspection.json
├── thermal.json
├── final_ddr.json
└── DDR_Report.docx
```

---

## Technologies Used

- Python
- PyMuPDF
- Google Gemini API
- python-docx
- dotenv

---

## Workflow

Inspection PDF
        │
        ▼
Extract Text
        │
        ▼
Extract Images
        │
        ▼
Gemini AI
        │
        ▼
Inspection JSON

Thermal PDF
        │
        ▼
Extract Text
        │
        ▼
Gemini AI
        │
        ▼
Thermal JSON

Inspection JSON + Thermal JSON
        │
        ▼
Gemini AI Merge
        │
        ▼
Final DDR JSON
        │
        ▼
Word Report (.docx)

---

## Current Limitations

- Thermal image extraction is intentionally skipped to reduce processing time.
- Image-to-observation mapping is currently sequential and not computer vision based.
- Output quality depends on the structure of the uploaded reports.

---

## Author

**Sujay S Pattar**

Artificial Intelligence & Machine Learning Engineer
