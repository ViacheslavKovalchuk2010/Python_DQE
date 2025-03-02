# import the random library
import random
# import the string library
import string

# Generate random number of dictionaries from 2 to 10 inclusive
num_dicts = random.randint(2, 10)

# Create an empty list to store the result
list_of_dicts = []

# Loop over the dictionaries
for _ in range(num_dicts):
    # Generate a random number of keys for each dictionary (1 to 94 inclusive, the largest group size)
    # 26 lowercase letters, 26 uppercase letters, 10 digits, 32 punctuation marks
    num_keys = random.randint(1, 94)

    # Generate keys
    keys = []
    for _ in range(num_keys):
        # Randomly choose whether to generate a letter, digit or punctuation
        choice = random.choice(['letter', 'digit', 'punctuation'])
        if choice == 'letter':
            key = random.choice(string.ascii_letters)
        elif choice == 'digit':
            key = random.choice(string.digits)
        else:
            key = random.choice(string.punctuation)
        keys.append(key)

    # Generate a dictionary with the keys and random values from 1 to 100 inclusive for each key
    random_dict = {key: random.randint(1, 100) for key in keys}
    # Add dictionary to the list of dictionaries
    list_of_dicts.append(random_dict)

print("List of random dictionaries:")
for i, d in enumerate(list_of_dicts):
    print(f"Dict {i + 1}: {d}")


# Create an empty dictionary
common_dict = {}
# Iterate over each dictionary from the list_of_dicts
for i, d in enumerate(list_of_dicts):
    # Iterate over each key-value pair in the dictionary
    for key, value in d.items():
        # Check if key exists already in common_dict
        if key in common_dict:
            # Extract the dictionary number and its value from the stored value in common_dict
            existing_dict_number, existing_value = common_dict[key]
            # If the current dictionary's value is greater than the stored one, update dict_number and value
            if value > existing_value:
                common_dict[key] = (i + 1, value)
        else:
            # Store the current dictionary number and value as a tuple
            common_dict[key] = (i + 1, value)

print(f"Auxiliary common_dict: {common_dict}")

# Create an empty dictionary to store the final result
final_dict = {}
# Loop through each key-value pair in common_dict, unpacking the tuple
for key, (dict_number, value) in common_dict.items():
    # Check if key is unique across all dictionaries by counting its occurrences. If it appears once, use it directly.
    if len([d[key] for d in list_of_dicts if key in d]) == 1:
        # If key is present in only one dictionary, use it directly
        final_dict[key] = value
    else:
        # For shared keys, rename the key with the dictionary number having the max value
        final_dict[f"{key}_{dict_number}"] = value

# Print the list of dictionaries and the final combined dictionary
print(f"Final common dict: {final_dict}")
