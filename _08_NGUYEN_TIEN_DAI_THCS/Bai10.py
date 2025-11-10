# Bài 10: Tính lương thực nhận
luong_cb = float(input("Nhập lương cơ bản: "))
ngay_cong = int(input("Nhập số ngày công: "))

luong_1_ngay = luong_cb / 22
luong_thang = luong_1_ngay * ngay_cong

if ngay_cong > 22:
    thuong = luong_thang * 0.1
    tong = luong_thang + thuong
elif ngay_cong < 22:
    phat = luong_thang * 0.05
    tong = luong_thang - phat
else:
    tong = luong_thang

print("Tổng lương thực nhận:", round(tong, 2))