#! python3
# bulletPointAdder.py

import pyperclip
text = pyperclip.paste()
newText = str(text).splitlines()

for i in range(len(newText)):
    newText[i] = ' * ' + newText[i]
finalText = ''
#for i in newText:
#   finalText += i + '\n'

finalText = '\n'.join(newText)

print(finalText)




pyperclip.copy(finalText)

