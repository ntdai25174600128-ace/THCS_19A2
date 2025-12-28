with open("vanban.txt", "r", encoding="utf-8") as f:
    words = f.read().lower().split()

tan_suat = {}

for word in words:
    tan_suat[word] = tan_suat.get(word, 0) + 1

for word, count in tan_suat.items():
    print(word, ":", count)
