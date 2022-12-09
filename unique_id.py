import  pandas as pd
import random

i = 1000

data_list = []
product_Cat = ['GRO', 'FFD', 'ELE', 'HAL', 'LFS']
columns_list = ['Order Id', 'Product Id', 'Product Category']
product_Category = ['Grocery', 'Fresh food', 'Electronics', 'Home & Living', 'Lifestyle']

for val in range(i):
    x =  random.choice(product_Cat)
    y = []

    if x == product_Cat[0]:
        y = product_Category[0]
    elif x == product_Cat[1]:
        y = product_Category[1]
    elif x == product_Cat[2]:
        y = product_Category[2]
    elif x == product_Cat[3]:
        y = product_Category[3]
    elif x == product_Cat[4]:
        y = product_Category[4]


    data_list.append([random.randint(1000, 100000), str(x) + str(random.randint(1000, 100000)), str(y)])


df = pd.DataFrame(data_list,columns=columns_list)
df.to_csv("inventory_data_ids_cat", mode='w', index = False)