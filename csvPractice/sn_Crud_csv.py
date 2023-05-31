import sys
class CrudCsv:
    def create_csv(self):
        keys=''
        for i in self.__dict__.keys():
            keys+=i+"," 
        keys = keys[:-1]
        print(keys)

        values=list(self.__dict__.values()) 
        v_str=""
        for i in values:
            v_str += str(i) + ","
        v_str = "\n" + v_str
        v_str=v_str[:-1]            
        try:     
            with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
                first_row = file.readline()
                data=file.readlines()
        except FileNotFoundError:
            with open(f"{self.__class__.__name__.lower()}.csv","a", newline='') as file:
                file.writelines(keys)
                file.writelines(v_str)
                sys.exit()
            data = []

        id= str(self.id)
        my_data=[i for i in data if i!="\n"]
        print(my_data)
        for i in my_data:
            if id in i:      
                print(f"Data with this id {id} already exists")
                return
            
        if first_row == '':       
            with open(f"{self.__class__.__name__.lower()}.csv","a", newline='') as file: 
                        file.write(keys)
                        file.writelines(v_str)
        else:
            print("First row is not none")
            first_row = first_row[:-1]

            if keys == first_row:
                print("Header exists")
                with open(f"{self.__class__.__name__.lower()}.csv","a", newline='') as file: 
                    file.writelines(v_str)
                    print("value Added")
            else:
                print("First row is not header")
                with open(f"{self.__class__.__name__.lower()}.csv", 'r+') as file:
                    row1 = file.readlines()
                    keys = keys + "\n"
                    row1[0] = keys + row1[0] # Modify the first line by appending the content
                    file.seek(0)  # Move the file pointer to the beginning of the file
                    file.writelines(row1)
                    file.writelines(v_str) 

    def update_csv(self):
        with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
            list_data=file.readlines()
            data_list = list(list_data)
            for i in range(len(data_list)):
                if i == 0:
                    continue
                if data_list[i].endswith("\n"):
                    data_list[i] = data_list[i][:-1]
                    print(data_list[i])
                else:
                    print(data_list[i])
        # mystr = ','.join(map(str, args))

        update_list = ""
        for i in self.__dict__.keys():
            i = input(f"Enter {i} TO update :- ")
            update_list += i + ","
        update_list = update_list[:-1]
        print(update_list)
        
        id = update_list[0]
        if id:
            for d in range(len(list_data)):
                if id in list_data[d]:
                    print("Yes")
                    print(list_data[d])
                    target = d
                    print(f"You select id {target}")
                    break
            if target:
                # list_data[target]= d_str
                list_data[target]= update_list + "\n"
            else:
                print("Id doesnot match")

            with open(f"{self.__class__.__name__.lower()}.csv", "w+",) as update_file:
                update_file.writelines(list_data)
                # update_file.writelines("\n")
                print("Updated")
        else:
            print("id not found")

    def delete_data(self):
        with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
            data=file.readlines()
        data_list = list(data)
        for i in range(len(data_list)):
            if i == 0:
                continue
            if data_list[i].endswith("\n"):
                data_list[i] = data_list[i][:-1]
                print(data_list[i])
            else:
                print(data_list[i])

        id= input("Enter Id :- ")
        num=None
        for i in range(len(data)):
            if id in data[i]:
                num=i
                break
        if num!=None:
            data[num]=""
            with open(f"{self.__class__.__name__.lower()}.csv","w") as file:
                file.writelines(data)
                print(f"Data with id {id} is deleted")
        else:
            print("Enter correct Id")


    def show_data(self):
        with open(f"{self.__class__.__name__.lower()}.csv", 'r') as csv_file:
            # reader = csv.reader(csv_file)
            # data_list = list(reader)
            reader = csv_file.readlines()
            data_list = list(reader)
            for i in range(len(data_list)):
                if i == 0:
                    continue
                if data_list[i].endswith("\n"):
                    data_list[i] = data_list[i][:-1]
                    print(data_list[i])
                else:
                    print(data_list[i])
            

class Employee(CrudCsv):
    def __init__(self,id,name,salary):  
        self.id=id
        self.title=name
        self.salary=salary

# for employee
obj = Employee(2,"Ram Bahadur", 5000)
obj.create_csv()

# obj.update_csv()
# obj.delete_data()
# obj.show_data()

class Student(CrudCsv):
    def __init__(self,id,name,faculty):
        self.id = id
        self.name = name
        self.faculty = faculty



stu = Student(1,"Samir","BCA")
# stu.create_csv()
# stu.update_csv(1,"Samir Neupane","BBS")
# stu.show_data()
# stu.delete_data()











