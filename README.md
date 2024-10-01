<br/>
<div align="center">
</a>
<h3 align="center">To Convert !</h3>
<p align="center">
" To Convert ! " app coded by Muhammet Salih Koca.
  
</p>
</div> 

## About The Project
  This is a file converter application built using "Kivy" for the user interface, which allows conversion between multiple file formats. 

 The app supports: 
- JPEG to PDF
- JPEG to DOCX/DOC
- DOCX/DOC to PDF 
- DOCX/DOC to JPEG 
- PDF to JPEG  
- PDF to DOCX/DOC
  
## Screenshots

<img src="https://github.com/user-attachments/assets/d021b515-1002-4a3f-91e4-516cf445bed9" alt="Screenshot 2024-10-01 035541" width="200" height="300" style="border:2 solid lightblue;"/>
<img src="https://github.com/user-attachments/assets/7cf81030-7997-4405-a8e2-dc1020446a30" alt="Screenshot 2024-10-01 035548" width="200" height="300" style="border:2 solid lightblue;"/>
<img src="https://github.com/user-attachments/assets/549c8caa-7978-4bdb-9238-6cb91331162c" alt="Screenshot 2024-10-01 035556" width="200" height="300" style="border:2 solid lightblue;"/> 
<img src="https://github.com/user-attachments/assets/fdf1d693-c67b-4b75-89ab-c485d74f0445"  alt="Screenshot 2024-10-01 035603" width="200" height="300" style="border:2 solid lightblue;"/>      


## Requirements

```sh
pip install -r requirements.txt
```


## Tesseract Installation

For Windows:

```sh
https://github.com/UB-Mannheim/tesseract/wiki
```

For macOS:

```sh
brew install tesseract
```
For Linux: 

```sh
sudo apt-get install tesseract-ocr
```

## Set Tesseract Path
 
 Make sure to set the path for Tesseract in your Python script before using pytesseract.
 
```sh
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## Running the Application

To run the application, navigate to the project directory and execute:

```sh
python converter.py
```

The app window should open, and you can start converting files by selecting the appropriate options.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
