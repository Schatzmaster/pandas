# with open("weather_data.csv") as weather:
#     data = weather.readlines()
#
# print(data)
#
# # Above puts the data from file in a list, but that looks not so nice. There is an inbuild module 'csv' that can be used
# # to clean up the data
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     # Creates a csv.reader object that can be looped through
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             temperature.append(int(row[1]))
#     print(temperature)

# This is a lot of effort for getting just one value of data. Here, the module pandas comes into play

from pandas import read_csv

data = read_csv("weather_data.csv")
print(data["temp"])

# 3 lines against 8 lines. 
