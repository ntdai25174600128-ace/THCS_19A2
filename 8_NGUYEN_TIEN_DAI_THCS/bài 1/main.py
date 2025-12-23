from hinh_hoc import chu_vi_hinh_vuong, chu_vi_hinh_tron
canh_vuong = 5
ban_kinh_tron = 3

chu_vi_vuong = chu_vi_hinh_vuong(canh_vuong)
chu_vi_tron = chu_vi_hinh_tron(ban_kinh_tron)

print("=== KẾT QUẢ BÀI 1 ===")
print(f"Chu vi hình vuông có cạnh {canh_vuong}: {chu_vi_vuong}")
print(f"Chu vi hình tròn có bán kính {ban_kinh_tron}: {chu_vi_tron:.2f}")