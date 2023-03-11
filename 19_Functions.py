# ========================== Functions ===========================
# 1- What are Python Functions?
# ---> A function is a block of code which only runs when it is called.
# ---> You can pass data, known as parameters, into a function.
# ---> A function can return data as a result.


# 2- Creating a Function:
# ---> In Python a function is defined using the def (define) keyword:
def my_function():
    print("Hello from a function")
    

# 3- Calling a Function:
# ---> To call a function, use the function name followed by parenthesis:
def my_function():
    print("Hello from a function")

my_function()

print("=" * 75)

# def generate_years():
#     for year in range(2000, 2024):
#         print(year)
        
# generate_years()

# Parameters and Arguments

def generate_years(start, end):
    for year in range(start, end):
        print(year)
        
generate_years(2000, 2024)
print("=" * 75)
generate_years(2000, 2011)
print("=" * 75)
generate_years(1990, 2001)
print("=" * 75)

# generate_years(1990) # error => missing 1 required positional argument

# 4- Default Parameter Value:

def user_info(name="Unknown", country="Unknown"):
    
    print( f"Hello {name}, I am from {country}" )
    
user_info("Yehya", "Syria")

user_info("Ahmad")

user_info()
print("=" * 75)

# 5- Function Return

def sum_two(n1, n2):
    
    return n1 + n2

result = sum_two(10, 20) * 10

print(result)
print("=" * 75)

# 6- Arbitrary Arguments, *args

def user_skills(name, *langs):
    
    # print( type(langs) )
    
    print(f"Hello {name}, your skills are: =>")
    
    for lang in langs:
        print(f"---> {lang}")
    
# langs = ("Python", "JavaScript", "PHP", "HTML")

user_skills("Yehya", "Python", "JavaScript", "PHP", "HTML")
print("=" * 75)


# 7- Arbitrary Keyword Arguments, **kwargs

def user_skills(name, **langs):
    
    print( type(langs) )

    print(f"Hello {name}, your skills with progress are: =>")
    
    for key, value in langs.items():
        print(f"---> {key} => {value}")
        
langs = {
    "Python": "80%",
    "Js": "90%",
    "PHP": "70%"
}
        
user_skills("Yehya", **langs)
print("=" * 75)

# 8- Function Scope

x = 0

def one():
    global x
    x = 1
    print(f"From function one {x}")
    
def two():
    x = 2
    print(f"From function two {x}")
    
    def three():
        x = 3
        print(f"From function three {x}")
    
    three()
    
    
print(f"From global {x}")

one()

print(f"From global {x}")

two()
print("=" * 75)

# 9- Function Recursion

def factorial(x):
    
    if x == 1:
        return 1
    
    return x * factorial(x-1)

print(factorial(5))
print("=" * 75)


def clean_list(numbers):
    
    if len(numbers) == 1:
        return numbers
    
    if numbers[0] == numbers[1]:
        return clean_list(numbers[1:])
    
    return [numbers[0]] + clean_list(numbers[1:])
    
nums = [1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 8, 9, 9, 9, 10]

print(clean_list(nums))
print("=" * 75)

# 10- Function Lambda

# def say_hi(name):
#     return f"Hello {name}"

# result = say_hi("Yehya")
# print(result)


# result = lambda name: f"Hello {name}"

# print(result("Yehya"))

def sum_two(n1, n2): return n1 + n2

result = sum_two(1, 2)


print(result)

result = lambda n1, n2: n1 + n2

print(result(1, 2))

print( sum_two.__name__ )
print( result.__name__ )



