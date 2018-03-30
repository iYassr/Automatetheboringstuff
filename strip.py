import re


def stripMe(text):
    text = re.sub('^\s*','',text)
    text = re.sub('\s*$','',text)
    print(text)

stripMe(text='    hello        fsd    ')
