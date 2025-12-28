with open("nguon.dat", "rb") as src:
    with open("dich.dat", "wb") as dest:
        while True:
            data = src.read(1024)
            if not data:
                break
            dest.write(data)
