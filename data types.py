name= "aryan"         #string
age = 16                #integer
idk = 1.17365637828     #float
boo = True              #boolean
print(name.lower())
print(name.upper())
print(name.islower())
print(name.isupper())
print(name.upper().isupper())
print(len(name))        #shows how many characters
print(name[0])          #takes the first character from the variable
print(name[2])
print(name.index("a"))  #this is like grep in linux, tells you the position of the specified parameter. It will only show the first place where the string was found, not each and every one.
print(name.replace("aryan", "linux"))   #useful to replace the given string with something else
print(10 % 3)           #modulus operator. gives remainder
print(str(16) + " is my age")   #you need to convert the integer 16 to a string to add it to a string. this also applies to any variable.

my_num= -5
print(abs(my_num))      #this is the absolute value, you can say this is the magnitude of -5
print(pow(5, 3))        #this is 5^3
print(max(age, my_num)) #gives the larger number from the 2 passed parameters
print(min(age, my_num)) #gives the smaller number from the 2 passed parameters
print(round(3.4))
print(round(3.8))       #this rounds off numbers into an integer basically

from math import *

print(floor(3.7))       #chops off the decimal and only leaves the beginning integer
print(ceil(3.1))        #rounds it off to the next integer, no matter what the value
print(sqrt(81))         #square root!