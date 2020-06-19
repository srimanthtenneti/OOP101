"""
Created on Fri Jun 19 15:38:51 2020

@author: Srimanth Tenneti
"""

""" This is OOP 101 """
""" This is only the basics.
Note:
----

__init__ is also a magic method. I would describe about it in detail in my next article for now just 
remember that it is necessary for the class to function. 

Also note that the self can be replaced with anything. It is a reference element. You can add your name
too. But for the reset of the program you have to follow the same.

a : integer
b : integer

"""
class calculator(): 
    def __init__(self):  # Class constructor
        
        self.a = 0
        self.b = 0     # Attributes or properties of class objects
        
    def add(self , a , b):
        return a + b
    def subtract(self , a , b):
        return a - b
    def multiply(self , a , b):
        return a * b
    def divide(self , a , b):
        return a / b
    def sqrt(self , a):
        return a ** 0.5
    
calc = calculator()

a = float(input("Enter a number : "))
b = float(input("Enter a number :"))

print("\n")

print("Addition of {} & {} is {}\n".format(a,b,calc.add(a,b)))
print("Subtraction of {} & {} is {}\n".format(a,b,calc.subtract(a,b)))
print("Multiplication of {} & {} is {}\n".format(a,b,calc.multiply(a,b)))
print("Division of {} & {} is {}\n".format(a,b,calc.divide(a,b)))
print("Square root of {} is {}\n".format(a,calc.sqrt(a)))
