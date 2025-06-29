# Write a program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=1
def f(n):
    if n == 0:
        return 1
    else:
        return f(n - 1) + 100

# Get input from user
n = int(input("Enter a non-negative integer: "))

# Compute and display result
print(f"f({n}) =", f(n))
