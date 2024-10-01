</p>
</div> 

# About The Project

  "To Convert!" is a file converter application with a user-friendly interface built using Kivy. It enables users to convert files between various formats efficiently.

The app currently supports the following conversions:

- JPEG to PDF
- JPEG to DOCX/DOC
- DOCX/DOC to PDF 
- DOCX/DOC to JPEG 
- PDF to JPEG  
- PDF to DOCX/DOC
  
# Screenshots

<img src="https://github.com/user-attachments/assets/d021b515-1002-4a3f-91e4-516cf445bed9" alt="Screenshot 2024-10-01 035541" width="200" height="300" style="border:2 solid lightblue;"/>
<img src="https://github.com/user-attachments/assets/7cf81030-7997-4405-a8e2-dc1020446a30" alt="Screenshot 2024-10-01 035548" width="200" height="300" style="border:2 solid lightblue;"/>
<img src="https://github.com/user-attachments/assets/549c8caa-7978-4bdb-9238-6cb91331162c" alt="Screenshot 2024-10-01 035556" width="200" height="300" style="border:2 solid lightblue;"/> 
<img src="https://github.com/user-attachments/assets/fdf1d693-c67b-4b75-89ab-c485d74f0445"  alt="Screenshot 2024-10-01 035603" width="200" height="300" style="border:2 solid lightblue;"/>      

# Getting Started


## Requirements

  Ensure you have Python installed on your system. You also need to install required Python packages and external libraries as described below.

### Python Dependencies

  Install all necessary Python packages using the requirements.txt file.

```sh
pip install -r requirements.txt
```

## Poppler Installation

Poppler is required for PDF processing (e.g., PDF to JPEG conversion). Ensure Poppler is installed and added to your system PATH.

#### For Windows:

Download the Poppler binaries from Poppler for Windows and extract them. Make sure to add the
bin folder of Poppler to your system PATH.

```sh
https://github.com/oschwartz10612/poppler-windows
```

#### For macOS:

```sh
brew install poppler
```

#### For Linux:

```sh
sudo apt-get install poppler-utils
```

#### Note: On Windows, set the poppler_path in your script when using pdf2image:

```sh
convert_from_path('example.pdf', poppler_path=r'C:\path\to\poppler\bin')
```

#### Replace C:\path\to\poppler\bin with the actual path where you have extracted Poppler binaries.

## Tesseract Installation

Tesseract is used for Optical Character Recognition (OCR) to extract text from images (e.g., JPEG to DOCX conversion).

#### For Windows:

Download Tesseract from the following link and install it:

```sh
https://github.com/UB-Mannheim/tesseract/wiki
```

#### For macOS:

```sh
brew install tesseract
```

#### For Linux: 

```sh
sudo apt-get install tesseract-ocr
```

#### Note: Make sure to set the path for Tesseract in your Python script before using pytesseract:
  
```sh
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

Replace the path with the location where you installed Tesseract.

## Running the Application

To run the application, navigate to the project directory and execute:

```sh
python converter.py
```

A window should open where you can select different options for file conversion.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

##
  
  This comprehensive README will help users understand the purpose of the project, how to install dependencies, and run the application effectively. Make sure to adjust any paths or instructions based on your specific project setup.
