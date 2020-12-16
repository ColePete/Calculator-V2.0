import os
from termcolor import colored
import time
def clear(seconds=0):
  time.sleep(seconds)
  os.system('clear')
print(colored("Welcome to the Calculator", "green")) 
clear(1) 

calculator_running1 = True 

while calculator_running1 == True:
  x = float(input (colored("Please input", "green") + colored(" FIRST ", "red") + colored("number", "green") + "\ninput here: "))      
  clear(.5)





  y = float(input (colored("Please input", "green") + colored(" SECOND ", "red") + colored("number", "green") + ("\ninput here: ")))


  operation = True
  while operation == True:
    clear(.5)
    
    operation_choice = input (colored("Please input", "green") + colored(" OPERATION ", "red") + "\n 1) + \n 2) - \n 3) * (multiply) \n 4) / (divide)" + ("\ninput here: ")) 


    if operation_choice == "1":
        operation1 = "add"
        operation = False
        clear(.5)
        print("Your answer is:", (x + y)) 
        clear(2)

    elif operation_choice == "2":
        operation1 = "subtract"
        operation = False
        clear(.5)
        print("Your answer is:", (x - y))
        clear(2)

    elif operation_choice == "3":
        operation1 = "multiply"
        operation = False
        clear(.5)
        print("Your answer is:", (x * y))
        clear(2)
    
    elif operation_choice == "4":
        operation1 = "divide"
        operation = False  
        clear(.5)
        print("Your answer is:", (x / y))
        clear(2)
       
    else:
        print("***" * 7)
        print("ERR: INVAILD INPUT") 
        print("***" * 7)
        operation = True