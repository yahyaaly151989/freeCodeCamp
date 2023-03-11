# ========================== Loop - While, For and Else ===========================
# 1- What is loop in Python?
# ---> Looping means repeating something over and over until a particular condition is satisfied.

# 2- Loop => While Loop:
# ---> Syntax:
# while true_condition:
#     code to run
# else:
#     code to run when finished

# x = 1
# while x <= 10:
#     # print(x <= 10)
#     print(x)
#     x += 1 # x = x + 1
# else:
#     # print(x <= 10)
#     print("Loop is done.")
    
names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

# print( names[0] )
# print( names[1] )
# print( names[2] )
# print( names[3] )
# print( names[4] )
# print( names[5] )
# print( names[6] )
# print( names[7] )
# print( names[8] )

# print( len(names) )
# x = 0

# while x < len(names):
#     print( names[x] )
#     x += 1 # x = x + 1
    
# 3- Loop => For Loop:
# ---> Syntax:
# for item in iterable_object:
#     code to run
# else:
#     code to run when finished


# for number in range(1, 11):
#     print(number)
# else:
#     print("Loop is done.")
# print("=" * 75)
    
# names = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

# for name in names:
#     print(name)
# else:
#     print("Loop is done.")
    
# print("=" * 75)


# 4- Break, Continue, Pass
# ---> break:

# for year in range(2000, 2024):
    
#     if year == 2020:
#         break
    
#     print(year)
    
    
# # ---> continue

# for year in range(2000, 2024):
    
#     if year == 2020:
        
#         continue
    
#     print(year)

    
# ---> pass

# if 10 == 10:
#     pass

# for year in range(2000, 2024):
#     pass

# def test():
#     pass
    
    

    
# products = ["Product1", "Product2", "Product3"]
# colors = ["Red", "Green", "Blue"]

# for product in products:
#     print( f"{product} => " )
    
#     for color in colors:
#         print( f"---> {color}" )
        
        
languages = {
    "Python": "70%",
    "JavaScript": "85%",
    "PHP": "65%",
    "C++": "80%"
}

# for language in languages:
#     print( f"{language} => {languages[language]}")

# for key, value in languages.items():
#     print( f"{key} => {value}")


name = "Yehya"

# ls = []

# for l in name:
#     ls.append(l)
    
# print(ls)


print( [l for l in name] )


    

