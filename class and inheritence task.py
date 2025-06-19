#Vehicle is parent and Car is child class that create an inheritence.
class Vehicle:
    def start(self):
        print("Car is start...")

    def stop(self):
        print("Car is stop...")

class Car(Vehicle):
    def drive(self):
        print("I drive the car...")

obj=Car()
obj.start()
obj.drive()
obj.stop()      

#Attributes access in another class
class Person:
    def __init__(self):
        self.name=None
        self.age=None
class Student(Person):
    def __init__(self):
        self.grade=None
        self.school=None
    def input(self):
        self.name=input("Enter your name...")
        self.age=int(input("Enter your age..."))
        self.grade=input("Enter your grade...")
        self.school=input("Enter your school name...")
    def output(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Grade: ",self.grade)
        print("School Name: ",self.school)    
obj1=Student()
obj1.input()
obj1.output()

#Override function for inheritence
class Shape:
    def area(self,val):
        print("Shap")
