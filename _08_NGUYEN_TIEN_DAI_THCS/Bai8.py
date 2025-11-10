# Bài 8: Tính BMI
can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))
if chieu_cao <= 0:
    print("Chiều cao phải lớn hơn 0")
else:
    bmi = can_nang / (chieu_cao ** 2)
    print("Chỉ số BMI:", round(bmi, 2))