# pdf-word-counter

On Mac, you will need to install tesseract, poppler and pdf2image :

Install pip and homebrew first and then run the following commands:

`brew install tesseract`

`brew install poppler`

`pip install pdf2image`

Then, once these packages have been installed, you will need to locate the tesseract package and add the location to the script

Do:

`which tesseract`

and then copy and paste the output into line 5 of **wordcounter.py**

