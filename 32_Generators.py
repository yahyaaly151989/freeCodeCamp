# ========================== Generators ==========================

# def square_numbers(number):
#     result = []
#     for i in number:
#         result.append(i * i)
#     return result
# my_numbers = square_numbers( [1, 2, 3, 4, 5] )

# print(my_numbers)

# my_numbers = [ i * i for i in [1, 2, 3, 4, 5] ]

# print(my_numbers)

# def square_numbers(number):

#     for i in number:
#         yield (i * i)

# my_numbers = square_numbers( [1, 2, 3, 4, 5] )

# print(my_numbers)

# # print(dir(my_numbers))

# print(next(my_numbers))
# print(next(my_numbers))
# print(next(my_numbers))
# print(next(my_numbers))
# print(next(my_numbers))


my_numbers = ( i * i for i in [1, 2, 3, 4, 5] )

print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))

print("======================================================")


for g in my_numbers:
    print(g)

