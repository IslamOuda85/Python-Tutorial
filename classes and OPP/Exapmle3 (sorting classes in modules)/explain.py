#When you write a program, it's easy and simple to write your
#classes and then write the else code in one module. But when 
#you write a big program, it's a priority to organize all the 
#classes in modules so you can import them wanted.
#Look at the file classes.py and see how we created a class named
#(Coin). If you took a look at main.py (line 1), you will note the following:
#1. We imported the name of the python file (not the class name)
#2. We created an object, but instead of using the formula : variable = class(), we 
#   now use the formula: variable = file.class()
#3. Now, we can benifit from the class like if it was written above, and we conserced 
#our time, code, and organized everything and become mre able to fix the problems.

#       --{END OF EXAMPLE 3}--



#       --{Setters and getters}--
#Of course you the purpose of both setters and getteres, the general formula of the getter is:
#   {consider that self.__var is a data attribute of a class}
'''
def get_var(self):
    return self.__var
'''
#The general formula of the setter is:
'''
def set_var(self,para):
    self.__var=para
''' 
#In designing classes, you can note that: 
#the number of getters = the number of setters = the number of the data attributes 


