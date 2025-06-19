print("Single Inheritence....")
class one:
    def __init__(self):
        print("This is Parent root class")
class two:
    def __init__(self):
        print("This is Second root class")
class three:
    def __init__(self):
        print("This is Third root class")                
class single_inheritence(one):
    def __init__(self):
        super().__init__()
        print("This is Child node class")

#in multiple inheritence contain one class contain two classes as inheritence         
class multiple_inheritence(two,one):
    def __init__(self):
        super().__init__()
        print("This is Multiple...")  
# In multilevel inheritence there are first class is inherit with second class 
# and second class is inherit with third class.          
class multilevel_inheritence0(one):
    def __init__(self):
        super().__init__()
class multilevel_inheritence1(two):
    def __init__(self):
        super().__init__()     
class multilevel_inheritence2(three):
    def __init__(self):
        super().__init__()         
#hierarichical inheritence in which each parent class has multiple child class               
class one:
    def __init__(self):
        print("This is Parent root class")
class two(one):
    def __init__(self):
        super().__init__()
        print("This is Second root class")
class three(one):
    def __init__(self):
        super().__init__()
        print("This is Third root class") 
        

obj1=single_inheritence()
print("*"*50)
print("Multiple Inheritence")
obj2=multiple_inheritence()
print("*"*50)
print("Multilevel Inheritence...")
obj3=multilevel_inheritence2()
print("*"*50)


