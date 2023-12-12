def main():
  employee = str(input("What is the employees name? "))
  
  hours_worked = float(input("How many hours has the employee worked? "))
  
  
  pay_rate = float(input("What is the employees pay rate? "))
  
  print("-"*30)
  if hours_worked >40:
    overtime = hours_worked - 40
  else:
      overtime = 0
   
  overtime_Pay = overtime * (pay_rate * 1.5)
    
  
  reg_pay = (hours_worked - overtime) * pay_rate
  gross_pay = reg_pay + overtime_Pay
  


  
  print("Employee name:\t ", employee)
  print("")
  print("Hours Worked\t","Pay Rate\t", "Overtime\t", "Overtime Pay\t", end="") 
  print("Regular Pay\t", "Gross Pay")
  print("-"*80)
  print(f'{hours_worked:<20} {pay_rate:<10} {overtime:<10}', end = '')
  print(f'{overtime_Pay:<15.2f} {reg_pay:<10.2f} {gross_pay:<10.2f} ')  
main()
