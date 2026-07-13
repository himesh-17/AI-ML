#strings in pyhton

word = "himesh"
print(len(word))

# concatenation
str1 = "himesh"
str2 = "badlani"
print("This is the conatenation -> "+ str1+str2)

# slicing of string 

word = "Himesh badlani a Student of MITS" 
print(word[0 : 15])

#formatting - directly embedding the variables into the strings 
name = input("Enter the name ")
age = int(input("Enter the age"))

print("Himesh my name is {} and im {} years old".format(name , age))

#---------------------------------------------------------------------------------------------------#
#List

person = [[10,20,30] , 35 , "Himesh"]