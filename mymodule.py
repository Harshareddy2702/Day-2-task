# Creating mymodule and saving it in bin
def greeting(name):
    print("Good Morning, " + name)
# Importing the mymodule
import mymodule
mymodule.greeting("Nikhil \n")

# Variables in Modules
person ={
    "Name" : "Harsha",
    "Age" : 21,
    "Country" : "India"
    }
import mymodule
a = mymodule.person["Age"]
print(a)



#Re-naming a Module by using as keyword


import mymodule as mm

a = mm.person["Name"]
b = mm.person["Age"]
c = mm.person["Country"]
print(a,b,c)


# Importing the platform module
import platform
x = platform.system()
print(x)


#using the dir() function
import platform

x=dir(platform)
print(x)


#Importing only greetingg form the module
from mymodule import person
print(person["Age"])

## Exercise :
## Create a python module with list and import the module in another .py file and change the value in list
num1=[5,15,25,35]
import mymodule
z = mymodule.num1[1]
print(z)

##Import a module that picks random number and write a program to fetch a random number from 1 to  100 on every run

import random
print(random.randint(1,100))

##Import sys package and find the python path
import sys
print(sys.path)








import pip install pandas
