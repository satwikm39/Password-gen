import random
import webbrowser
chars='abcdefghijklmnopqrstuvwxyz1234567890'
times=input('How many passwords do you want?')
length=input('Password length?')
times=int(times)
length=int(length)
for i in range(times):
    password=''
    for i in range(length):
        password+=random.choice(chars)
    print(password)
print('\n')
check=input('Do you want to check how secure your password is?(yes/no)')
if check=='yes':
    webbrowser.open("howsecureismypassword.net")
    
