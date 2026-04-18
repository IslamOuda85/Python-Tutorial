#       --{SOME DEFINITIONS}--
#Encapsulation: the combining of data and code into a single object
#Data hiding:  refers to an object’s ability to hide its data attributes from code that is outside the object
#Class: code that specifies the data attributes and methods of a particular type of object
#=================================================
#       --{CLASS VS OBJECT}--
#the most simple difference is that a class can create objects,
#and objects are created from a class
#TO EASE: consider the class as a pan and the object as some eggs. Then,
#the class cannot become Omlet, but it is used for. And the object can be
#modefied and processed to be Omlet only when using the pan (class). Got it?
#=================================================
#       --{CODING TECHNIQUIES}--
#look at the below statement:
print(abs(-4))
#Of course, the abs(arg) is a method (like any methods), and you passed an
# argument to it, now compare between those two written methodes:
def calculate1():
    var1=int(input('enter the first number'))
    var2=int(input('enter the second number'))
    return var1 + var2

calculate1()

def calculate2(var1,var2):
    return var1 + var2

calculate2(2,5)

#The second function is more near to the "print(abs(-4))" method, because it
#accepts at least one argument insted of asking for variables once the function
#is executed. IN SHORT, when you define a function, it's better to make it accept
#arguments and then make the operations instead of definig it without arguments and
#then ask for many inputs (deploy parameters instead of the input statements). got it?

