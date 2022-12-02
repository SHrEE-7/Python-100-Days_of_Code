from datetime import datetime 
import pandas 
#2 check if today matches a birthday in the birthday.csv
today = datetime.now()
today_tuple = (today.month, today.day)

#3 use pandas to read csv
data = pandas.read_csv("birthday.csv")
birthday_dict = {(data_row["month"],data_row["day"]):data_row for(index,data_row) in data.iterrows()}
# if today_tuple in birthday_dict:
    