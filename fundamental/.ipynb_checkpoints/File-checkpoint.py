# name1 = str(input("Enter the name1"))
# name2 = str(input("Enter the name2"))
# name3 = str(input("Enter the name3"))

# names = [name1 , name2 , name3]

# with open("names.txt" , "w") as f:
#     f.writelines(name +"\n"  for name in names)

# with open("names.txt" ,"r") as f2:
#     data = f2.read()
#     print(data)
    
    
with open("log.txt" , "r") as file:
    file.write("program run successfullt")
    data = file.read()
    print(data)