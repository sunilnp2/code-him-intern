import psycopg2

conn = psycopg2.connect(database="postgres",
    user = "postgres",
    password = "root",
    host = "127.0.0.1",
    port = "5432")

print("Database Connect Successfull ")

cur = conn.cursor()
# --------------------------------------create table-------------------------------
# cur.execute('''CREATE TABLE INFO
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       ADDRESS        CHAR(50));''')
# print ("Table created successfully")


#--------------------------------------------------- Insert Operation----------------------------------------
# cur.execute("insert into info(id,name,age,address) values(1,'Sunil',20 ,'koteshwor');")

# cur.execute("insert into info(id,name,age,address) values(2,'Anil',22 ,'gorkha');")

# conn.commit()
# print("Data insert successfully")

# ---------------------------------------select Operation----------------------------------------------------------
# cur.execute("SELECT id, name,age, address from info")
# rows = cur.fetchall()
# for row in rows:
#    print ("ID = ", row[0])
#    print ("NAME = ", row[1])
#    print ("age = ", row[2])
#    print ("address = ", row[3], "\n")
#     # print(row)
# print ("Operation done successfully")


# -----------------------------------update Operation--------------------------------

# cur.execute("UPDATE info set age = 25 where ID = 1")
# conn.commit()
# print ("Total number of rows updated :", cur.rowcount)

# # see data after uupdate

# cur.execute("SELECT id, name,age, address from info")
# rows = cur.fetchall()
# for row in rows:
#    print ("ID = ", row[0])
#    print ("NAME = ", row[1])
#    print ("age = ", row[2])
#    print ("address = ", row[3], "\n")

# print ("Operation done successfully")



# Delete Operaetion

cur.execute("DELETE from info where ID=2;")

conn.commit()
print ("Total number of rows deleted :", cur.rowcount)

cur.execute("SELECT id, name,age, address from info")
rows = cur.fetchall()
for row in rows:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("age = ", row[2])
   print ("address = ", row[3], "\n")

print ("Operation done successfully")


conn.close()

