import calendar
#Function to print the calendar
def print_calender(year, month):
    cal=calendar.month(year, month)
    print(cal)

#Get year and month from user
year=int(input("Enter year: "))
month=int(input("Enter month: "))

print_calender(year,  month)
