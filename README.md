#  DDR AI Generator

An AI-powered system that automatically generates a **Detailed Diagnostic Report (DDR)** by analyzing inspection and thermal inspection reports using **Google Gemini AI**.

The application extracts observations from multiple PDF reports, combines the information intelligently, avoids duplicate findings, and generates a structured client-ready diagnostic report in Microsoft Word format.

---

# Features

- Extracts text from Inspection Reports (PDF)
- Extracts text from Thermal Reports (PDF)
- Extracts relevant inspection images
- Uses Google Gemini AI to understand and structure the reports
- Merges inspection and thermal findings
- Detects duplicate observations
- Handles missing information gracefully
- Generates a professional DDR report in DOCX format

---

# Tech Stack

- Python 3.11
- Google Gemini 2.5 Flash API
- PyMuPDF (fitz)
- python-docx
- python-dotenv
- JSON
- VS Code

---

# Project Structure

```
DDR AI Generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── input/
│   ├── inspection_report.pdf
│   └── thermal_report.pdf
│
├── modules/
│   ├── workflow.py
│   ├── pdf_reader.py
│   ├── image_extractor.py
│   ├── llm.py
│   ├── report_generator.py
│   ├── document_parser.py
│   └── utils.py
│
├── prompts/
│
├── templates/
│
└── output/
    ├── inspection.json
    ├── thermal.json
    ├── final_ddr.json
    └── DDR_Report.docx
```

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
```

Move into the project folder.

```bash
cd DDR-AI-Generator
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
python -m pip install -r requirements.txt
```

---

# Configure Environment Variables

Create a `.env` file.

Add your Gemini API key.

```env
GEMINI_API_KEY=your_api_key_here
```

---

# Run the Project

```bash
python app.py
```

Generated outputs are stored inside the **output/** folder.

---

# Workflow

```
Inspection Report PDF
            │
            ▼
      PDF Text Extraction
            │
            ▼
      Inspection JSON
            │
            │
Thermal Report PDF
            │
            ▼
      Thermal JSON
            │
            ▼
      Gemini AI Merge
            │
            ▼
     Final DDR JSON
            │
            ▼
     Microsoft Word Report
```

---

# Output

The application automatically generates

- inspection.json
- thermal.json
- final_ddr.json
- DDR_Report.docx

---

# Current Limitations

- Thermal observations are included only when supported by the source document.
- Image placement is based on extracted inspection images and may not always achieve perfect semantic alignment.
- The system intentionally avoids inventing or assuming missing information.

---

# Future Improvements

- Confidence scoring for extracted observations
- Better semantic image mapping
- Interactive web interface
- Support for additional inspection report formats
- Multi-property batch processing

---

# Author

**Sujay S Pattar**

Artificial Intelligence & Machine Learning Engineering Student

Built as part of an AI Generalist / Applied AI Builder hiring assignment.