# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperature.append(temp)
# #     print(temperature)   

# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(sum(data["temp"])/len(data["temp"]))

import pandas as pd
data = pd.read_csv("squirrel_data.csv")
gray_count = len(data[data["Primary Fur Color"]=="Gray"])
print(gray_count)
black_count = len(data[data["Primary Fur Color"]=="Black"])
print(black_count)
cinnamon_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
print(cinnamon_count)

count_data = pd.DataFrame()
count_data["Fur Color"] = ["Gray", "Black", "Cinnamon"]
count_data["Count"] = [gray_count, black_count, cinnamon_count]

print(count_data)

count_data.to_csv("count_data.csv")