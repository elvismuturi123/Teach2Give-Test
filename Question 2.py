



#QUESTION TWO
# Write a program to generate the Fibonacci sequence up to 10


# Define a function to generate the Fibonacci sequence
def fibonacci(m):
  
  # This code Initialize the first two numbers in the sequence
  x, y = 0, 1
  
  # Create an empty list to store the numbers in the sequence
  fibonacci_sequence = []
  
  while y <= m:
    # This code Appends the current number (y) to the sequence list
    fibonacci_sequence.append(y)
    
    # Update the next two numbers in the sequence
    x, y = y, x + y
    # In this piece of code, whereby x becomes the previous y and  b becomes the sum of x and y

  # This piece of code Returns the generated Fibonacci sequence
  return fibonacci_sequence

# Generates the Fibonacci sequence up to 100
fibonacci_sequence = fibonacci(100)

# This piece of code Print the generated Fibonacci sequence
print(fibonacci_sequence)

