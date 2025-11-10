# Bài 4: Chuyển VNĐ sang USD (1 USD = 24.500 VNĐ)
vnd = float(input("Nhập số tiền (VNĐ): "))
usd = vnd / 24500
print("Số tiền tương ứng (USD):", round(usd, 2))