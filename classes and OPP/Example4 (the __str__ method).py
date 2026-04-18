#Welcome to a new example and a new method. What do
#you think will happen if you created an object from
#a class and once you create it, you decided to dislpay
#it on the screen? you will see something like this:
#       <__main__.No object at 0x0000020814E0A570>
#Now, the quiestion is how to display another value?
#This is what we will learn using the (__str__) class method
class no__str___:
    def  __init__(self):
        self.name='orion'
        self.damage=663
        self.speed=8.33
        self.health=619

    def get_stats(self):
        return f'name: {self.name}\
            \n damage: {self.damage}\
            \n speed: {self.speed}\
            \n damage: {self.health}'
    
class yes__str___:
    def  __init__(self):
        self.name='orion'
        self.damage=663
        self.speed=8.33
        self.health=619

    def __str__(self):
        return f'name: {self.name}\
            \n damage: {self.damage}\
            \n speed: {self.speed}\
            \n damage: {self.health}'
    
#Till now, note that the only difference between those two 
# classes are the name of the classes (functional names) and 
#the name of the second functions(__str__ VS get_stats). Now,
# see this:
var1=no__str___()
print(var1) # <__main__.no__str___ object at 0x0000012C8E80A8A0>
print(var1.get_stats()) #name: orion ...

print(f'\n=============================\n')

var2=yes__str___()
print(var2) #name: orion ...
print(var2.__str__()) ##name: orion ...

#As you can notice, without the __str__ method, the value of
#the object itself returns its plase in the memory, and you can
#print its stetus only when you make another function. But when 
#you use the __str__ method, there is a specific value for the 
#object itself and there is no need to make another function to 
#display the status of the object. Moreover, look at those statements:

print(str(var2)) ##name: orion ...
print(str(yes__str___())) ##name: orion ...