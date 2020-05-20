# 1
sheep_list = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and these are my sheep sizes")
print(sheep_list)
print()

# print("Now my bigggest sheep has size: ", max(sheep_list), "let's shear it")
# print()

# index = sheep_list.index(300)
# sheep_list[index] = 8
# print("After shearing, here is my flock")
# print(sheep_list)
# print()

# print("One month has passed, now here is my flock")
# for i in range(7):
#     sheep_list[i] = sheep_list[i] + 50
# print(sheep_list)

for i in range (1, 4):
    print("Month", i)

    print("Now my bigggest sheep has size: ", max(sheep_list), "let's shear it")
    
    index = sheep_list.index(max(sheep_list))
    sheep_list[index] = 8
    print("After shearing, here is my flock")
    print(sheep_list)
    

    print("One month has passed, now here is my flock")
    for i in range(7):
        sheep_list[i] = sheep_list[i] + 50
    print(sheep_list)
    print()

print ("My flock has size in total: ", sum(sheep_list))
print ("I would get ",sum(sheep_list),"* 2$ = ",sum(sheep_list)*2,"$")