# In this project we will be running a program to determine the budget leftover after expenses and then organize the output
# 9-14-2023
# CTI-110 P2HW1 - Travel Expense Sheet 2
# Ian Blanchard

# display what this program will do
print('This program calculates and displays trip expenses.')

print('In the following texts you are to answer a series', end='') 
print(' of questions.')

print()

# ask user for their budget
print('What is your budget for this trip: ', end = '')
budget = float(input())

# ask user where they will be traveling
print('Where will You be Traveling: ', end = '')
travel = input()

# ask user how much will be spent on gasoline
print('How much will you spend on gas: ', end = '')
gas = float(input())

# ask user how much they will spend on room/board
print('Approximately, how much will you need for room/board: ', end = '')
board = float(input())

# ask user how much money they will spend on food
print('Lastly, how much money will you spend on food: ', end = '')
food = float(input())

# display the users input
print('----------Travel Expenses----------')

print('Traveling To:\t', travel)
print('Initial Budget:\t', budget, sep='$')
print('Fuel Expense:\t', gas, sep='$')
print('Room & Board:\t', board, sep='$')
print('Food Expense:\t', food, sep='$')

#subtract the expenses from the total budget
remaining = budget - gas - board - food 

# display the final balance after expenses

print('Your remaining balance after expenses is ', remaining, sep='$')
print('Enjoy your trip to', travel)

