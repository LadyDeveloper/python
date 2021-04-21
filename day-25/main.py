# DATA_LIST = []

# with open("weather_data.csv") as wheater_data:
#     DATA_LIST = wheater_data.readlines()

# print(DATA_LIST)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))

# #Transform the data into a dictionary
# data_dic = data.to_dict()
# #print(data_dic)


# #Transform the data into a list
# temp_list = data["temp"].to_list()

# average_temp = sum(temp_list) /len(temp_list)
# print(average_temp)

# average = data['temp'].mean()
# print(average)

# max_temp = data['temp'].max()
# print(max_temp)

# print(data.temp)

# #Returning row instead of column
# row_data = data[data.day == "Monday"]
# print(row_data)

# #In which day has the maximun temperature
# row_max_temp = data[data.temp == data.temp.max()]
# print(row_max_temp)

  
# # Convert Monday temperture from Celsius to Fahrenheit
# monday = data[data.day == "Monday"]
# temp_fahrenheit = (monday.temp * 9/5) + 32
# print(temp_fahrenheit)

# #Create a DataFrame from scratch
# data_dict = {
#         "students": ["Amy", "Ana", "Jay"],
#         "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


#TODO from squirrel data find the quanntity of each color 
#Primary Fur Color X Count
#grey, red, black
#TODO Read the csv file
squirrel = pandas.read_csv("squirrel.csv")

#TODO count qtt of squirrel per color
grey = squirrel["Primary Fur Color"][squirrel["Primary Fur Color"] == "Gray"].count()
red = squirrel["Primary Fur Color"][squirrel["Primary Fur Color"] == "Cinnamon"].count()
black = squirrel["Primary Fur Color"][squirrel["Primary Fur Color"] == "Black"].count()

#TODO create the dictionary
data_squirrel = {
    "Fur Color": [ "gray", "red" , "black"],
    "Count": [grey, red, black]
}
 #TODO Converting to DataFrame
data = pandas.DataFrame(data_squirrel)
#TODO Converting the DataFrame to csv as squirrel_count.csv
data.to_csv("squirrel_count.csv")