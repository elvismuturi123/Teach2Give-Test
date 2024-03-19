



#QUESTION SIX
#Write a program that counts the number of vowels in a sentence.
#eg " Hello World " => returns 2


def count_vowels(sentence):
    # DefineS a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Initialize a variable to store the count of vowels/ number of counts
    vowel_count = 0
    
    # Loops through each character in the sentence
    for char in sentence:
        # Check if the character is a vowel (in lowercase)
        if char.lower() in vowels:
            # If it's a vowel, increment the vowel count
            vowel_count += 1
    
    # Return the total count of vowels
    return vowel_count

# Prompts the user to enter a sentence
input_sentence = input("Enter a sentence: ")

# Call the function to count vowels in the sentence
result = count_vowels(input_sentence)

# Print the result
print("Number of vowels in the sentence:", result)
