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
    totalSum = evenNumber + odeNumber



print("Total Sum: ", totalSum)
print("Even Number: ", evenNumber)
print("Ode Number: ", odeNumber)

# while loop
i =1
j =1
sumA = 0
sumB = 0
while i<100:
    sumA = sumA + i
    i = i+1
    sumB = sumB + i

while j<100:
    sumB += j
    j +=1
print("SumA: ", sumA)
print("SumB: ", sumA)

# list
charList = ["A","B","C","D","E","F"]
print("Character", charList[1])
for char in charList:
    print(char)