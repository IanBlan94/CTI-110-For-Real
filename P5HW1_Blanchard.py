# CTI-110 
 # P5HW1 - Math Quiz
 # Ian Blanchard
 # Date

import random 

def main():

  print("WELCOME TO MATH QUIZ!")
  print("")
  print("")
  print("MAIN MENU")
  print("-"*25)
  print("1. Adding Random Numbers")
  print("2. Subtracting random numbers")
  print("3. Exit")
  choice = input("Choose a number from the menu: ")
  if choice == '1':
    random_add()
  elif choice == '2':
    subtraction()
  elif choice == '3':
    exit()
  else:
    print("")
    print("Thats not a valid choice")
    print("Please try selecting again")
    print("")
    
    main()
 

def random_add():
  num1 = random.randint(1, 100)
  num2 = random.randint(1, 100)
  print(num1, "+", num2)
  sol = num1 + num2
  print("Please enter the solution to the followng problem")
  solution = int(input())
  while solution != sol:
    if solution > sol:
      print("Your solution is too high.")
      print("Please try again.")
      solution = int(input())
    elif solution < sol:
      print("Your solution is too low")
      print("Please try again.")
      solution = int(input())
      
  print("You got it! Would you like to do another subtraction problem?")
  print("")
  print("Enter 'yes' to continue, or enter 'no' to go to the main menu ")
  yes = input()
  print("")
  if yes == "yes":
     random_add()
  else:
     main()



def subtraction():
  num1 = random.randint(1, 100)
  num2 = random.randint(1,100)
  print(num1, "-", num2)
  sol = num1 - num2
  print("Please enter the solution to the followng problem")
  solution = int(input())
  while solution != sol:
    if solution > sol:
      print("Your solution is too high.")
      print("Please try again.")
      solution = int(input())
    elif solution < sol:
      print("Your solution is too low")
      print("Please try again.")
      solution = int(input())
    
  print("You got it! Would you like to do another subtraction problem?")
  print("Enter 'yes' to continue, or enter 'no' to go to the main menu ")
  yes = input()
  print("")
  if yes == "yes":
    subtraction()
  else:
     main()




def exit():
  print("Have a good day")
  

main()
