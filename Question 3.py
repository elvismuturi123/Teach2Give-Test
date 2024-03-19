



#QUESTION THREE
#Write a program that takes an integer as input and returns true if the input is a power of two.
#Examples: 
#8=> returns true
#6=> returns false


def numberPowerOfTwo(d):
 """Checks if a given integer is a power of two."""

 # Check for negative numbers and zero
 if d <= 0:
   return False

 # Efficient bitwise check for a single set bit
 return d & (d - 1) == 0

# Continuously prompt for input and check for powers of two
while True:
 try:
   number = int(input("Enter an integer : (q to quit): "))
   if number == 'q':
     break
   result = numberPowerOfTwo(number)
   print(f"{number} is a power of two: {result}")
 except ValueError:
   print("Invalid input. Please enter an integer or 'q' to quit.")


   

