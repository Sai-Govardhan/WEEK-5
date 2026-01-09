#24331A05I6

#with recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter number of terms : "))
print("Fibonacci series (with Recursion) :")
for i in range(n):
    print(fibonacci(i), end=" ")

#without recursion
n = int(input("\nEnter number of terms: "))
a=0
b=1
print("Fibonacci series (without recursion) : ")
for i in range(n):
    print(a, end=" ")
    a,b=b,a+b
