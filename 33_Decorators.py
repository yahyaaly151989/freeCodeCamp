# ========================== Decorators ==========================


# def my_decorator(func):
#     def apply_decorator():
#         print("Hello")
#         func()
#         print("Bye")
#     return apply_decorator
    
# @my_decorator
# def me():
#     print("Yehya")
    
# me()

# print("==================================")

# @my_decorator
# def him():
#     print("Ahmad")
    
# him()
# print("==================================")

# @my_decorator
# def her():
#     print("Alaa")

# her()




def my_decorator(func):
    def apply_decorator(number1, number2):
        
        
        if type(number1) != int:
            print("The * operator is for repeating objects not for multi.")
        
        func(number1, number2)
    return apply_decorator

@my_decorator
def calc(num1, num2):
    print(num1 * num2)
    
calc("10", 5)