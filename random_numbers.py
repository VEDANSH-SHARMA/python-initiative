import  pandas as pd
import random

i = 1000

data_list = []
columns_list = ['x', 'y', 'z']


for val in range(i):
    data_list.append([random.randint(100, 1000), random.randint(1, 5),random.randint(2, 3)])


df = pd.DataFrame(data_list,columns=columns_list)
df.to_csv("inventory_data_ran_data2", mode='w', index = False)