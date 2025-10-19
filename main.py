import pyttsx3
import PyPDF2
book = open('oop_python.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)

friend = pyttsx3.init()
fot(int i; )

for p in range(7, 14):
    page = pdfreader.getPage(p)
    text = book.read()
    test = page.extractText()
    friend.say(test)
    friend.runAndWait()
