# #1
# for a in range (20):
#     print(a)

# #2
# b = int(input("please enter a number: "))
# for c in range (b):
#     print(c)

# #3
# for i in range(20):
#     if i%2 == 0:
#         print (1, end=" ")
#     else:
#         print(0, end=" ")

#5 
for y in range (1, 10):
    for x in range (1, 10):
        if x*y >= 10:
            print(x*y, end=" ")
        else:
            print(x*y, end="  ")
    print()
