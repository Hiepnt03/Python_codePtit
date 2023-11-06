import struct

# Đọc dữ liệu từ tệp nhị phân và chuyển thành danh sách số nguyên
def read_binary_file(file_name):
    with open(file_name, 'rb') as file:
        data = file.read()
        int_list = struct.unpack('i' * (len(data) // 4), data)
        return int_list

# Tìm số không giảm trong danh sách và đếm số lần xuất hiện
def find_non_decreasing_numbers(int_list):
    result = {}
    for num in int_list:
        num_str = str(num)
        if num_str == ''.join(sorted(num_str)):
            result[num] = result.get(num, 0) + 1
    return result

# Đọc dữ liệu từ hai tệp nhị phân
list1 = read_binary_file('DATA1.in')
list2 = read_binary_file('DATA2.in')

# Tìm các số không giảm và số lần xuất hiện trong từng danh sách
non_decreasing_numbers1 = find_non_decreasing_numbers(list1)
non_decreasing_numbers2 = find_non_decreasing_numbers(list2)

# Tìm các số không giảm xuất hiện trong cả hai danh sách
common_numbers = set(non_decreasing_numbers1.keys()) & set(non_decreasing_numbers2.keys())

# Sắp xếp các số và in kết quả
common_numbers = sorted(common_numbers)
for num in common_numbers:
    count1 = non_decreasing_numbers1[num]
    count2 = non_decreasing_numbers2[num]
    print(f"{num} {count1} {count2}")
