# CTI-110
# M3 LAB1 - LEAP YEAR
# BlanchardIan
# 9/21/23

# Calculate if a leap year is a leap year

#LEap years are::
#Divisible by four unless its a century, then it's divisible by 400

# TODO: Handle the century case

is_leap_year = False

print("What year to check")
year= int(input())

# If the year is divisible by 4, it is a leap year
# We use the modulas (%) operator to get the remainder

if year % 4 == 0:
  is_leap_year = True

#Century exception, if it's divisible by 100 then it isnt a leap year
#UNLESS it is also divisible by 400

if year % 100 == 0:
  is_leap_year = False
  if year % 400 == 0:
    is_leap_year = True

if is_leap_year:
  print(year,"is a leap year")
else:
  print(year, "is not a leap year")







