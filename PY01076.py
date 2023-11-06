import math

# Hàm để tìm GCD của hai số a và b
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Đọc số lượng bộ test
T = int(input())

# Đọc và xử lý từng bộ test
for _ in range(T):
    a = int(input())
    b = int(input())
    
    # Tìm GCD của a và b
    gcd = find_gcd(a, b)
    
    # In kết quả
    print(gcd)
