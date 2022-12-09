from faker import Faker
import  pandas as pd
import random

i = 1000
country = 'nl_NL'
data_list = []
fake = Faker(country)
columns_list = ['Id', 'Date', 'Product Category', 'Product Status', 'PostCode' ,'City', 'Country']
product_Category = ['Grocery', 'Fresh food', 'Electronics', 'Home & Living', 'Lifestyle']
product_Status = ['Arrived', 'In-Transit', 'Returned', 'Priority', 'Expired']

for val in range(i):
    data_list.append([fake.unique.random_int(), fake.date_of_birth(), random.choice(product_Category), random.choice(product_Status) , fake.postcode(), fake.city(), 'Bahrain' ])

df = pd.DataFrame(data_list,columns=columns_list)
df.to_csv("inventory_data_Bahrain", mode='w', index = False)