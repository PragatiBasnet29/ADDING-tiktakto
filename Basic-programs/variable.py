#variable decleration

"""Variable are like containers that store values which are changeable. in python there is no need to declare varialbe explicitly 
like in other languages. we use = "assignment operator" to assing values to variables"""

#Example
_x=2
y=9
print(_x)
print(_x+y)

"""variables  are of two types LOCAL and GLOBAL"""\

#Local Variable

"""Local variable are declared inside a function and can only be accessed inside that function"""

def myfunc():   #function
    x=5
    print(x)       
myfunc()  #calling function


#Global Variable        
"""Global variable are declared outside a function and can be accessed anywhere in the program"""

x=7
def myfunc():
    print(x)
myfunc()

#Global Keyword

"""If you want to change the value of a global variable inside a function, you can use the global keyword"""   

x=5 #global variable
def myfunc():
    global x
    x=10
myfunc()
print(x)
