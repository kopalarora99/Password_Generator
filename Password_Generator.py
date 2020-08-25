import random
omit=[';',':']
letters=[chr(i) for i in range(35,125) if chr(i) not in omit]
password=" "
Length=int(input("Enter the length"))
random.choice(letters)
for i in range(0,Length):
    password=password+random.choice(letters)
print(password)

