def fib(n):
    if n<0:
        print("enter a valid no")
    elif(n>0):
        a=0#1
        b=1#2
        temp=0#3
        print(a)
        print(b)
        for i in range(n):
            temp=a+b
            print(temp)
            a=b
            b=temp
    
n=int(input("enter"))
fib(n)