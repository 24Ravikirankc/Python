import itertools

# Define the list
numbers = [1, 2, 3]

# Get all permutations
permutations = itertools.permutations(numbers)

# Print each permutation
for p in permutations:
    print(p)
