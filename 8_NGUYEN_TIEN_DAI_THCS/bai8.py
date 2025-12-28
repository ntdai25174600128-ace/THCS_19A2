import os

# 1. Tạo thư mục temp_files
os.mkdir("temp_files")

# 2. Tạo file.txt trong temp_files
with open("temp_files/file.txt", "w") as f:
    f.write("Nội dung mẫu")

# 3. Đổi tên file.txt thành new_file.txt
os.rename("temp_files/file.txt", "temp_files/new_file.txt")

# 4. Di chuyển new_file.txt ra thư mục hiện tại
os.rename("temp_files/new_file.txt", "new_file.txt")

# 5. Xóa thư mục temp_files
os.rmdir("temp_files")
