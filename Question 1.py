



#QUESTION ONE
# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for 
# multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print 
# "FizzBuzz".


# This statement Loops through numbers from 1 to 100
for number in range(1, 101):
  # This statement checks if if the number is divisible by 3 and 5 and replaces with (FizzBuzz)
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  # This statement checks if the number is divisible by 3 and replaces with "Fizz"
  elif number % 3 == 0:
    print("Fizz")
  # This statement checks if the number is divisible by 5 and replaces with "Buzz"
  elif number % 5 == 0:
    print("Buzz")
  # This statement Prints the numbers in continuation
  else:
    print(number)

