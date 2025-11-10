# Bài 1: Tính tổng chi phí và VAT 10%
gia = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))
tong = gia * so_luong
vat = tong * 0.1
tong_tien = tong + vat
print("Tổng tiền trước VAT:", round(tong, 2))
print("Tiền VAT (10%):", round(vat, 2))
print("Tổng tiền phải trả:", round(tong_tien, 2))