"""
CTI-110
P3T2 - Choices & Menus 
Blanchard Ian
9/26/2023

"""


def main():
  print ("-"*10, "Main Menu", "-"*10)
  print("1. Beef")
  print("2. Seafood")
  print("2. Pork")
  
  print("Would you like beef, pork, or seafood ? ", end="")
  choice = str(input())
  print("You chose", choice)

  if choice == "beef":
    option_1()
  
  elif choice == "pork":
    option_2()

  elif choice == "seafood":
    option_3()
  
  else:
    print("Sorry thats not an option.")
  
def option_1():
  print("Youve chosen the beef.")
  print("Would you like to make it a combo, yes or no? ")
  combo = str(input())
  if combo == "yes":
    print("One beef dish with fries and drink coming up!")

  else:
    print("One beef dish coming up!")


def option_2():
  print("Youve chosen the pork.")
  print("Would you like to make it a combo, yes or no? ")
  combo = str(input())
  if combo == "yes":
    print("One pork dish with fries and drink coming up!")

  else:
    print("One pork dish coming up!")

def option_3():
   print("Youve chosen the seafood.")
   print("Would you like to make it a combo, yes or no? ")
   combo = str(input())
   if combo == "yes":
    print("Seafood dish with fries and drink coming up!")

   else:
    print("One seafood coming up!")



# Call function with Name + ()
main()

