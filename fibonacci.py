def fib(n):
    a,b = 0,1
    while a < n:
        print (a)
        a,b = b,b+a

n =int(input("enter the count of fibonacci series"))
fib(n)
