numbers = [1, 3, 5, 7, 9, 11]

with open("so_nguyen.txt", "w") as f:
    for num in numbers:
        f.write(str(num) + "\n")
