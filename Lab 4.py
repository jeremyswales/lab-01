# Function 1: Check if the given number is a proper day number and return "It is a Weekday!" if it is, or "It is a Weekend!" if it is not.
def check_weekday_or_weekend(day_number):
    return 0

day_number=(int(input("what day of the week:")))

if 1<=day_number<=5:
    print("It is a weekday")
elif 6<= day_number <= 7:
    print("It is a weekend")
else:
    print("Not a proper day number")


# Function 2: Check if the given number is a proper day number and return the corresponding day name.
def get_day_name(day_number):
    return 0

name_day=(int(input("what day of the week:")))

if name_day ==1:
    print("It is MOnday")
elif name_day == 2:
    print("It is a Tuesday")
elif name_day ==3:
    print("Its a wednesday")
elif name_day ==4:
    print("It is a thursday")
elif name_day ==5:
    print("It is a friday")
elif name_day ==6:
    print("It is a saturday")
elif name_day ==7:
    print("It is a sunday")
else:
    print("Not a proper day")