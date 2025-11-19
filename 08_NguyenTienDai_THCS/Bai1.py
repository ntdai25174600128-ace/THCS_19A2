import math

n = int(input("Nhập n: "))

r = int(math.sqrt(n))

if r * r == n:
    print(n, "là số chính phương")
else:
    print(n, "không phải số chính phương")