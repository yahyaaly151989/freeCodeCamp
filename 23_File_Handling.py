# ========================= File Handling =========================

# my_file = open("yehya.txt", "r")

# print( type(my_file) )

# print(dir(my_file))

# contents = my_file.read()

# contents = my_file.readlines()

# contents = my_file.readline()

# print(contents)

# my_file.close()

# print(my_file.closed)

# contents = my_file.read() # I/O operation on closed file.


# with open("yehya.txt", "r") as my_file:
#     contents = my_file.read()
    
#     print(contents)
    
    
# print(my_file.closed)

# with open(r"C:\Users\Administrator\Desktop\noha.txt", "r") as my_file:
#     contents = my_file.read()
#     print(contents)

with open("alaa.txt", "a") as my_file:
    my_file.write("\ntest")
    
    
print(dir(my_file))