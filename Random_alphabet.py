import random
i=0
j=''
while i < 4:
    randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
    i+=1
    j+=randomUpperLetter
print(j)

