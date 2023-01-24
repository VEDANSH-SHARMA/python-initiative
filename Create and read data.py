import  pandas as pd
import random

i = 1000

date=['1/1/2019','1/1/2020','1/1/2021','1/1/2022']

data_list = []
columns_list = ['Store Name','Date','Product Category','Profit','Revenue','Basket Value','Customer','Rating']
store_name=[]
with open(r"C:\Users\vedan\Desktop\Priority_Important\SAC\Lulu\Inventory\Store_names.txt") as f:
    store_name=f.readlines()
    store_name= [i.rstrip("\n") for i in store_name ]
print(store_name)
product_Category = ['Grocery', 'Fresh food', 'Electronics', 'Home & Living', 'Lifestyle']
customer_distribution = ['Prime', 'Non Prime']


for val in range(i):
    data_list.append([random.choice(store_name), random.choice(date),random.choice(product_Category),
    random.randint(2000, 10000), random.randint(20000, 99999), random.randint(100, 1000),random.choice(customer_distribution),
    random.randint(1, 10)])

df = pd.DataFrame(data_list,columns=columns_list)
df.to_csv("inventory_Store_data", mode='w', index = False)

