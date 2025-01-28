import random
print("Welcome to random password generator!")
randomchars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+"
numofinputs=int(input("How many types of random password you want?:"))
pwdlen=int(input("plesase enter the length of password:"))
print("Here are your random passwords:")
for input in range(numofinputs):
    pwd=""
    for chars in range(pwdlen):
        pwd=pwd+random.choice(randomchars)
    print(pwd)
