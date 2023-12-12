'''
Get number of tests to be graded
Enter scores for tests
Scores are entered into a list
The lowest score is displayed and then deleted from the list
Displays the modified list
Displays the average of the list
Displays the grade recieved from the average
'''
# CTI-110
# P4HW1 - Score list
# Blanchard Ian
# 10/10/23

DAYS_IN_WEEK = int(input("How many scores do you want to enter? "))
score = [] #  the total starts at zero

 
for days in range(DAYS_IN_WEEK):
    print("Enter the score for test", days + 1, ": ", end="")
    test_score = int(input())
    while test_score >100 or test_score < 0:
      print("Ivalid input, please try again with a value of 0-100")
      print("Enter the score for test ", days + 1, "again: ", end="")
      test_score = int(input())
    score.append(test_score)

  


lowest = min(score)
print("-"*20, "Results", "-"*20)
print("Lowest score: \t", lowest)
score.remove(lowest)
print("Modified list: \t", score)
sum = sum(score)
avg = sum / len(score)
print(f"Scores average:\t {avg:.2f}")

if avg >= 90:
  print('Your grade is:\t A')
elif(avg>=80):
    print('Your grade is:\t B')
elif(avg>=70):
  print('Your grade is:\t C')
elif(avg>=60):
  print('Your grade is:\t D')
else:
  print('Your grade is:\t F')

 