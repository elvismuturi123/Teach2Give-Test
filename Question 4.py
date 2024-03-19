



#QUESTION FOUR

#Write a program that accepts a string as input, capitalizes the first letter of each word in the 
#string, and then returns the result string.
#Examples: 
#"hi"=> returns "Hi"
#"i love programming"=> returns "I Love Programming

def capitalize_first_letter(input_string):
    # This code Splits the input string into a list of words
    words = input_string.split()
    
    # Initialize an empty string to store the result
    result_string = ""
    
    # Loop through each word in the list
    for word in words:
        # Capitalizes the first letter of the word and concatenate it with the rest of the word
        capitalized_word = word[0].upper() + word[1:]
        
        # Add the capitalized word to the result string
        result_string += capitalized_word + " "
    
    # Remove the space from the result string and return it
    return result_string.strip()

# Loop indefinitely to allow multiple inputs
while True:
    # Prompt the user to input a sentence
    input_string = input("Enter a sentence (press Enter to quit): ")

    # Check if the input is empty (user pressed Enter)
    if input_string == "":
        break

    # Call the function to capitalize the first letter of each word
    result = capitalize_first_letter(input_string)

    # Print the result
    print("Result:", result)
