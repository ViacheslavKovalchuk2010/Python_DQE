# Import the regular expression module
import re

text = """homEwork:
tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix"iZ" with correct "is", but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# Function to lowercase the text
def normalize_text(text):
    # Сonvert the input text to lowercase
    return text.lower()


# Function to correct 'iz ' to 'is '
def correct_iz(text):
    # Replace 'iz ' with 'is ' (but only when 'iz' is a mistake)
    return text.replace('iz ', 'is ')


# Function to capitalize sentence
def capitalize_sentence(sentence):
    # Capitalize the first letter of a sentence
    return sentence.capitalize()


# Function to get the last word of a sentence (excluding punctuation)
def get_last_word(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Check if the sentence has words and the last word is not "homework:"
    if words and words[-1] != "homework:":
        # Remove punctuation from the last word
        last_word_cleaned = words[-1].strip(".!?,;")
        # Return the cleaned last word
        return last_word_cleaned
    # Return None if the sentence is empty or the last word is "homework:"
    return None


# Function to count the number of whitespace characters in the input text
def count_whitespace_characters(text):
    # The expression to count the sum of whitespace characters
    return sum(1 for char in text if char.isspace())




# Function to process the text
def process_text(text):
    # Split the input text into lines (paragraphs)
    split_text = text.split('\n')
    # Initialize empty lists to store processed paragraphs and last words
    paragraphs_list = []
    last_words = []

    # Iterate over each paragraph in the split text
    for paragraph in split_text:
        # Check if the paragraph is not empty
        if paragraph:
            # Normalize the paragraph to lowercase
            normalized_paragraph = normalize_text(paragraph)
            # Correct 'iz' to 'is' where applicable
            corrected_paragraph = correct_iz(normalized_paragraph)
            # Split the corrected paragraph into sentences using regex
            sentences = re.split(r'(?<=[.!?])\s+', corrected_paragraph)
            # Capitalize the first letter of each sentence
            capitalized_sentences = [capitalize_sentence(sentence) for sentence in sentences]
            # Join the capitalized sentences to form the processed paragraph
            paragraph_text = ' '.join(capitalized_sentences)
            # Append the processed paragraph to the paragraphs_list
            paragraphs_list.append(paragraph_text)

            # Iterate over each sentence in the paragraph
            for sentence in sentences:
                # Get the last word of the sentence (excluding punctuation)
                last_word = get_last_word(sentence)
                # Check if a last word was found
                if last_word:
                    # Append the last word to the last_words list
                    last_words.append(last_word)

    # Return the processed paragraphs and the list of last words
    return paragraphs_list, last_words


# Function to add a new sentence to the processed text
def add_sentence(paragraphs_list, last_words):
    # Create a new sentence from the last words
    new_sentence = ' '.join(last_words).capitalize() + '.'
    # Join the paragraphs and add the new sentence
    final_text = '\n\n\n\n'.join(paragraphs_list) + '\n\n\n\n' + new_sentence
    # Return the final text
    return final_text


# Function to get the final result
def main_function():
    # Process the input text
    paragraphs_list, last_words = process_text(text)
    # Add the new sentence to the processed text
    final_text = add_sentence(paragraphs_list, last_words)
    # Print the final text
    print(f"Final text: \"{final_text}\"")
    # Count the whitespace characters in the input text
    whitespace_count = count_whitespace_characters(text)
    # Print the whitespace character count
    print(f'The actual count of whitespace characters is: {whitespace_count}')


main_function()