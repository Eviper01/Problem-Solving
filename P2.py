def Fib(x):
    if x ==1:
        return 1
    if x ==2:
        return 2
    else:
        return Fib(x-1)+Fib(x-2)
total=0
x = 1
while Fib(x)<4*10**6:
    if Fib(x)%2==0:
        total+=Fib(x)
    x+=1
print(total)
