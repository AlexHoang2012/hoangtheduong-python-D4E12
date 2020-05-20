name = 'trứng rán'
name1 = 'bắp'
name2 = 'bơ'
name3 = 'mỡ'
name4 = 'mắm tôm'

#list, array

mon_an = ['trứng rán', 'bắp', 'mỡ', 'bơ', 'mắm tôm', 'thịt chó']
print(mon_an)
# name = 'củ giềng'
# mon_an.append(name) # Create
# mon_an [6] = 'bạch tuộc' #Update
# # print(mon_an)
# # print('-------------')

# for i in range(len(mon_an)): #ý nghĩa tương đương với câu lệNh bên dưới
#     print(i+1, mon_an (i))

# for index, value in enumerate(mon_an): #['trứng rán', 'bắp', 'mỡ', 'bơ', 'mắm tôm', 'thịt chó']
#     print(index+1, value)

# mon_sua = int(input("Bạn muốn sửa món thứ mấy trong những món trên: "))
# mon_moi = input("Tên món bạn muốn sửa thành: ")
# if mon_sua >len(mon_an)+1:
#     print("Đề nghị nhập số đúng")
# else:
#     mon_an [mon_sua-1] = mon_moi
# print(mon_an)
# print(mon_an.index('thịt chó'))

# mon_sua = input("Bạn muốn sửa món nào trong những món trên: ")
# mon_moi = input("Tên món bạn muốn sửa thành: ")
# index = mon_an.index(mon_sua)
# mon_an[index] = mon_moi
# for index, value in enumerate(mon_an):
#     print(index+1, value)

deleted_item = mon_an.pop() #Delete
print(deleted_item)
