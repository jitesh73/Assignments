def factorial(num):
    fact = 1
    while num > 1:
        fact *= num
        num -= 1

    return fact

n = int(input("Enter the number: "))

fact = factorial(n)

print(f"Factorial of {n} is: {fact}")