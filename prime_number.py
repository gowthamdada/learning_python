#function to check the prime number

def checkforprime(n):
    for i in range (2,n//2+1):
        if n%i == 0:
            return False
        return True

n = int(input("enter the number"))

if checkforprime(n) == False:
    print("not a prime number", n)
else:
    print ("prime number", n)
