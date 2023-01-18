def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Tidak bisa membagi dengan 0.")
    else:
        print("Hasilnya adalah: ", result)
    finally:
        print("Aksi selesai")


divide(10, 2)   # Hasilnya adalah: 5.0, Aksi selesai
divide(10, 0)   # Tidak bisa membagi dengan 0., Aksi selesai