# Define the generator function
def even_numbers(limit):
    for num in range(0, limit + 1):
        if num % 2 == 0:
            yield num

# Accept input from the user
n = int(input("Enter a number: "))

# Generate and print even numbers in comma-separated form
print(",".join(str(num) for num in even_numbers(n)))
