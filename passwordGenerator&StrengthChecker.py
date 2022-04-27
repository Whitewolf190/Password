import random
import re 

userInput = input("Enter the hint: ")
Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
pwd = ""

for i in range(len(userInput)):
    passwordChar = random.choice(Chars)
    pwd += passwordChar

with open('generatedPass.txt', 'w+') as f:
    f.write(pwd)
print("Successfully written in textfile.")

def check(pwd): 
    if pwd == "\n" or pwd == " ": 
        return "Password must not contain a newline or space!"
 
    if 8 <= len(pwd) <= 15: 
        if not re.search('[a-z]', pwd):
            print("Weak Password! At least one lowercase alphabet should be present!")
        elif not re.search('[A-Z]', pwd): 
            print("Weak Password! At least one uppercase alphabet should be present!") 
        elif not re.search('[0-9]', pwd): 
            print("Weak Password! At least one digit should be present!")
        elif not re.search('[_@$]', pwd): 
            print("Weak Password! At least one special char should be present!")
        elif re.search(r'(.)\1\1\1', pwd): 
            print("Weak Password! Char repetition more than 3 times!")
        elif re.search(r'(..)(.*?)\1', pwd): 
            print("Weak Password! String pattern repetition!")
        else: 
            print("The given password is a strong password!")
   
    else: 
        print("Weak Password! Password must be 8 to 15 characters long! ")
        
check(pwd)