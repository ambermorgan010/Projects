"""
FUNCTION: Returns name of the month based on associated number.
AUTHOR: Amber Morgan
"""

month_num = input("What is the month number?: ")
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',' Nov',' Dec']
while not month_num.isdigit() or int(month_num) < 1 or int(month_num) > 12:
    print('Not a valid month number.')
    month_num = input("What is the month number?: ")
print(months[int(month_num) - 1])
