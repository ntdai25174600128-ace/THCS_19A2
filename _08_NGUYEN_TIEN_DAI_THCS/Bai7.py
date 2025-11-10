# Bài 7: Kiểm tra quyền truy cập
user = input("Nhập tên đăng nhập: ")
password = input("Nhập mật khẩu: ")

if user == "admin" and password != "password123":
    print("Truy cập thành công")
else:
    print("Truy cập bị từ chối")