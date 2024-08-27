import pandas

# Pandas has two main data types: Series (1-Dimensional) and DataFrames (2-Dimensional)

data = pandas.read_csv("weather_data.csv")
print(type(data)) # --> this is a DataFrame - Equivalent to a table.
print(type(data["temp"])) # --> this is a Series - Equivalent to a list.

data_dict = data.to_dict()
print(data_dict)