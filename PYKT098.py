# Mở file dữ liệu DATA.in
file = open("DATA.in", "r")

# Khởi tạo một danh sách để lưu các nội dung không phải số nguyên
danh_sach = []

# Lặp qua từng dòng trong file
for dong in file:
    # Tách các từ trong dòng
    danh_sach_tu = dong.split()
    # Lặp qua từng từ trong danh sách từ
    for tu in danh_sach_tu:
        # Kiểm tra xem từ có phải là số nguyên hay không
        if(len(tu) > 18):
            danh_sach.append(tu)
        else:
            try:
                # Nếu từ có thể chuyển thành số nguyên, thì bỏ qua
                int(tu)
            except ValueError:
                # Nếu từ không thể chuyển thành số nguyên, thì thêm vào danh sách
                danh_sach.append(tu)

# Đóng file
file.close()

# Sắp xếp danh sách theo thứ tự từ điển
danh_sach.sort()

# In ra danh sách trên một dòng, cách nhau bởi khoảng trống
print(*danh_sach)
