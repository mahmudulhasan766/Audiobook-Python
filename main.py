from selectors import SelectSelector

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
    #friend.say(test)
    #friend.runAndWait()

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
s = 0
for x in range(0, 2):
    secondNum = input('SecondNum: ')
    s= s+x
    print("index: ", x,s)
    print("Sum: ", firstNum + int(secondNum),x)
    if firstNum >= int(secondNum):
        print("valid number")
    else:
        print("invalid number")

forSum = 0
for i in  range(0,100,45):
    forSum = forSum + i
    print(i)

evenNumber = 0
odeNumber = 0
totalSum = 0
for i in  range(0,100):
    if i%2==0:
        continue
    else:
        odeNumber = odeNumber + i
        print("Ode Number: ", i)

    totalSum = evenNumber + odeNumber
    print("Sum: ", totalSum)


print("Total Sum: ", totalSum)
print("Even Number: ", evenNumber)
print("Ode Number: ", odeNumber)