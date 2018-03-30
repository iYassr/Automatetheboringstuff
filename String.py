

myList = ['i','am','yasser aldosari']
string = 'hello guys'

string_list = string.split()
print(string_list)

print('hi'.center(20,'*'))


def printing(dict,rjust,ljust):
    print ( 'Items'.center(rjust+ljust,'*') )
    for i,k in dict.items():
        print (i.ljust(ljust,'.'),str(k).rjust(rjust,' '))


items = {'Red': 5, 'Blue': 10432432, 'Black': 40}
printing(items,9,9)




while True:
    print("Enter your UserName, Letters Only")
    username = input()
    if username.isalpha():
        break
    print("I said letters only")

while True:
    print("Enter your Password, Letters and digits only")
    password = input()
    if password.isalnum():
        break
    print("only letters and digits please!!!")


print("Your username is %s and your password is %s" % (username,password))


while True:
    print("Say thanks")
    thanks = input()
    if thanks.startswith("thanks"):
        print(" good boy ")
        break

    print("I SAID SAY THANKS!!!!")



