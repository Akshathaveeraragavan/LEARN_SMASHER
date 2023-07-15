#This is a password generator using secret module
import secrets
import string 
letters=string.ascii_letters
numbers=string.digits
symbols=string.punctuation
low=numbers
fair=letters+numbers
strong=letters+numbers+symbols
password=''
while 1:
    length=int(input("Hi user , Please enter the length of the password : "))
    level=int(input('Enter the level of security?\n(1-LOW/2-FAIR/3-STRONG):'))
    if level in [1,2,3]:
        if level==1:
            for i in range(length):
                password+=''.join(secrets.choice(low))
            print('The generated password of low security is:',password)
            print('Hope the generated password helps! Visit again!!!')
            break
        elif level==2:
            for i in range(length):
                password+=''.join(secrets.choice(fair))
            print('The generated password of fair security is:',password)
            print('Hope the generated password helps! Visit again!!!')
            break
        elif level==3:
            for i in range(length):
                password+=''.join(secrets.choice(strong))
            print('The generated password of strong security is:',password)
            print('Hope the generated password helps! Visit again!!!')
            break
        else:
            print('Invalid choice...')
            break
