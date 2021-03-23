from pdf2image import convert_from_path
import pytesseract

# location of tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# open pdf
doc_name = 'Slim_shady.pdf'
pages = convert_from_path('pdf_docs/'+doc_name, 500)

# word of interest
word = 'Shady'

# initiate counters
page_number=0
word_count=0

for page in pages:

    # Saving pages in jpeg format
    page_name = 'jpg_images/'+str(doc_name[:-4])+'_'+str(page_number)+'.jpg'
    page.save(page_name, 'JPEG')
    
    # Read words from jpeg
    string=pytesseract.image_to_string(page_name)
    
    #count word on the page and add result to counter
    word_count += string.upper().count(word.upper())
    
    page_number+=1

print('The word '+word+' appears '+ str(word_count)+' times')
