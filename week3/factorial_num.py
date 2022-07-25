

def num_factorial(n):
    if n == 0:
        return 1
    else:
        return num_factorial(n-1) * n


result = input("Enter a number to find the factorial of it:")
result = int(result)
print(num_factorial(result))