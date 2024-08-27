import pandas

# Documentation for pandas: https://pandas.pydata.org/docs/

# Pandas has two main data types: Series (1-Dimensional) and DataFrames (2-Dimensional)

data = pandas.read_csv("weather_data.csv")
print(type(data))  # --> this is a DataFrame - Equivalent to a table.
print(type(data["temp"]))  # --> this is a Series - Equivalent to a list.

# I can use different methods to cast the DataFrame to a Dict, Array or whatever.
data_dict = data.to_dict()
print(data_dict)

# Coming to the Series:

temp_list = data["temp"].to_list()
print(temp_list)

# Calculating average temp.
list_count = len(temp_list)
list_sum = sum(temp_list)
average = list_sum/list_count
print(round(average, 2))

# Alternative using pandas

print(data["temp"].mean())

# Getting the max value of temp

print(data["temp"].max())

# For now, I accessed a column bei data["column_name"]. I could also use data.column_name. Panda takes the column names
# and convert them to attributes of the dataframe.

print(data.condition)
