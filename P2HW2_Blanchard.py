'''
Display Ask user to enter grades 
Input Module 1
Input Module 2
Input Module 3
Input Module 4
Input Module 5
Input Module 6
Display Highest Grade
Display Lowest Grade
Display Sum of Grades
Display Average of Grades

Note: Write program Pseudocode (detail algorithm) and add it as a comment block. (10 points)
 '''

# CTI-110
# P2HW2 - List
# Blanchard Ian
# 9-14-23

print("Please enter your test scores for module 1-6.")

print("Enter the score for module 1: ", end="")
mod_1 = float(input())

print("Enter the score for module 2: ", end="")
mod_2 = float(input())

print("Enter the score for module 3: ", end="")
mod_3 = float(input())

print("Enter the score for module 4: ", end="")
mod_4 = float(input())

print("Enter the score for module 5: ", end="")
mod_5 = float(input())

print("Enter the score for module 6: ", end="")
mod_6 = float(input())

my_list = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

print("------------RESULTS------------")
min = min(my_list)
print("Lowest Grade:\t", min, sep="") 

max = max(my_list) 
print("Highest Grade:\t", max, sep="") 


sum = sum(my_list)
print("Sum of Grades:\t", sum, sep="")

avg = sum / len(my_list) 
print(f"Average:\t\t{avg:.2f}", sep="") 


