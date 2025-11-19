import math

tu = int(input("Tử số: "))
mau = int(input("Mẫu số: "))

g = math.gcd(tu, mau)

print("Phân số tối giản:", tu//g, "/", mau//g)
