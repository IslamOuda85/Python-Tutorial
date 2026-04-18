import random #to import the random module 

class Coin: #to identify a class of name "Coins"
     #^---(upper case): recommended to distinguish a class name from a variable name

    def __init__(self):     #this class method is used to initialize the data(of the sideup) and accend a 
        self.sideup='heads' #default value of "heads"
       #|  |      |       | 
       #|  |      |       |     
       #\__/======|=======|=>#to inform that the opperations done are for the current object(not for another outer one)
       #\_________/=======|=>#the default statement of initializing a properety for an object
       #\_________________/=>#accending a value of 'heads' for an object's proreoty (variable)
    #NOTE: the __init__ special method is automatically executed once an object is created

    def toss (self):        #you can understand the purpose of this method easily
        if random.randint(0,1)==0:
            self.sideup='heads'
        else:
            self.sideup='tails'

    def get_sideup(self):   #this is a "getter" method that has the purpose of
                            #returning asked values only (must be permissionized)
        return self.sideup
#=====================================================
#       --{THE (self) PARAMETER}--
#As described in main.py (lines 6-11), a class is used to make copies of objects,
#and to determine the exact copy of object we are using, we use the (self) parameter.

#========--{THE END OF DEFINING Coin CLASS }--========

var=Coin() #this is the official formula of creating an object from a class (an Omlet made)
#formula: variable = Class OR variable = module.Class (for imported classes)

print(var.get_sideup()) #return (heads)
print(var.toss())       #return (None), but change the value of sideup value
print(var.sideup)       #returns the current sideup value (heads/tails)
#As you can see, the object (of name var) can now get access to all the functions
#and variables inside the class (we'll learn soon how to limit those access)
#NOTE: note that the functions executed in lines 34, 35 didn't asked any parameters,
#however that the funcs. in lines 15, 21 asked for 1 argument (self) . That's because  
#Python automatically passes a reference to the calling object into the method’s first parameter. 
#As a result, the self parameter will automatically reference the object on which the method is to operate.
#Moreover, if you made the functions without deploying (self), many errors will occur (this is a challenge!)
#=====================================================
#       --{IMPORTANT NOTE}--
'''
def abc():
    varx=123
def ABC():
    VAR=varx <==NameError
    print(VAR)
    print(varx)
abc()
ABC()
'''
#NOTE that the above 2 functions didn't manage to access to
#each others variables, while in the class methots (thanks to 
# self paramater), all the functions can be connected well
#=====================================================
#Now, you are ready to go to Example2 (Hiding attributes)
#but before, and to conserve time, effort, space, code, note the below:
varx=Coin()
varx.sideup='tails'
varx.sideup='batata'
varx.sideup= 0.0
varx.sideup= print('I AM A HACKER, WHAT A ZEEEEEEERO SECURETY!!!')
varx.toss()
print(varx.get_sideup()) #look at the scandolus result :(



