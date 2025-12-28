import os

# Tạo thư mục gốc
os.makedirs("my_project/src", exist_ok=True)
os.makedirs("my_project/docs", exist_ok=True)
os.makedirs("my_project/data", exist_ok=True)

# Tạo các tập tin rỗng
open("my_project/src/main.py", "w").close()
open("my_project/docs/README.md", "w").close()
open("my_project/data/input.txt", "w").close()

# In cấu trúc thư mục
print("my_project:")
for folder in os.listdir("my_project"):
    print("-", folder)
    path = os.path.join("my_project", folder)
    if os.path.isdir(path):
        for file in os.listdir(path):
            print("   +", file)
