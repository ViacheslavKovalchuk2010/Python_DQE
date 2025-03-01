import re

# Input the text to be processed
text = """homEwork:
tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


# Normalize the text to lowercase and correct 'iz' to 'is' where it is needed
result_text = text.lower().replace('iz ', 'is ')

# Split the text into paragraphs using '\n' to make the paragraph for each line
split_text = result_text.split('\n')

# Create an empty lists to store processed paragraphs and last words
paragraphs_list = []
last_words = []

# Loop through each paragraph in the split text
for paragraph in split_text:
    # Check if paragraph is not empty
    if paragraph:
        # The paragraph is split at positions where a sentence-ending punctuation mark is immediately followed by one or
        # more whitespace characters
        sentences = re.split(r'(?<=[.!?])\s+', paragraph)
        # Create a list to gather capitalized sentences
        capitalized_sentences = []

        # Loop through each sentence in the paragraph
        for sentence in sentences:
            # Check if sentence is not empty
            if sentence:
                # Capitalize the first character in the sentence
                capitalized_sentence = sentence.capitalize()
                # Append the capitalized sentence to the list
                capitalized_sentences.append(capitalized_sentence)

                # Split each sentence to the list of words
                words = sentence.split()
                # Avoid the header "homework:" to be added to the list of the last words
                if words and words[-1] != "homework:":
                    # Remove any trailing punctuation marks like period (.!?,;), add last cleaned-up word to last_words
                    last_words.append(words[-1].strip(".!?,;"))

        # Join the sentences back to paragraph without adding additional periods
        fixed_text = ' '.join(capitalized_sentences)
        # Append the paragraph to the list of paragraphs
        paragraphs_list.append(fixed_text)


# Construct a new sentence from last words and capitalize the first letter
new_sentence = ' '.join(last_words).capitalize() + '.'
# Join the paragraphs from paragraph_list to a string and add the new sentence preserving the spaces between lines
final_text = '\n\n\n\n'.join(paragraphs_list) + '\n\n\n\n' + new_sentence

# Print the final text
print(f"final text: \"{final_text}\"")


# Count the number of whitespace characters in the original text using isspace() method
whitespace_count = sum(1 for char in text if char.isspace())
# Print the count of whitespace characters
print(f'The actual count of whitespace characters is: {whitespace_count}')








