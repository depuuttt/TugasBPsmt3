import sys

newLine = "\n"


def userInput():
    nim = input("NIM  : ")
    nama = input("Nama : ")
    data = [nim, nama]
    return data


def selectionPrint():
    print("Pilihan")
    print("1. Cappuccino")
    print("2. Teh")
    print("3. Exit")
    print(newLine)
    data = input("Masukkan Pilihan :")
    return int(data)


def selectionProcess(x):
    match x:
        case 1:
            print("Memilih Cappuccino")
            print(newLine)
            price = int(input("Masukkan Harga : "))
            ppn = 10 / 100 * price
            totalPrice = price + ppn
            print(newLine)
            print("Jumlah yang harus dibayar sebesar Rp " + str(totalPrice) + ",-")
        case 2:
            print("Memilih Teh")
            print(newLine)
            price = int(input("Masukkan Harga : "))
            ppn = 10 / 100 * price
            totalPrice = price + ppn
            print(newLine)
            print("Jumlah yang harus dibayar sebesar Rp " + str(totalPrice) + ",-")
        case 3:
            print("Terimakasih! ^_^")
            sys.exit()


buyerData = userInput()
choose = selectionPrint()
selectionProcess(choose)
