def oldway():
    def isPhoneNumber(text):

        if len(text) != 12:
            return False
        for i in range(0,3):
            if not text[i].isdecimal():
                return False
        if text[3] != '-':
            return False

        for i in range(4,7):
            if not text[i].isdecimal():
                return False

        if text[7] != '-':
            return False
        for i in range(8,12):
            if not text[i].isdecimal():
                return False
        return True


    print('415-555-4242 is a phone number')

    print(isPhoneNumber('415-555-4242'))
    message = 'Call me at 415-545-5455 when i need you 434-541-3454'
    for i in range(len(message)):
        chunk = message[i:+i+12]

        if isPhoneNumber(chunk):
            print('your phone number is : %s' % (chunk))

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d').search('my phone number is 434-434-5343').group()
#mo = phoneNumRegex.search('my phone number is 434-434-5343')
#print('phone number found = ' + mo.group())
print(' a ' + phoneNumRegex)

groupRegexEx = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)').search('415-555-4343')
print(groupRegexEx.group(1))
print(groupRegexEx.group(0))


heroRegex = re.compile(r'Batman | super man').findall('Batman and super man')
print(heroRegex)
batRegex = re.compile(r'bat(man|mobile|copter|bat)').search('batbat batmobile bat copter')
print(batRegex.group())

optRegex = re.compile(r'Bat(wo)?man').fullmatch('Batman , Batwoman')
print(optRegex)

plusReg = re.compile('Yasse(r)*').search('Yasse')
print(plusReg.group())

try:
    ipReg = re.compile('(\d){2,3}.(\d){2,3}.(\d){1,3}.(\d){1,3}\\\(\d)').search('10.168.1.1\\4')
    print(ipReg.group())
except:
    print('Not found')


myname = re.compile('(Y|y)(asser)\saldosari').search('yasser aldosari')
print(myname.group())
# stands for ^ not inside [] only, if not means begin and $ ends
consonantRegex = re.compile(r'[^aeiouAEIOU]')
cR = consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
print(cR)

print( re.match((r'^y(\D)*y$') , 'yasser aldosfsdfsdariy') )

nameRegex = re.match(r'First Name: (.*) Last Name: (.*)','First Name: Yasser Last Name: Aldosari')
print(nameRegex)

# RE IS FREAKING AWESOME!!!! LOVE IT

subRegex = re.compile(r'Yasser')
print(subRegex.sub('\1***','Agent Yasser gave the secret documents Yasser'))

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
print('-------------')
var = '43 1,1234 6,368,745 12,34,567 1234 '
print(re.findall(r'\d{1,3}(?:,\d{3})*','43 1,1234 6,368,745 12,34,567 1234 '))


print( re.findall(r'(?:Alice|Bob|Carol)\s(?:eats|pets|throws)\s(?:apples.|cats.|baseballs.)'
                     ,'Alice eats apples. Bob pets cats. Carol throws baseballs. Alice throws Apples. '
                      'BOB EATS CATS. Tobocop eats apples. ALICE THROWS FOOTBALLS. '
                      'Carol eats 7 cats ',re.IGNORECASE) )

print( re.findall(r'[A-Z]\w*\sNakamoto' ,'Satoshi Nakamoto Alice Nakamoto Robocop Nakamoto satoshi Nakamoto Mr. Nakamoto Satoshi nakamoto' ))