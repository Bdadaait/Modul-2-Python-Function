
# Task 1: Create functions for each arithmetic operation:

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y 

def multiply(x, y):
    return x * y

def divide(x, y):
     try:
            return x / y 
     except ZeroDivisionError:
          return "Error! Devission by zere."

def calculator():
     
     print("add")
     print("subtract")
     print("multiply")
     print("divide")

     while True:      # Task 2: Use inputs to ask the user what operation they want to perform:
          operation = input ("what operation do you want to perform (add, subtract, multiply, divide): ")

          if operation in [ 'add', 'subtract', 'multiply', 'divide']:
               x = float(input("enter the first number : "))
               y = float(input("enter the second number : "))
              
               if operation == 'add':
                    print(f"Result: {add(x, y)}")
               elif operation == 'subtract':
                    print (f"Result: {subtract(x, y)}")
               elif operation == 'multiply':
                    print(f"Result: {multiply(x, y)}")
               elif operation == ' divide':
                    print(f"Result: {divide(x, y)}")
       
          else :
               print ("invalid choice. Please select a valid operation.")  

calculator()                   



