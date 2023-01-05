import random
import pandas as pd

def r_a():
    i=0
    j=''
    while i < 4:
        randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
        i+=1
        j+=randomUpperLetter
    return j
data_list = []
columns_list = ['ID']
k=10000
for val in range(k):
    data_list.append(r_a())

df = pd.DataFrame(data_list,columns=columns_list)
df.to_csv("inventory_id_test_data", mode='w', index = False)