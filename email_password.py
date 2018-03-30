import pandas as pd
import numpy as np
import pprint
import os
import email
import olefile,sys
file = open('C:\\Users\\xl7\\PycharmProjects\\Automatetheboringstuff\\email_template.msg','rb')

msg = email.message_from_binary_file(file)
print(msg)
ole = olefile.OleFileIO("C:\\Users\\xl7\\PycharmProjects\\Automatetheboringstuff\\email_template.msg")
print(ole.header_signature())



xls = pd.ExcelFile("C:\\Users\\xl7\\PycharmProjects\\Automatetheboringstuff\\email_list.xlsx")
sheet_contacts = xls.parse('contacts')
emails = {}

for row in range(len(sheet_contacts.index)):
    bank_name = sheet_contacts.iloc[row,1]
    bank_emails = sheet_contacts.iloc[row,2]
    emails[bank_name] = bank_emails

print(len(emails))
pprint.pprint(emails)


