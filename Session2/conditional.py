

# import random
# n=random.randint(0,100)
# print (n)

# if n<20:
#     print("my mood is not goood")
# elif n<60:
#     print ("my mood is good")
# else:
#     print ("I'm very happy")

print ("Giải phương trình bậc 2: ax2 + bx + c")

a = int(input("Mời nhập số a: "))
b = int(input("Mời nhập số b: "))
c = int(input("Mời nhập số c: "))

delta = b**2 - 4 * a * c
print("delta = ", delta)

if delta < 0:
    print("vô nghiệm")
elif delta == 0:
    print("phương trình có một nghiệm: x=", -b/(2*a))
else:
    print("Phương trình có 2 nghiệm: x1=", (-b+delta**1/2)/(a*2),"; x2=",(-b-delta**1/2)/(a*2))
