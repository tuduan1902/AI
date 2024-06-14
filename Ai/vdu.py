import time
class MyClass:
    # Class variable
    class_variable = 10
    
    # Constructor method
    def __init__(self, name):
        self.name = name  # Instance variable
    
    # Instance method
    def greet(self):
        print("Hello, my name is", self.name)

# Creating an object of MyClass
obj = MyClass("John")

# Accessing instance variables and calling methods
obj.greet()               # Output: Hello, my name is John



class sinhvien:
    def __init__(self, name, Mssv, Diem):
        self.ten = name 
        self.mssv = Mssv
        self.diem = Diem



tuong = sinhvien("tuong", "19146425", 10)
print("ten: ", tuong.ten)
print("mssv: ", tuong.mssv)
print("diem: ", tuong.diem)
time.sleep(10)