# CTI-110
# P4HW2
# Blanchard 
# 10/12/23

DONE_VALUE = ("no")
keep_going = True
stop = ()
nameList = []
overtimeList = []
regularPayList =[]
grossPayList = []


while keep_going == True:

 employee = str(input("Enter the emloyees name: "))
 nameList.append(employee)
 hours_worked = float(input("How many hours has the employee worked? "))
  
  
 pay_rate = float(input("What is the employees pay rate? "))
  
 print("-"*30)
 if hours_worked >40:
    overtime = hours_worked - 40
 else:
      overtime = 0
   
 overtime_Pay = overtime * (pay_rate * 1.5)
 overtimeList.append(overtime_Pay)
  
 reg_pay = (hours_worked - overtime) * pay_rate
 regularPayList.append(reg_pay)
 gross_pay = reg_pay + overtime_Pay
 grossPayList.append(gross_pay)
   


  
 print("Employee name:\t ", employee)
 print("")
 print("Hours Worked\t","Pay Rate\t", "Overtime\t", "Overtime Pay\t", end="") 
 print("Regular Pay\t", "Gross Pay")
 print("-"*80)
 print(f'{hours_worked:<20} {pay_rate:<10} {overtime:<10}', end = '')
 print(f'{overtime_Pay:<15.2f} {reg_pay:<10.2f} {gross_pay:<10.2f} ')  
 print()
 print("Would you like to add another emloyee? Answer yes or no.")
 stop = input()
 print()
 if stop == DONE_VALUE:
    keep_going = False 

nameListLength = len(nameList)
overtimeListSum = sum(overtimeList)
regularPaySum = sum(regularPayList)
grossPaySum = sum(grossPayList)

print("The total number of empolyees entered: \t\t", nameListLength)
print("The total amount paid for overtime: \t\t", overtimeListSum)
print("The total amount paid for reguler hours: \t", regularPaySum)
print("The total gross amount paid: \t\t\t\t", grossPaySum)
# get how many employees were entered

