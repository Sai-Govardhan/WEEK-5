#24331A05I6

#with recursion
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

n = int(input("Enter a number: "))
print("Factorial of",n, "is (with recursion) : ",fact(n))

#without recursion
n = int(input("Enter a number: "))
fact = 1
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    for i in range(1, n + 1):
        fact*= i
    print("Factorial of",n, "is (without recursion) : ",fact)
