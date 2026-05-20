# class Student:#BLUE PRINT of the class
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")


# s1 = Student("Vishesh", 20)#object

# s1.display()

# class car:
#     def __init__(self,name,model):
#         self.name=name
#         self.model=model
    
#     def display(self):
#         print(f"NAME:{self.name}")
#         print(f"NAME:{self.model}")

# c1=car("BMW","X7")
# c1.display()

# class employee:
#     def __init__(self,name,age,dept):
#         self.name=name
#         self.age=age
#         self.dept=dept
    
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"age: {self.age}")
#         print(f"dept: {self.dept}")

# e1=employee("vishesh",21,"it")
# e1.display()

# class inherit(employee):#inherited function take the properties of the employee class 
#     def function(self):
#         print("inherited function")

# i1=inherit("hemika",25,"MBA")
# i1.display()
# i1.function()


# class encap(car):
#     def __init__(self, name, model, price):
#         super().__init__(name, model)

#         self.__onroadprice = price
#     def update(self):
#         percent=self.__onroadprice*0.18
#         self.__onroadprice+=percent
    
#     def show(self):
#         print(self.__onroadprice)

# e2=encap("AUDI","Q5",5000000)
# e2.update()
# e2.show()



from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


d = Dog()

d.sound()

class cat(Animal):
    def meow(self):
        print("meow")
    def sound(self):
        print("meow1")

c=cat()
c.sound()