# import the random library
import random
# import the string library
import string


def generate_random_key():
    """Generates a random key consisting of a letter, digit, or punctuation."""
    # Randomly choose the type of key.
    key_type = random.choice(['letter', 'digit', 'punctuation'])
    # Return a random letter if 'letter' is chosen.
    if key_type == 'letter':
        return random.choice(string.ascii_letters)
    # Return a random digit if 'digit' is chosen.
    elif key_type == 'digit':
        return random.choice(string.digits)
    # Return a random punctuation if 'punctuation' is chosen.
    else:
        return random.choice(string.punctuation)


def generate_random_dict():
    """Generates a random dictionary with alphanumeric keys and random values."""
    # Randomly decide the number of keys (1 to 94 inclusive)
    # 26 lowercase letters, 26 uppercase letters, 10 digits, 32 punctuation marks
    num_keys = random.randint(1, 94)
    # Generate a list of random keys.
    keys = [generate_random_key() for _ in range(num_keys)]
    # Return a dictionary with keys and random values from 1 to 100.
    return {key: random.randint(1, 100) for key in keys}


def create_list_of_dicts(num_dicts):
    """Generates a list of random dictionaries."""
    # Return a list of random dictionaries, of length num_dicts.
    return [generate_random_dict() for _ in range(num_dicts)]


def construct_common_dict(list_of_dicts):
    """Constructs a dictionary with the highest values from the list of dictionaries."""
    # Create an empty dictionary to store the highest values.
    common_dict = {}
    # Iterate through the list of dictionaries with index
    for index, d in enumerate(list_of_dicts):
        # Iterate through key-value pairs of each dictionary
        for key, value in d.items():
            # If the value is greater than the stored one
            if key in common_dict and value > common_dict[key][1]:
                # Update the value and the index
                common_dict[key] = (index + 1, value)
            # If the key is not in the common_dict
            elif key not in common_dict:
                # Store new key with index and value
                common_dict[key] = (index + 1, value)
    # Return the dictionary with the highest values
    return common_dict


def finalize_common_dict(list_of_dicts, common_dict):
    """Finalizes the common dictionary with unique or highest valued keys."""
    # Create an empty dictionary for the final result
    final_dict = {}
    # Iterate through the common_dict
    for key, (dict_number, value) in common_dict.items():
        # Count occurrences of key in all dictionaries
        occurrence_count = sum(key in d for d in list_of_dicts)
        # If key occurs in only one dictionary
        if occurrence_count == 1:
            # Add it to final_dict as it is
            final_dict[key] = value
        # If key occurs in more than one dictionary
        else:
            # Rename key including origin dictionary number
            final_dict[f"{key}_{dict_number}"] = value
    # Return the finalized dictionary
    return final_dict


def main_function():
    # Randomly choose the number of dictionaries (2 to 10)
    num_dicts = random.randint(2, 10)
    # Generate the list of dictionaries
    list_of_dicts = create_list_of_dicts(num_dicts)
    # Print each dictionary
    print("List of random dictionaries:")
    for i, d in enumerate(list_of_dicts):
        print(f"Dict {i + 1}: {d}")

    # Construct common dictionary with the highest values
    common_dict = construct_common_dict(list_of_dicts)
    # Print common dictionary
    print(f"Auxiliary common_dict: {common_dict}")

    # Generate the final dictionary
    final_dict = finalize_common_dict(list_of_dicts, common_dict)
    #  Print the final dictionary
    print(f"Final common dict: {final_dict}")

# Execute the main function to perform all operations
main_function()
