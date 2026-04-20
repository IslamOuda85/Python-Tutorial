#              --{CHAPTER 11: Inheretance }--
#     --{Part 1 of 2 : Introduction in Inheretance}--
#       --{GENERALIZATION AND SPECIALIZATION}--

#In the real world, there are many examples of expressions of general
#things, like "Fishes", and something classified under it, like "Salmon".
#the "is a" relationship is a casual tool to separate between the general 
#thing and the special one, like: football is a sport, MGG is a game,
#python is aprogramming language, and so on...
#NOTE that te general formula of the the "is a" relationship is 
#{special} is a {general}
#Also NOTE that the special thing has all the properties of the general 
#thing plus mora additional things that makes it special.
#In programming. inhertance stands for the "is a" relationship. By deploying
#it, you can create classes with more capabilities than the original ones.
#And as there was a general and a special in the real life, there is a 
#Superclass stands for the general and a Subclass stands for the special

#Example: Imagine that you have a tech store and you sell laptops, mobiles and
#PlayStations. You shaow the following data for the customers:
#1. the price of the device.
#2. the storage of the device.
#3. the year of manufactoring the device.
#In addition to those data, the laptops has the data of the following:
#1. RAM speed 
#2. CPU processing speed
#The mobiles has those additional data:
#1. the camera pixels
#2. Pro/Max/Pro Max/ Lite/ Ultra/ None of them
#The PlayStation has the additional data:
#1. The list of the games that come with each one
#Task: Translate the previous into classes

#Solution: without inheretance, you will make 3 classes with the 5 attributes for 
#laptops, 5 attributes for the mobiles, 4 attributes for the PlayStation, but if 
#you decide to add more common data, like the power of each type, How will you do?
#With inheretance, you can create 4 classes, and the fourth one (let's name it 
#"device") is the superclass that holds the common data attributes, and the 3
#subclasses holds the special data attributes. But also, what is the formula of the inhertance?
#The general formula of inheriting a class is:
#   class subclass(superclass): 
#Let's start first with the device class (we will not add the setters amd getters now)
class Device:
    def __init__(self,price,storage,manu_year):
        self.__price=price        
        self.__storage=storage
        self.__manu_year=manu_year       

    def check(self):
        print('Done!')
#Now, before to define the Laptops class, you know that it requires 5 data attributes and
#3 of them are common (inheretated), so, its __init__ method requires 6 parameters(with "self")
class Laptop(Device):
    def __init__  (self, price, storage, manu_year,RAM,CPU):#Once you type "init" and let the autofill 
    #                     ||||  |||||||  |||||||||          #continues, this code appear, NOTE that it 
    #                     VVVV  VVVVVVV  VVVVVVVVV          #it automatically asked you for 3 args (the common ones)
        super().__init__(price, storage, manu_year)         #and then passed them to the __init__ method of the
                                                            #superclass (Device).By that, we get the common arguments
                                                            #of the subclass, the other 2 remained, and as general, we do:
        self.__RAM=RAM                          
        self.__CPU=CPU
#NOTE the super().__init__ method, it executed the init method of the superclass, whichever it was, ALSO NOTE that it did NOT
#asked for the self parameter, because the super() class kept on the same object 
#In the mobile class, we will use a different way to inherit from the device class:
class Mobile(Device):
    def __init__(self, price, storage, manu_year,cam_pix,type):
        Device.__init__(self, price, storage, manu_year) 
        self.__cam_pix=cam_pix
        self.__type=type
#NOTE that we passed the 3 common args by calling the Device method (without mentioning that its a superclass), so the self was
#required. and finally, the playStation class:
class PlayStation(Device):
    def __init__(self, price, storage, manu_year,games):
        super().__init__(self, price, storage, manu_year) #NOTE that we added the self again and nothing is wrong
        self.__games=games

#Now, it's time for creating objects:
var1=Mobile(2000,'128 GB','2023','108 MP','PRO MAX')
var2=Device(3000,'512 GB','2022')
var2.check()
var1.check()

#===========================================================================================================================

#       --{Part 2 of 2 : Polymorphism and the "isinstance" function }--
#Welcome to the second half of this chapter, our load will be lite.
#In polymorphism, you can name methods with the same names for both the superclasses and the
#subclasses, but before to continue, do you sense something wrong? IF I CALLED THE FUNCTION OF
#THE SUBCLASS (WHICH INHERETS FROM A SUPERCLASS), AND BOTH OF THEM HAS SAME NAME, THEN WILL THE 
#CALLED FUNCTION BE THE ONE OF THE SUPERCLASS OR THE SUBCLASS? This is what we mean by polymorphism
class Animal:
    def __init__(self,name):
        self.__name=name

    def show_name(self):
        print(f'my name is {self.__name}')        

    def show_sound(self):
        print('psssssst')

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self,'cat') 

    def show_sound(self):       
        print('meow')


Animal_Var=Animal('dog')
Animal_Var.show_name()
Animal_Var.show_sound()

Cat_Var=Cat()
Cat_Var.show_name()
Cat_Var.show_sound()

#NOTE that there is a couple of functions with the same name and even almost the same code (the 
# difference is just in the text printed), however, the results were different. Simply, this difference
#referes to the difference of the objects theirself and the class they use. IN short, polymorphism informs 
#the objects that when there are two methods with the same name (one from the subclass and the other is 
#from the superclass), then execute the one of your class first. If you were an object of a subclass, then,
#DON'T TOUCH the method of the superclass as your class own a one! Got it?


#       --{the isinstance function}--
#Let's add on our code in order to learn and to short the code:
def show_animal_info (arg_must_be_an_OBJECT):
    arg_must_be_an_OBJECT.show_name()
    arg_must_be_an_OBJECT.show_sound()
#Now, this function eases the process of displaying the data better than the previous code above.
#This method accepts objects from Animal and Cat classes (as they are the only classes available).
#BUT..., what if we passed a string instead? Then, an AttributeError will rise. 
#In python, there is a method called "is instance" with the general formula:
#       isinstance(object,class) ->bool
#this method checks if the passed object is an istance of the passed object. For example:
print(isinstance(Cat_Var,Cat))          #==>True
print(isinstance(Animal_Var,Animal))    #==>True
print(isinstance(Cat_Var,Animal))       #==>True !!!
print(isinstance(Animal_Var,Cat))       #==>False
print(isinstance('se7leiah',Animal))    #==>OF COURSE False!
#Surly you noticed that an object of a subclass is an instance of the superclass
#while an object of a superclass is NOT an instanceof the subclass, Why? 
#Answer: The "is a" relationship 
#HINT: You can a "try: ... except AttributeError: ..." statement, but it will require more code 
#and effort, so, it's better to keep on the isinestance method

#           --{End of chapter 11}--