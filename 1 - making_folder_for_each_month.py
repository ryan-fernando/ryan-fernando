import os

from datetime import date
today = date.today()

d4 = today.strftime("%m/%d/%y")

month = int(d4[:2]) 

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

newpath = r'C:\\Users\\ACER\\Desktop\\Budget_&_Expense_Tracker\\' + month_name[month] 
if not os.path.exists(newpath):
    os.makedirs(newpath)
