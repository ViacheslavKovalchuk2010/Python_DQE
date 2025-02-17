# importing the numpy library
import numpy as np

# generating the list of 100 random numbers from 0 to 1000 inclusive
rand_numbers = np.random.randint(0, 1001, size=100).tolist()


# Iterate over each index 'i' for the elements in the rand_numbers list
for i in range(len(rand_numbers)):
    # Iterate over each index 'j', starting from 'i+1' to the end of the list
    for j in range(i+1, len(rand_numbers)):
        # Compare element at index 'i' with element at index 'j'
        if rand_numbers[i] > rand_numbers[j]:
            # If element at 'i' is greater, swap with element at 'j'
            rand_numbers[i], rand_numbers[j] = rand_numbers[j], rand_numbers[i]

# Create the empty list to store even numbers
even_numbers = []
# Create the empty list to store odd numbers
odd_numbers = []

# take each element in the list rand_numbers
for num in rand_numbers:
    # check if the element is divisible by 2 without remainder
    if num % 2 == 0:
        # store the element to the list even_numbers
        even_numbers.append(num)
    # if the element is not divisible by 2 without remainder
    else:
        # store the element to the list even_numbers
        odd_numbers.append(num)

# calculate the average for even numbers, if the list even_numbers is empty even_avg = 0 (to avoid division by 0)
even_avg = sum(even_numbers) / len(even_numbers) if even_numbers else 0
# calculate the average for odd numbers, if the list odd_numbers is empty odd_avg = 0 (to avoid division by 0)
odd_avg = sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0

# print the average for even numbers
print(f"Average of even numbers: {even_avg}")
# print the average for odd numbers
print(f"Average of odd numbers: {odd_avg}")
