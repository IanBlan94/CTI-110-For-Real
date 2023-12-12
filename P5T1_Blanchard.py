# CTI-110
# P5T1- Functions'
# Blanchard Ian 
# 10/24/23


def main():
  print("Hello world!")
  burger = 4.997
  print_money(burger)
  print_money(12)
  print_money(0.3)
# Main ends when indentation stops
def print_money(amount):
  print("$", format(amount, ".2f"))

main()