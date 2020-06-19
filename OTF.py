from OOP101 import calculator # Calling the calculator class from OOP101 file

c = calculator() # Class instance

print("Sum of 1 , 2 is {}".format((c.add(2 , 1))))

"""
Now this describes how we use a class defines in one program call it is another program .

Before running the code in this file make sure you delete 

calc = calculator() # Class instance 

a = float(input("Enter a number : "))
b = float(input("Enter a number :"))

print("\n")

print("Addition of {} & {} is {}\n".format(a,b,calc.add(a,b)))
print("Subtraction of {} & {} is {}\n".format(a,b,calc.subtract(a,b)))
print("Multiplication of {} & {} is {}\n".format(a,b,calc.multiply(a,b)))
print("Division of {} & {} is {}\n".format(a,b,calc.divide(a,b)))
print("Square root of {} is {}\n".format(a,calc.sqrt(a)))

in the previous file. This is part is added just to shoe the functionality.
"""
