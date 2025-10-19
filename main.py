import pyttsx3
import PyPDF2

book = open('oop_python.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)

friend = pyttsx3.init()

for p in range(7, 14):
    page = pdfreader.getPage(p)
    text = book.read()
    test = page.extractText()
    # friend.say(test)
    # friend.runAndWait()

print("hello world")

a = 10
b = 12
print(a + b)
print(a - b)
print(a * b)

name = "Mahmudul Hasan"
address = "vill:x, post:t, dist:z"
address1 = "vill:x, post:t, dist:z"
print(name, address, address1)

firstNum = 10
for x in range(0, 2):
    secondNum = input('SecondNum: ')
    print("Sum: ", firstNum + int(secondNum))
    if firstNum >= int(secondNum):
        print("valid number")
    else:
        print("invalid number")
