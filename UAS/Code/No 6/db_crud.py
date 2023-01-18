from db_connect import *


def view_data():
    cursor.execute("SELECT * FROM mahasiswa ORDER BY nim ASC")
    dataMhs = cursor.fetchall()
    for data in dataMhs:
        print("NIM  : ", data[0])
        print("Nama : ", data[1])
        print("IPK  : ", data[2], "\n")


def add_data():
    print("Enter the following data!")
    nim = input("NIM  : ")
    nama = input("Nama : ")
    ipk = input("IPK  : ")

    ipk = float(ipk)

    query = "INSERT INTO mahasiswa (nim, nama, ipk) VALUES ('{:s}', '{:s}', {:f})".format(
        nim, nama, ipk)
    cursor.execute(query)
    cnx.commit()

    view_data()


def update_data():
    view_data()
    print("Select the data you want to update!")
    nim = input("NIM : ")

    print("Note: NIM cannot be changed.")
    print("Enter the value you want to update!")
    nama = input("Nama : ")
    ipk = input("IPK  : ")
    ipk = float(ipk)

    query = "UPDATE mahasiswa SET nama = '{:s}', ipk = {:f} WHERE mahasiswa.nim = '{:s}'".format(
        nama, ipk, nim)
    cursor.execute(query)
    cnx.commit()

    view_data()


def delete_data():
    view_data()
    print("Select the data you want to delete!")
    nim = input("NIM : ")

    verification = input("are you sure want to delete this data? (Y/N)")
    if verification == 'y' or verification == 'Y':
        query = "DELETE FROM mahasiswa WHERE mahasiswa.nim = '{:s}'".format(
            nim)
        cursor.execute(query)
        cnx.commit()
    else:
        exit()

    view_data()
