#Importing stuff to make it look cool 
import os
from termcolor import colored
import time
from time import sleep
import pyfiglet
def clear(seconds=0):
  time.sleep(seconds)
  os.system('clear')
#How I make "Welcome to the Calculator" appear on the screen 
def type(words):
  for char in words:
    sleep(.009)
    print(char, end='', flush=True)

type(pyfiglet.figlet_format(("Welcome to the Calculator")))
clear(1)

calculator = True
#Inputing your problem 
while calculator == True:
  def type(words):
    for char in words:
      sleep(0)
      print(char, end='', flush=True)

  type(pyfiglet.figlet_format(("Welcome to the Calculator")))   
  print(colored("Please enter your math problem", "green"))  
  #Solving your problem and telling you the answer
  problem = eval(input())
  print(problem)
  clear(1.5)