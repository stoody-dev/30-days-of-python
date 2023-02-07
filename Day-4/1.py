#strings in python
#in python you enclose anything between single and double quotes is called as string
name ="akshay"
game ="valorant"
print ("i want to play ", game) #for multi line string we use triple single quotes

print (name[0])#indexing in string starts from 0 to size-1 in python
print (name[1])
print (name[2])
print (name[3])
print (name[4])
print (name[5])#on using print(name[6] we get an error because there is nothing at 6th index)

intro='''
hi 
i am stoody-dev
a weeb dev xd
'''
for character in intro: # to print every character in a multi line string we use for loop
    print (character) 


#string slicing
names ="Akshay,stoody"
print(names[0:6])
print(len(names))