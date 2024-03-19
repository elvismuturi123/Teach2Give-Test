# QUESTION FIVE

#Write a program that takes an integer as input and returns an integer with reversed digit 
#ordering.
#Examples:
#For input 500, the program should return 5.
#For input -56, the program should return -65.
#For input -90, the program should return -9.
#For input 91, the program should return 19.

def reverse_integer(num):
    # Convert the integer to a string and reverse it
    reversed_str = str(num)[::-1]
    
    # Remove leading zeros if any
    reversed_str = reversed_str.lstrip('0')
    
    # Check if the original number was negative
    if num < 0:
        # Remove the '-' sign from the end and add it back to the beginning
        reversed_str = '-' + reversed_str[:-1]
    
    # Convert the reversed string back to an integer and return it
    return int(reversed_str)

# Prompt the user to enter a number
input_num = int(input("Enter a number: "))

# Call the function to reverse the input number
reversed_num = reverse_integer(input_num)

# Print the reversed number
print("Reversed number:", reversed_num)


