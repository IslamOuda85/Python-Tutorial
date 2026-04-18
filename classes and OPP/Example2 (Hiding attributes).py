#Before to begin, note the lines 46-54 and see how
#easy you can modify the vales and access all the 
#methods, that's because the access of all those 
#are public (readable and updatable). In this examlpe
#we will learn how to limit those access

#In order to adapt the access as private, we use 
#2 underscores (__) as a prefixfor the attribute
class Mine: 
    def __init__(self):
      self.__unreached_value=10  

    def __unreached_function(self):
        return 10

var=Mine()
#print(var.__unreached_value)    #Rise an ERROR
#print(var.__unreached_function) #Rise an ERROR
#As you can see, you can't access neither the values
#nor the functions ... but look at this :

print(var._Mine__unreached_function()) #10
print(var._Mine__unreached_value)      #10
#This is simply a bug in Python itself. Don't worry!

#BUT, look at this:
class B:
   __unreached_value=100
   def reaching_the_unreached_value(self):
      return self.__unreached_value
   
MyVar=B()
#print(MyVar.__unreached_value) #ERROR
print(MyVar.reaching_the_unreached_value()) #100

#that was a simple example on the benifits of the getter method




