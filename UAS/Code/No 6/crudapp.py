from var_dump import var_dump
from db_connect import *
from db_crud import *


print("1. View Data")
print("2. Create Data")
print("3. Update Data")
print("4. Delete Data")

choose = input("\nPilih Menu: ")
choose = int(choose)

if (choose == 1):
    view_data()

elif (choose == 2):
    add_data()

elif (choose == 3):
    update_data()

elif (choose == 4):
    delete_data()

else:
    print("Input salah!")


cnx.close()
