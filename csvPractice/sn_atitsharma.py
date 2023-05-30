class Main:
    def __init__(self):
        pass
                     
    def save(self):
        values=list(self.__dict__.values())      
        try:     
            with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
                data=file.readlines()
                
        except FileNotFoundError:
            with open(f"{self.__class__.__name__.lower()}.csv","w") as file:
                keys=''
                for i in self.__dict__.keys():
                    keys+=i+","                 
                # print(keys)
                file.writelines(keys[:-1])              
            data=[]           
        id=str(self.id)
        my_data=[i for i in data if i!="\n"]
        print(my_data)
        for i in my_data:
            if id in i:      
                print("id must be unique")
                return
        
        string=""
        print(values,"******")
        for i in values:
            string+=str(i) 
            string+="," 
        string=string[:-1]
        
        with open(f"{self.__class__.__name__.lower()}.csv","a") as file:
            file.writelines(f"\n{string}")
            print("Sucessfully saved your data !!! ")
            
        # return data
            
        
        
    def delete(self):
        with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
            data=file.readlines()
        id=str(self.id)
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
            print("Sucessfully Deleted !!!!")

        

    
    def update(self,*newdata):
        with open(f"{self.__class__.__name__.lower()}.csv","r") as file:
            data=file.readlines()
        id=str(newdata[0])
        num=None
        if str(self.id) == id:
            for i in range(len(data)):
                if id in data[i]:
                    print(data[i])
                    num=i
                    break
            if num!=None:
                data[num]=','.join(map(str, newdata))
            else:
                print("Enter correct Id")
            with open(f"{self.__class__.__name__.lower()}.csv","w+") as file:
                file.writelines(data)
                print("Successfully Updated !!!! ")
        else:
            print("Please provide correct id")
            
    def get(self):
        print (self.__dict__)
        
    
        
        
    # THIS FUNCTION IS USED TO GET ALL OBJECTS 
    @classmethod
    def get_all(cls):
        
        objects = []
        try:
            with open(f"{cls.__name__.lower()}.csv", "r") as file:
                data = file.readlines()
        except FileNotFoundError:
           raise Exception("Make sure to save before ")
       
        newdata = [i for i in data if i != "\n"]
        
        for i in newdata:
            values = i.strip().split(",")
            obj = cls(*values[:])
            objects.append(obj)
              
              
        for obj in objects:
            obj_name=(type(obj).__name__,obj.id)
            print(obj_name)

 

class Book(Main):
    def __init__(self,id,title,author):  
        super().__init__() 
        self.id=id
        self.title=title
        self.author=author
        
class Person(Main):
    def __init__(self,id,name):
        super().__init__()
        self.id=id
        self.name=name
        


b=Book(2,"GoodBook","Ram1")
b2=Book(3,"GoodBook2","Ram22")
b3=Book(4,"BJGG","KKSH")
# b.save()
b.update(2,"badbook","sunil")










