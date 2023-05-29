import csv
import pandas as pd

class CrudCsv():
    def create_csv(self,name, data, header):
        file_name = f'{name}.csv'

        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)

        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            first_row = next(reader, None)  # Get the first row or None if empty file

        if first_row == header:
            print("Header exists")
            split_data = data.split(',')
            print(split_data)

            with open(file_name, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(split_data)

        if first_row != header:
            with open(file_name, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(header)
    

            print(type(data))
            split_data = data.split(',')
            print(split_data)
            with open(file_name, 'a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(split_data)

        
    def update_csv(self, name, data,id):
        file_name = f'{name}.csv'
        # reading the csv file
        df = pd.read_csv(file_name)
        # updating the column value/data
        df.loc[id, 'Name'] = data
        
        # writing into the file
        df.to_csv(file_name, index=False)
  

    def delete_data(self,name, id):

        file_name = f'{name}.csv'
        rows = []
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        if id < len(rows):
            del rows[id]
        else:
            print("Row Not found")

        # Write the modified contents back to the file
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)


    def show_data(self,name):
        file_name = f'{name}.csv'
        with open(file_name, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for r in reader:
                print(r)
            # print(reader)


class Person(CrudCsv):
    def create_csv(self, name, data, header):
        return super().create_csv(name, data, header)


class Student(CrudCsv):
    def create_csv(self, name, data, header):
        return super().create_csv(name, data, header)

# for parent        
header = ['Id','Name','Age']
file_name = 'person'
data = "2,'Anil',20"
updated_data = "Ram Saran"
id = 1


# for Persond
person = Person()
# person.create_csv(file_name,data,header)
# person.update_csv(file_name, updated_data, id)
# person.delete_data(file_name,id)
# person.show_data(file_name)

# for Student
stud = Student()
file_name = 'student'
stud.create_csv(file_name, data, header)
# stud.update_csv(file_name, updated_data,id)
# stud.delete_data(file_name,id)
# stud.show_data(file_name)