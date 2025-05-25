# PDF Image Screenshot Tool for LLM

A simple tool designed to extract images from PDFs, allowing Large Language Models (LLMs) to analyze and read image content, as current LLMs cannot directly process images embedded within PDF files.

## Requirements

- Python 3
- PyMuPDF

## Installation

Install the required Python package:

```bash
pip3 install PyMuPDF
```

## Setup

1. Create a directory named `PDF_Database` in the same directory as the Python script.
2. Place your PDF files into the `PDF_Database` directory.

```
project/
├── PDF_Database/
│   └── example.pdf
└── pdf_image_screenshot.py
```

## Usage

1. Open your terminal in the directory containing the Python script.
2. Run the script:

```bash
python3 pdf_image_screenshot.py
```

3. Follow the interactive prompts:
   - Select the index of your PDF file.
   - Specify the desired resolution or pixel settings.

4. The images extracted from the PDF will be saved in your current working directory.

## Output

- Extracted images are saved directly to your original directory for easy access.
