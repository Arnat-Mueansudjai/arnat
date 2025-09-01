def fibonacci(n):
    a=0 
    b=1  
    for i in range(n):
        print(a) 
        a=b
        b=b+a


n = int(input("Fibonacci sequence: "))
fibonacci(n)