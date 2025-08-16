import re
import os

extractThreeCount = 0

if os.path.exists('Assignment - Regex.txt'):
    fin = open('Assignment - Regex.txt')
    text = fin.read()
    extractOne = re.findall(r"\d+", text)

    extractTwo = re.findall(r'(www\.\w+\.\S+)', text)
    #genex = re.compile(r'(www\.)(\w+\.\w+)')
    #extractTwo = genex.sub(r'\2',text)

    extractThree = re.findall('Arduino', text)
    for entry in extractThree:
        extractThreeCount += 1
else:
    print('File does nto exist')

print(extractOne)
print(extractTwo)
print(f"Arduino Appears {extractThreeCount} times")