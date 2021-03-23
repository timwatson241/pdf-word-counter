# pdf-word-counter

# Setup

On Mac, you will need to install tesseract, poppler and pdf2image :

Install pip and homebrew first and then run the following commands:

`brew install tesseract`

`brew install poppler`

`pip install pdf2image`

Then, once these packages have been installed, you will need to locate the tesseract package and add the location to the script

Do:

`which tesseract`

and then copy and paste the output into line 5 of **wordcounter.py**

# Operation

1. Add your pdf to the **pdf_docs** folder
2. Modify **wordcounter.py** to include the name of the doc you want to work on
3. Modify **wordcounter.py** to include the word you want to count
4. Run `python wordcounter.py`
