'''

CTI-110
P3LAB2 - Grades
Blanchard Ian
9/28/23

'''


def main ():

  num_grade = int(input("What's the number grade? "))
  if (num_grade >= 90 and num_grade <= 100):
    letter_grade = "A"
    print("Your grade is a", letter_grade)
  elif (num_grade >= 80 and num_grade < 90):
    letter_grade = "B"
    print("Your grade is a", letter_grade)
  elif (num_grade >= 70 and num_grade < 80):
    letter_grade = "C"
    print("Your grade is a", letter_grade)
  elif (num_grade >= 60 and num_grade < 70):
    letter_grade = "D"
    print("Your grade is a", letter_grade)
  elif (num_grade >= 0 and num_grade < 60):
    letter_grade = "F"
    print("Your grade is a", letter_grade)
  else:
    print("Sorry thats not a correct entry.")

main()
  
  
  