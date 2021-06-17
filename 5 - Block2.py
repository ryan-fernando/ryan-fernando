# #I
# #csv file starts off in downloads folder
 
# #II
# #move csv file to month_folder
def get_month_and_year():
    from datetime import date
    today = date.today()

    d4 = today.strftime("%m/%d/%y")

    global month_num
    month_num = int(d4[:2]) 
    global year
    year = 2000 + int(d4[6:])

    global month_name
    month_name = {
            1 : 'January',
            2 : 'February',
            3 : 'March',
            4 : 'April',
            5 : 'May',
            6 : 'June',
            7 : 'July',
            8 : 'August',
            9 : 'September',
            10 : 'October',
            11 : 'November',
            12 : 'December', 
        }

    global month
    month = month_name[month_num]

get_month_and_year()

import shutil
original_file_path ="C:\\Users\\ACER\\Downloads\\cibc.csv" 

target_file_path = f"C:\\Users\\ACER\\Desktop\\Budget_&_Expense_Tracker\\{month}\\cibc.csv" 

shutil.move(original_file_path,target_file_path)

#III
#add heading to csv file
path = f'C:\\Users\\ACER\\Desktop\\Budget_&_Expense_Tracker\\{month}\\cibc.csv'
path1 = r'C:\Users\ACER\Downloads\cibc.csv'

import pandas as pd

file = pd.read_csv(path)

header_names = ['Date', 'Description', 'Credit', 'Debit', 'Account Number']

df = pd.read_csv(path, header = None, skiprows=0, names = header_names)

# print(df.head())
df.to_csv(path, index = None)

#IV
#convert csv file to xlsx format

path1 = f'C:\\Users\\ACER\\Desktop\\Budget_&_Expense_Tracker\\{month}\\cibc.csv'
path2 = f'C:\\Users\\ACER\\Desktop\\Budget_&_Expense_Tracker\\{month}\\cibc.xlsx'

import pandas as pd
readfile = pd.read_csv(path1)
readfile.to_excel(path2, index = None, header = False)

#V
#rename the xlsx file according to format

import os

account_type = 'Visa' 
filename = f'CIBC_{account_type}_{month_name[month_num]}_{year}.xlsx'

path3 = f'C:\\Users\\ACER\\Desktop\\Budget_&_Expense_Tracker\\{month}\\{filename}'

os.rename(path2, path3)

#VI
#delete the csv file from the month_folder

os.remove(path1)