'''
PURPOSE: This program calculates whether a year is a leap year or not.

AUTHOR: Amber Morgan
'''

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    year = int(input("Enter a year: "))
    leap_year = is_leap_year(year)
    if leap_year:
        print(year, "is a leap year")
    if not leap_year:
        print(year, "is not a leap year")

# All of your code is above these lines
if __name__ == "__main__":
    main()
