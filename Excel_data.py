import pandas as pd
import random
import csv
data=pd.read_excel("./Prod_group.xlsx")
print(data)
#print(data['Product Category'])
#print(data['Product Group'])
l=["Men's Formal","Womens's Formal","Kids","Men's Informal","Womens's Informal"]
g=["Bakery","Frozen","Beverage","Deli","Non Food"]
f=["Dairy","Fruits","Vegetables","Meat","Sea food"]
h=["Appliances","Decor","Furnishing","Lighting","Garden"]
e=["Mobiles","Wearables","TVs","Computers","Laptops"]
columns_list = ['Product Group']
data_list = []
for i in data['Product Category']:
    if i == 'Lifestyle':
        r=random.randint(0,4)
        data_list.append(l[r])
    elif i == 'Grocery':
        r=random.randint(0,4)
        data_list.append(g[r])
    elif i == 'Fresh food':
        r=random.randint(0,4)
        data_list.append(f[r])
    elif i == 'Home & Living':
        r=random.randint(0,4)
        data_list.append(h[r])
    elif i == 'Electronics':
        r=random.randint(0,4)
        data_list.append(e[r])
    else:
        pass

df = pd.DataFrame(data_list,columns=columns_list)
df.to_csv("dummy data pG", mode='w', index = False)
