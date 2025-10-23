from selectors import SelectSelector
"""
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

#Function and Method

def addTwoNumbers(num1, num2):
    return num1 + num2
q = int(input())
w = int(input())

result = addTwoNumbers(q, w)
print("add to number",result)
"""

listCharacter = ['A','B','C','D','E','F']
print("Character last char:", listCharacter[-1])
print("Character first char:", listCharacter[1])
print("Character range(C,D) char:", listCharacter[2:4])
print("Character first 2 char:", listCharacter[:2])
print("Character after 2 char:", listCharacter[2:])
print("Character remove last 2 char:", listCharacter[:-2])
print("Character after 2 char:", listCharacter[-2:])
for char in listCharacter:
    print(char)

max_value = max(listCharacter)
min_value = min(listCharacter)
print("\nMax: ", max_value)
print("Min: ", min_value)
listNum = [1,2,3,4,5,6,7,8,9]
print("Sum Of List:",sum(listNum))
#max number
maxNum = listNum[0]
for num in listNum:
    if num > maxNum:
        maxNum = num
print("Max: ", maxNum)

#min number
minNum = listNum[0]
for num in listNum:
    if num < minNum:
        minNum = num
print("Min: ", minNum)