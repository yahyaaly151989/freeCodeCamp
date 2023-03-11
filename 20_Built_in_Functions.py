# ========================== Built in Functions ===========================

# all()


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
if all(number > -5 for number in numbers):
    print("All numbers are greater than -5")
else:
    print("There is at least one number less than 5")
    
print("=" * 75)
    
# any()
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

if any(number > 10 for number in numbers):
    print("There is at least one number greater than 10")
else:
    print("All numbers are less than 10")
    
print("=" * 75)

# id()
a = 1
b = 2
print( id(a) )
print( id(b) )

print("=" * 75)

# bin()
print( bin(100) )
print("=" * 75)

# sum()
print( sum( [1, 2, 3, 4], 5 ) )
print("=" * 75)

# range()
print( list(range(10)) )
print( list(range(5, 15)) )
print( list(range(5, 15, 2)) )
print( list(range(20, 10, -1)) )
print("=" * 75)

# pow()
print( pow(2, 3) )
print( pow(2, 3, 3) )
print("=" * 75)

# round()
print( round(10) )
print( round(10.9) )
print( round(10.5) )
print( round(10.2) )
print( round(10.65) )
print( round(10.66, 1) )
print( round(10.66678, 3) )
print("=" * 75)

# max()
print( max( 10, 20, 30, -10, 93 ) )
print( max( "a", "b", "z", "yehya" ) )
print("=" * 75)

# min()
print( min( 10, 20, 30, -10, 93 ) )
print( min( "a", "b", "z", "yehya" ) )
print("=" * 75)

# abs()
print( abs(10) )
print( abs(-20) )
print("=" * 75)

# slice()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( nums[0:5] )
print( nums[ slice(0, 5) ] )
print("=" * 75)

# print()
print("Hi", end=" | ")
print("How are you?")
print(10, 20, sep="\n")
print("=" * 75)

# enumerate()

# langs = ["HTML", "CSS", "JS", "Python"]

# for lang in enumerate(langs, 20):
#     print(lang)
# print("=" * 75)

# for index, lang in enumerate(langs):
#     print(f"{index}- {lang}")
    
print("=" * 75)

# help()

# help(str)
print("=" * 75)

# reversed()

# my_name = "Yehya"

# print(list(reversed(my_name)))


# print("=======================================================")

# # A- What is map()?
# # ---> Map in Python is a function that works as an iterator to return a result 
# #      after applying a function to every item of an iterable (tuple, lists, etc.)

# # Syntax :

# # map(fun, iter)

# # Parameters :

# # fun : It is a function to which map passes each element of given iterable.
# # iter : It is a iterable which is to be mapped.

# # NOTE : You can pass one or more iterable to the map() function.

# # CODE 1:
# # Python program to demonstrate working
# # of map.
  
# # Return double of n
# def addition(n):
#     return n + n
  
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)

# result = map(addition, numbers)

# print(tuple(result))

# print("=" * 75)


# # CODE 2
# # We can also use lambda expressions with map to achieve above result.

# # Double all numbers using map and lambda

# numbers = [1, 2, 3, 4]

# result = map(lambda x: x + x, numbers)

# print(list(result))

# print("=" * 75)

# # CODE 3:

# # Add two lists using map and lambda

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
# numbers3 = [2, 4, 6]

# result = map(lambda x, y, z: (x + y) * z, numbers1, numbers2, numbers3)

# print(list(result))

# # [10, 28, 54]

# print("=" * 75)


# # CODE 4:
# # List of strings
# l = ['sat', 'bat', 'cat', 'mat']

# # map() can listify the list of strings individually

# test = list(map(list, l))

# print(test)

# print("=================================================")

# # filter()

# # def check_positive(number):
# #     if number > 0:
# #         return number
    
# # numbers = [1, 2, -3, 4, -89, 8, 5, -9]

# # result = filter(check_positive , numbers)

# # print(list(result))
# # # for n in result:
# # #     print(n)

# # def check_zero(number):
# #     return number == 0
    
# # numbers = [0, 0, 1, 2, 0, -3, 4, -89, 8, 5, -9, 0, 0, 3]

# # result = filter(check_zero , numbers)

# # print(list(result))


# # result = filter(lambda number: number == 0, numbers)

# # print(list(result))


# def check_even(number):
#     return number % 2 == 0


# numbers = [1, 2, 4, 6, 5, 9, 11, 33, 22, 24]

# result = list( filter( check_even, numbers ) )

# print(result)

# result = list( filter( lambda number: number % 2 == 0, numbers ) )

# print(result)

# print("============================================================")


# from functools import reduce
# # reduce()

# # def summAll(num1, num2):
# #     return num1 + num2

# # numbers = [1, 2, 4, 6, 5, 9, 11]


# # result = reduce(summAll, numbers)

# # print(result)

# # result = reduce(lambda num1, num2: num1 + num2, numbers)

# # print(result)

# # def convert_letter_to_name(l1, l2):
# #     return l1 + l2


# # letters = ["Y", "e", "h", "y", "a"]

# # my_name = reduce(convert_letter_to_name, letters)

# # print(my_name)


# numbers = [1, 4, 3, 7, 5, 11, 8, 12, 22]

# filter_even = list(filter(lambda number: number % 2 == 0, numbers))

# result = reduce( lambda number1, number2: number1 + number2, filter_even)

# print(result)







