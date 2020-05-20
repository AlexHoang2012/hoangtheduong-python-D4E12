list = ['bát', 'đũa', 'thìa', 'chén'] 
while True:
    
    print('Mời chọn thao tác: ')
    print('C: Nếu bạn muốn thêm mới vào danh sách.')
    print('R: Nếu bạn muốn in toàn bộ danh sách.')
    print('U: Nếu bạn muốn sửa nội dung trong danh sách.')
    print('D: Nếu bạn muốn xóa một mục trong danh sách.')
    print('Một chữ cái khác bất kỳ để thoát ứng dụng')
    lua_chon = input('Lựa chọn của bạn: ')

    if lua_chon == 'C':
        them = input('Mời nhập thứ muốn thêm vào danh sách: ')
        list.append(them)
    elif lua_chon == 'R':
        for index, value in enumerate(list):
            print(index+1, value)
    elif lua_chon == 'U':
        sua = input('Mời nhập món đỒ bạn muốn sửa: ')
        moi = input('Mời nhập món đỒ bạn muốn sửa thành: ')
        thu_tu_sua = list.index(sua)
        list[thu_tu_sua] = moi
    elif lua_chon == 'D':
        xoa = input('Mời nhập món đồ muốn xóa: ')
        thu_tu_xoa = list.index(xoa)
        list.pop(thu_tu_xoa)
    else:
        print('Cảm ơn bạn đã sử dụng chương trình. ')
        break

    print('Danh sách sau khi cập nhật: ')
    for index, value in enumerate(list):
            print(index +1, value)


