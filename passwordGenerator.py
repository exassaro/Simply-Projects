# Password Generator

import random

print('Welcome to your Password Generator')

chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\]^_{|}~'

num=input('Amount of passwords to generate: ')
num=int(num)

length=input('Your password length: ')

length=int(length)


print('\nThese are your passwords: ')

for pwd in range(num):
    passwords=''
    for c in range(length):
        passwords +=random.choice(chars) 
    print(passwords)   

    