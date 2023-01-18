import mysql.connector

cnx = mysql.connector.connect(
    user='root', password='', host='localhost', database='db_uas_pbo')

cursor = cnx.cursor()
