# Bài 9: Tính tiền điện theo bậc
so_kw = int(input("Nhập số kWh điện: "))

if so_kw <= 0:
    tong_tien = 0
elif so_kw <= 100:
    tong_tien = so_kw * 1678
elif so_kw <= 200:
    tong_tien = 100 * 1678 + (so_kw - 100) * 1734
else:
    tong_tien = 100 * 1678 + 100 * 1734 + (so_kw - 200) * 2014

print("Tổng tiền điện phải trả:", tong_tien, "VNĐ")