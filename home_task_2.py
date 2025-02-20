# import the numpy library
import numpy as np
# import the random library
import random
# import the string library
import string

# Generate random number of dictionaries from 2 to 10 inclusive
num_dicts = np.random.randint(2, 11)

# Create an empty list to store the result
list_of_dicts = []

# Loop over the dictionaries
for _ in range(num_dicts):
    # Generate a random number of keys for each dictionary (1 to 26 inclusive, English alphabet has 26 letters)
    num_keys = np.random.randint(1, 27)
    # Generate keys as a lower case alphabets
    keys = random.sample(string.ascii_lowercase, num_keys)
    # Generate a dictionary with the keys and random values from 1 to 100 inclusive for each key
    random_dict = {key: np.random.randint(0, 101) for key in keys}
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
    # Create a list to store the key from each dictionary in list_of_dicts and calculate the number of keys
    if len([d[key] for d in list_of_dicts if key in d]) == 1:
        # If key is present in only one dictionary, use it directly
        final_dict[key] = value
    else:
        # For shared keys, rename the key with the dictionary number having the max value
        final_dict[f"{key}_{dict_number}"] = value

# Print the list of dictionaries and the final combined dictionary
print(f"Final common dict: {final_dict}")
