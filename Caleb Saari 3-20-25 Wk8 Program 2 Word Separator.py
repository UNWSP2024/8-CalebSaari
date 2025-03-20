# Write a program that accepts as input a sentence in which all of the words are run together
# but the first character of each word is uppercase.
# Convert the sentence to a string in which the words are separated by spaces, and the first word starts with an uppercase.
# For example the string "RunningDistanceIsFun!" would be converted to "Running distance is fun!"



def format_sentence(runned_together):
    words = []
    current_word = ''

    for char in runned_together:
        if char.isupper() and current_word:
            words.append(current_word)
            current_word = char
        else:
            current_word += char
    words.append(current_word)  # Append the last word

    formatted_sentence = ' '.join(words).capitalize()
    return formatted_sentence

# Example usage
input_sentence = "RunningDistanceIsFun!"
output_sentence = format_sentence(input_sentence)
print(output_sentence)  # Output: "Running Distance is Fun!"

# Caleb Saari 3/20/25 Wk8 Program 2: Word Separator