import psycopg2

class Employee():
    def __init__(self):
            self.conn = psycopg2.connect(database="sunildb",
            user = "postgres",
            password = "root",
            host = "localhost",
            port = "5432")

            print("Connected to Database")
            self.cur = self.conn.cursor()

     #    creating table 
    def create_table(self,table_name, schema):
          query_create = "create table if not exists {0}({1})".format(table_name, schema)
          self.cur.execute(query_create)
          self.conn.commit()

          print("Table Created")

     # insert into table
    def insert_table(self, table_name, schema, value):
          sp = schema.split(',')
          sch = ''
          for i in sp:
            b = i.split(' ')
            sch = sch+b[0] +','
          schema = sch[:len(sch)-1]
          query_insert = "insert into {0}({1}) values({2})".format(table_name, schema, value)
          self.cur.execute(query_insert)
          self.conn.commit()
          
          print("Insert into database")

     # show data 
    def show_data(self,table_name):
         query_show = "select * from {0}".format(table_name)
         self.cur.execute(query_show)
         rows = self.cur.fetchall()
         for row in rows:
              print ("ID = ", row[0])
              print ("NAME = ", row[1], "\n")
              
     # update data 
    def update_table(self,table_name,update_row, update_value, id):
         query_update = "update {0} set {1}='{2}' where id = {3}".format(table_name, update_row, update_value, id)
         self.cur.execute(query_update)
         self.conn.commit()
         print("Value updated")
 
     # delete data 
    def delete_data(self, table_name, id):
         query_delete = "delete from {0} where id = {1}".format(table_name, id)
         self.cur.execute(query_delete)
         self.conn.commit()
         print("Data Delete Successfully")

class Test(Employee):
     def __init__(self):
          super().__init__()
          # print("This is Testing Code Child Inheritance")



# commands
table_name = 'employee'
schema = 'id INT PRIMARY KEY not null,name varchar(20)'
value = "2, 'anil'"

update_row = 'name'
update_value = 'anil'
id = 1

obj = Test()
# obj.create_table(table_name, schema)
# obj.insert_table(table_name, schema, value)
# obj.update_table(table_name, update_row, update_value, id)
# obj.show_data(table_name)
# obj.delete_data(table_name, id)
        
    