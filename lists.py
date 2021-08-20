distros = ["fedora", "arch", "mint", "ubuntu 18.04"]
              #0        1      2            3
print(distros)
print(distros[0] + " is my favourite") # takes the element number 0 from the list
print(distros[-1] + " was my first distro")  # negative means takes from the last btw
print(distros[1:]) # takes everything from position 1
print(distros[1:3]) # everything between 1 and 3 excluding 3
distros[1] = "bad"  #modifies the value number 1 from the list and replaces it with "bad"
print(distros[1])

random_numbers = [1, 5, 11, 55]

distros.extend(random_numbers)      #with this, both the lists are merged
print(distros)
distros.append("hi hello im added") #adds the thing to the list
print(distros)
distros.insert(1, "puppy linux")    #at position 1, the string is inserted
print(distros)
distros.remove("mint")              #remove element
print(distros)
#distros.clear()                     #cleans the list
#print(distros)
distros.pop()                       #removes last element from the list
print(distros)

print(distros.index("fedora"))      #sees if fedora is in the list, if it is then it sends the index position of fedora
print(distros.count("fedora"))        #sees how many times this thing is in the list
print(random_numbers.count(1))
distros.remove(1)
distros.remove(5)
distros.remove(11)
distros.remove(55)

distros.sort()
print(distros)                  #alphabetical order
random_numbers.sort()
print(random_numbers)

distros.reverse()               #reverses the list
print(distros)

random2 = random_numbers.copy()     #new list with the same elements
print(random2)
