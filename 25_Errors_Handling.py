# =============================== Errors Handling ===============================


# try:
#     f = open("my_file.txt", "r")
    
#     print(10/0)
    
# except FileNotFoundError as e:
#     print(e)
    
# except NameError as e:
#     print(e)

# except Exception as e:
#     print(e)

# else:
#     print(f.read())
#     f.close()

try:
    f = open("danger.txt", "r")
    if f.name == "danger.txt":
        raise Exception
    
except Exception as e:
    print("This file is corrupted.")
else:
    print(f.read())
    f.close()


