# Recursive function to compute Fibonacci number
# The Fibonacci Sequence is computed based on the following formula: f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Get input from user
n = int(input("Enter the number of terms: "))

# Print Fibonacci sequence
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i), end=" ")
