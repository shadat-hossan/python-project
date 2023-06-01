#A simple age calculating app on python

from datetime import  datetime

now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")

print("Age calculating app")

brithYear = int(input("Enter The birth Year (2000):- "))
brithMonth = int(input("Enter The birth Month (03):- "))

year = int(year)
month = int(month)

if(brithYear<year):
    if(brithMonth<month):
        X = year - brithYear
        Y = month - brithMonth
        print(f"Your age is {X} year and {Y} month")
    else:
        X = (year - brithYear) - 1
        Y = 12 - (brithMonth - month)
        print(f"Your age is {X} year and {Y} month")
else:
    print("Input is wrong please check your birth date and try again...")
