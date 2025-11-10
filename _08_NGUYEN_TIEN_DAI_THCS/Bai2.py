# Bài 2: Chia kẹo cho học sinh
tong_keo = int(input("Nhập tổng số kẹo: "))
so_hs = int(input("Nhập số học sinh: "))
if so_hs <= 0:
    print("Số học sinh phải lớn hơn 0")
else:
    moi_hs = tong_keo // so_hs
    thua = tong_keo % so_hs
    print("Mỗi học sinh nhận:", moi_hs)
    print("Số kẹo còn thừa:", thua)