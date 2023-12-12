DAYS_IN_WEEK = 5
totalHours = 0 #  the total starts at zero
 
print("Please enter your hours worked.")
 
for day in range(DAYS_IN_WEEK):
    print("Hours for day", day+1, ": ", end="")
    hoursToday = float(input())
    totalHours = totalHours + hoursToday # add to running total
 
# print the total
print("You worked a total of", totalHours, "hours this week.")
 
# print the average
avgHours = totalHours / DAYS_IN_WEEK
print("For an average of", format(avgHours, "0.2f"), "hours per day.")