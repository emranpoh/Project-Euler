print("Problem 19 : Counting Sundays\n")

day = 1
day_counter = 0
month = 1
year = 1900

sunday_counter = 0

month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

while (year != 2001):

    if((year%4 == 0)or(year%400 == 0)):
        month_days[1] = 29
    else :
        month_days[1] = 28
    if(day == 1 and day_counter == 7):
        print(month_names[month-1] + " " + str(year) + " starts with Sunday")
        sunday_counter += 1


    if day_counter == 7:
        day_counter = 0

    day += 1
    day_counter += 1

    if(day-1 == month_days[month-1]):

        day = 1
        month += 1

        if(month == 13):

            month = 1
            year += 1

print("Answer : ", sunday_counter - 2)
