import pyperclip
import re
def emailRegex(text):
    #:? is to not capture groups only.. you solved it haha
    #print(re.findall(r'\w{1,20}@\w{1,20}.(?:com|org|co)',text))

    return re.findall(r'\w{1,10}@\w{1,10}.(?:com|org|co)',text)

def phoneRegex(text):
    return re.findall(r'\d{3}(?:-|\))\d{3}-\d{4}',text)


text = pyperclip.paste()
emailsList = emailRegex(text)
phonesList = phoneRegex(text)
emailsPhoneList = emailsList + phonesList
if emailsPhoneList == []: #empty
    print('no emails nor phone numbers copied')
else:
    pyperclip.copy('\n'.join(emailsPhoneList))
    print('Copied to clipboard')
