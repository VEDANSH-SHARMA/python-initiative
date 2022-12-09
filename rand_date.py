from datetime import date, timedelta
from random import choices
import pandas as pd
# initializing dates ranges
test_date1, test_date2 = date(2022, 11, 15), date(2022, 12, 8)

# printing dates
print("The original range : " + str(test_date1) + " " + str(test_date2))

# initializing K
K = 1

res_dates = [test_date1]

# loop to get each date till end date
while test_date1 != test_date2:
    test_date1 += timedelta(days=1)
    res_dates.append(test_date1)

# random K dates from pack
res = choices(res_dates, k=K)

# printing
print("K random dates in range : " + str(res_dates))

i = 1
data_list = []
columns_list = ['x']


for val in range(i):
    res = choices(res_dates, k=i)
    data_list.append([res_dates])


df = pd.DataFrame(data_list,columns=columns_list)
df.to_csv("inventory_data_date", mode='w', index = False)