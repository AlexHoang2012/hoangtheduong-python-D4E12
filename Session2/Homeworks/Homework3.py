n = int(input("Please input your number: "))
f = 1
if(n==0):
    print("Sorry, this number can't calculate factorial")
else:
    for i in range (1,n+1):
        f = f * i
    
    print("factorial of this number is: ", f)