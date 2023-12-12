"""
CTI-110
P1HW1 - Variables
Blanchard Ian
9/5/23

Do some basice output with numbers
1.ask for int
2 square it and then cube it
3. ask for snother int
4. add them and multiply them

"""

# Part One
#variables

first = 0
second = 0

print("Enter integer:")
first = int(input())
print(first, "squared is", first * first)
print("and", first, "cubed is", first * first * first, "!!")

print("Enter another integer")
second = int(input())
print("The total of", first, "and", second, "added is", first + second)
print("The total of", first, "and", second, "multiplied is", first * second)

#Part Two
# Three VAriables
# string - movie name
# int- the year of the movie
# float - the gross (in millions)
# string - a quote
# finally - print a qote from the movie
movie_name = "The Batman"
gross = 771 #million
year = 2023

print("In the year", year, "Robert Pattinson starred in", movie_name, "grossing", gross, "million" )

quote =  "'Fear is a tool. When that light hits the sky, it's not just a call. It's a warning.'"
print("One of the more memorable quotes from the movie is:") 
print(quote)