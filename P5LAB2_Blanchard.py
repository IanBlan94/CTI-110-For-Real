# CTI-110
# Blanchard Ian 
# P5LAB2- More Functions
# 11/2/23

# First, print a table of squares

def main():
  print("PFT2 - Squares")
  print("number\t\tnumber squared")
  for num in range(1, 11):
    num_square = square(num)
    print_row(num, num_square)

def square(number):
  square = number * number
  return square
def print_row(num, num_square):
  print(num, "\t\t", num_square)

main()