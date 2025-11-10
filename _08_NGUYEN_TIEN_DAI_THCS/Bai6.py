# Bài 6: Kiểm tra năm nhuận
nam = int(input("Nhập năm: "))
if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print("Năm", nam, "là năm nhuận")
else:
    print("Năm", nam, "không phải năm nhuận")