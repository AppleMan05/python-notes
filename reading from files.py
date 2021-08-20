the_file = open ("/home/aryan/HDD/gui.py", "r")            #the r means read, no changes done. w mode means editing is possible. a mode means append, you can put info in the end. there is also r+ mode, which can read+write

print(the_file.readable())
print(the_file.writable())

#print(the_file.read())

print(the_file.readline())
print(the_file.readline())      #this reads the next line every time you use the readline function
#print(the_file.readlines())     #makes an array from all the lines
#print(the_file.readlines()[40])

for line in the_file.readlines():
    print(line)

the_file.close()  #closes the file