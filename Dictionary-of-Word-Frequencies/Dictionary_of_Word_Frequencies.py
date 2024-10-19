# Dictionary of Word Frequencies
# Name: Sahar Iqbal
# Date: 10/19/2024

def word_frequencies():
    # Ask the user for a sentence
    sentence = input("Please enter a sentence: ")
    
    # Split the sentence into words and create a dictionary for frequencies
    words = sentence.split()
    frequency_dict = {}
    
    # Loop through each word in the list of words
    for word in words:
        # Normalize the word to lowercase to count 'Word' and 'word' as the same
        word = word.lower()
        # Update the frequency count in the dictionary
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
            
    # Print the resulting dictionary
    print(frequency_dict)

# Example usage
word_frequencies()

