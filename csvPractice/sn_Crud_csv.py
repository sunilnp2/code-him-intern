
class CrudCsv:
    def create_csv(self):

        keys=''
        for i in self.__dict__.keys():
            keys+=i+"," 
        keys = keys[:-1]
        print(keys)             
        print(type(keys))
        try:     
            with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
                data=file.readlines()
                # first_row = file.readline()
                
        except FileNotFoundError:
            with open(f"{self.__class__.__name__.lower()}.csv","w+", newline='') as file:
                file.writelines(keys)
            data = []
        id=str(self.id)
        my_data=[i for i in data if i!="\n"]
        for i in my_data:
            if id in i:      
                print("Data with this id already exists")
                return

        values=list(self.__dict__.values()) 

        # if first_row:
        #     print(first_row)
        #     print(type(first_row))

        # else:
        #     with open(f"{self.__class__.__name__.lower()}.csv","w", newline='') as file:
        #     #     # writer = csv.writer(file)   
        #         # writer.writerow(list_value)
        #         file.writelines(keys)

        # if first_row == keys:
        #     print("Header exists")
        v_str=""
        print(values)
        for i in values:
            v_str += str(i) + ","
        v_str = "\n" + v_str
        v_str=v_str[:-1]
        print(v_str)

        with open(f"{self.__class__.__name__.lower()}.csv", 'a') as csv_file:
            # print(type(values))
            csv_file.writelines(v_str)
            print("Data Added")
            csv_file.write('\n')
        
    def update_csv(self,*args):
        with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
            list_data=file.readlines()
            print(list_data)
        # print(args)
        id = str(args[0])
        sys_id = str(self.id)
        if sys_id == id:
            print("This is true")
            for d in range(len(list_data)):
                if id in list_data[d]:
                    print(list_data[d])
                    target = d
                    print(target)
                    break
            print(args)
            d_str = ""
            for i in args:
                d_str =d_str+str(i)+','
                # d_str = d_str[:-2]
            d_str = d_str[:-1]
            d_str = f"\n{d_str}"

            if target:
                # list_data[target]= d_str
                list_data[target]=','.join(map(str, args))
            else:
                print("Enter correct id")

            with open(f"{self.__class__.__name__.lower()}.csv", "w+",) as update_file:
                update_file.writelines(list_data)
                # update_file.write("\n")

        else:
            print("id not found")


    def delete_data(self):

        # with open(f"{self.__class__.__name__.lower()}.csv", 'r') as csv_file:
        #     # reader = csv.reader(csv_file)
        #     list_data = csv_file.readlines()
        #     print(type(list_data))
        #     data_list = list(list_data)
        #     for i in range(len(data_list)):
        #         if i == 0:
        #             continue
        #         print(data_list[i])

        # user_id = input("Enter id to delete :- ")
        # print("You entered id " + user_id)

        # for d in range(len(list_data)):
        #     if user_id in list_data[d]:
        #             print(list_data[d])
        #             target = d
        #             break
        #     target = d
        #     print(target)
        #     if target:
        #         list_data[target] = ""
        #     else:
        #         print("please enter correct id")
        #         break

        #     with open(f"{self.__class__.__name__.lower()}.csv", 'w') as file:
        #         file.writelines(list_data)
        #         print(f"Data Deleted with id {user_id}")
                # writer(list_data)
        # rows = []
        # with open(f"{self.__class__.__name__.lower()}.csv", 'r') as file:
        #     reader = csv.reader(file)
        #     rows = list(reader)
        # if id < len(rows):
        #     del rows[id]
        # else:traget
        #     print("Row Not found")

        # # Write the modified contents back to the file
        # with open(f"{self.__class__.__name__.lower()}.csv", 'w', newline='') as file:
        #     writer = csv.writer(file)
        #     writer.writerows(rows)
        with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
            data=file.readlines()
        data_list = list(data)
        for i in range(len(data_list)):
            if i == 0:
                continue
            print(data_list[i])
        id= input("Enter Id :- ")
        num=None
        for i in range(len(data)):
            if id in data[i]:
                num=i
                break
        if num!=None:
            data[num]=""
            
        else:
            print("Enter correct Id")
        
        
        with open(f"{self.__class__.__name__.lower()}.csv","w") as file:
            file.writelines(data)
            # print("Sucessfully Deleted !!!!")


    def show_data(self):
        with open(f"{self.__class__.__name__.lower()}.csv", 'r') as csv_file:
            # reader = csv.reader(csv_file)
            # data_list = list(reader)
            reader = csv_file.readlines()
            data_list = list(reader)
            # print(len(data_list))
            for i in range(len(data_list)):
                if i == 0:
                    continue
                print(data_list[i])
            # print(reader)

class Employee(CrudCsv):
    def __init__(self,id,name,salary):  
        self.id=id
        self.title=name
        self.salary=salary

# for employee
obj = Employee(1,"Ram Bahadur", 2000)
# obj.create_csv()
# obj.update_csv(1,"
# Hari Bahadur",500000000000)
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
stu.delete_data()











