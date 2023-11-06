def count_substrings(N, M, s):
    len_s = len(s)
    t = N - len_s + 1
    return t % M

# Đọc số lượng bộ test
T = int(input())

# Xử lý từng bộ test
for _ in range(T):
    N, M = map(int, input().split())
    s = input().strip()
    result = count_substrings(N, M, s)
    print(result)
