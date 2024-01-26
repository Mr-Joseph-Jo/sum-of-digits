def add(n):
    x=0
    while(n>0):
        a=n%10
        x=x+a
        n=n//10
    else:
        print(x)
n=int(input("enter"))
add(n)
