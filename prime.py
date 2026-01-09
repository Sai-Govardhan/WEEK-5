#24331A05I6

#without recursion
n=int(input("Enter a number to check prime or not(without recursion) : "))
count=0
for i in range(2,n):
    if(n%i==0):
        count+=1
        break
if(count==0):
    print(n,"is a prime number")
else :
    print(n,"is not a prime number")

#with recursion
def prime(n,i=2) :
    if n<=1 :
        return 0
    if i*i>n :
        return 1
    if n%i==0 :
        return 0
    return prime(n,i+1)
n=int(input("Enter a number to check prime or not(with recursion) : "))
if(prime(n) == 1) :
    print(n,"is a prime number")
else :
    print(n,"is not a prime number")
