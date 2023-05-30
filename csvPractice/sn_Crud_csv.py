
class CrudCsv:
    def create_csv(self):

        keys=''
        for i in self.__dict__.keys():
            keys+=i+"," 
        keys = keys[:-1]               
            # list_value = keys.split(',')
            # list_value.pop()
            # print(type(list_value))
        try:     
            with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
                data=file.readlines()
                
        except FileNotFoundError:
            with open(f"{self.__class__.__name__.lower()}.csv","w", newline='') as file:
                # file.writelines(keys)
                data = []
        id=str(self.id)
        my_data=[i for i in data if i!="\n"]
        for i in my_data:
            if id in i:      
                print("Data with this id already exists")
                return

        values=list(self.__dict__.values()) 

        # reading first row heading  
        with open(f"{self.__class__.__name__.lower()}.csv", 'r', newline='') as file:
            # reader = csv.reader(file)
            # first_row = next(reader, None) 
            # first_row = file.readline().rstrip('\n')
            first_row = file.readline()
            print(first_row)# Get the first row or None if empty fil

        if first_row:
            print(first_row)
            print(type(first_row))

        else:
            with open(f"{self.__class__.__name__.lower()}.csv","w", newline='') as file:
            #     # writer = csv.writer(file)   
            #     print(keys)
                # writer.writerow(list_value)
                file.writelines(keys)

        if first_row == keys:
            print("Header exists")

            with open(f"{self.__class__.__name__.lower()}.csv", 'a', newline='') as csv_file:
                # writer = csv.writer(csv_file)
                # writer.writerow(values)
                print(type(values))
                v_str = ''
                for v in values:
                    v_str = v_str + str(v) +','

                print(v_str)
                v_str = '\n' + v_str 
                csv_file.write(v_str)

                print("Data Added")
                # csv_file.write('\n')
        
    def update_csv(self,*args):
        with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
            list_data=file.readlines()
            print(list_data)
        # print(args)
        id = str(args[0])
        print(id)
        sys_id = str(self.id)
        if sys_id == id:
            print("This is true")
            for d in range(len(list_data)):
                if id in list_data[d]:
                    print(list_data[d])
                    target = d
                    print(target)
                    print("There is")
                    break
            print(args)
            d_str = ''
            for i in args:
                d_str = d_str+str(i)+','
                # d_str = d_str[:-2]

            if target:
                list_data[target]= d_str[:-1]
            else:
                print("Enter correct id")

            with open(f"{self.__class__.__name__.lower()}.csv", "w+",) as update_file:
                update_file.writelines(list_data)

        else:
            print("id not found")

    def delete_data(self):
        with open (f"{self.__class__.__name__.lower()}.csv", 'r') as file_list:
            list_data = file_list.readlines()

        with open(f"{self.__class__.__name__.lower()}.csv", 'r') as csv_file:
            # reader = csv.reader(csv_file)
            reader = csv_file.readlines()
            data_list = list(reader)
            # print(len(data_list))
            for i in range(len(data_list)):
                if i == 0:
                    continue
                print(data_list[i])

        user_id = input("Enter id to delete :- ")
        print("You entered id " + user_id)
        target = None
        sys_id = str(self.id)
        print("This is true")
        for d in range(len(list_data)):
            if user_id in list_data[d]:
                    print(list_data[d])
                    target = d
                    print(target)
            if target is not None:
                list_data[target] = ''
            else:
                print("please enter correct id")
                break

            with open(f"{self.__class__.__name__.lower()}.csv", 'w+') as file:
                file.writelines(list_data)
                print(f"Data Deleted with id {user_id}")
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

class Student(CrudCsv):
    def __init__(self,id,name,faculty):
        self.id = id
        self.name = name
        self.faculty = faculty

# for employee
obj = Employee(2,"Ram Bahadur", 2000)
obj.create_csv()
# obj.update_csv(2,"Hari Bahadur",50000)









