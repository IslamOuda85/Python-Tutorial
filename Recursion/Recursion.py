'''
->  The recursion is an expression of the functions which call
    their selves.
->  The function that call itself is called "recursive function"
->  If a function kept calling itself without controlling, then the
    output will keep repeating forever (and this is wrong)!
->  Recursion is used to facilitate solving probles, however it can 
    be replaced by a loop.
->  when a function is called, then this is called "nase case", but 
    when the function calles itself, then this is called "recursive case".
->  when we decide to solve a problem using recusion, the first step 
    is to identify the base case (such as if the function is called 
    for only one time), and write the code basing on the base case only.
    That helps us to know how to solve the problem in the base case,
    and make it smaller and easier
->  After identifying the base case, we identify the recursive case
    by assuming the the repeated action
->  Here an example:
'''
#We will write a program that calculates the factorial of a number
#In factorial (n!), n must be a nonnegative number (n>=0), so there 
#are two cases for it: 
#1. n=0 then n!=1
#2. n>0 then n!=1*2*3*4*...*n
#Let's replace n! with the function "factorial(n)", then 
#1. n=0 then factorial(n)=1
#2. n>0 then factorial(n)=1*2*3*4*...*n
#if the value of n equals to 0, then return 1, and factorial(n) = 1
#if the value of n is greater than 0, then product n with n-1
#in mathmatics, n! = n * (n-1)! = n * (n-1) * (n-2)! = ...
#then, factoraial(n) = n * factoraial(n-1)  
#the final code:
import time


def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    #   return 3 * 2 * 1 * 1<==from the first condition 
print(factorial(3))

#=============================================================
#second example:
#write a program that gets the sum of a subset of a given list
listy = [4,3,2,5,1,7,9,8]

def ranger(listo,startindex,endindex=len(listy)):
    if startindex>=endindex:
        return 0
    else:
        return listo[startindex] + ranger(listo,startindex+1,endindex)
print(ranger(listy,3))
#=============================================================
#third example:
#write a program that displays the fibonacci series
#a fibonacci series:   0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,...
#the order of numbers: 0,1,2,3,4,5,6,7 ,8 ,9, 10,11,12 ,13 ,14 ,15 ,16
#a number is the sum of its previous 2 numbers

def fabonacci(n):
    if   n==0 :
        return 0
    elif n==1:
        return 1
    else:
        return (fabonacci(n-1)+fabonacci(n-2))
print(fabonacci(15))

"""
n0=0
n1=1
n2=1
n3=n1+n2
n4=n3+n2
...
nN=n(N-1)+n(N-2)
fabonacci(N)=fabonacci(N-1)+fabonacci(N-2)
"""
#=============================================================
#fourth example:
#write a program that gets the greatest common divisor (GCD)
#Don't say you dont know it!
def gcd(x,y):
    if x%y==0:
        return y
    else:
        print(y)
        return gcd(x,x%y)
print(gcd(96,72))

#=============================================================
#       --{recursion vs loops}--
#In short, recursion is not perfect for the simple problems, as
#it holds many operations on the system, so loops are better. 
#but if the problem is comlex (like the gcd), then recursion is
#the best. If you faced a problem, try to solve it using loops,
#and if it didn't work with you, you can use recursion to solve 
#it
 
#       --{END OF CHAPTER 12}-- 
#DON'T MISS TO SOLVE THE CHAPTER REVIEW
print('==========================')

   