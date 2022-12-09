import  pandas as pd
import random

i = 1000

data_list = []
uom = ['', 'FFD', 'ELE', 'HAL', 'LFS']

for val in range(i):

    data_list.append([random.choice(uom)])


df = pd.DataFrame(data_list,columns=columns_list)
df.to_csv("inventory_data_uom", mode='w', index = False)