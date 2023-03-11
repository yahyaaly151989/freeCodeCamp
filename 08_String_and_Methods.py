# ============================ String and Methods ============================
# 1- What is a String?

# type()
my_string = "Hello Python!"
my_string = 'Hello Python!'
my_string = """Hello Python!"""
my_string = '''Hello Python!'''
print( type(my_string) )

# len()
print( len(my_string) )


# 2- What is String Indexing?
my_string = "I love Python"   
print( my_string[0] ) # I
print( my_string[1] ) # " "
print( my_string[2] ) # l
print( my_string[-1] ) # n
print( my_string[-2] ) # 0
print(" " * 75)

# 3- What is String Slicing?
my_string = "I love Python"
print( my_string[0:6:1] ) # I love
print( my_string[0:6] ) # I love
print(" " * 75)

print( my_string[:13] ) # I love Python
print( my_string[2:] ) # love Python
print( my_string[:] ) # I love Python
print( my_string[::2] ) # Ilv yhn
print( my_string[::3] ) # Io tn
print( my_string[::-1] ) # nohtyP evol I

# ---> String is immutable data type. => We cannot add, edit, or delete its elements.
my_name = "Alaa"
# my_name[0] = "Y" # TypeError: 'str' object does not support item assignment
print(my_string)
print("=" * 75)

# ---> String Methods
# print(dir(str))
# print(help(str))

# ---> strip()
# ---> rstrip()
# ---> lstrip()

a = "    I love Python    "
print(a)
print( a.strip() ) 
print("=" * 75)

a = "########I love Python##########"
print( a.strip() )
print( a.strip("#") )
print( a.rstrip("#") )
print( a.lstrip("#") )
print("=" * 75)


# ---> capitalize() => Converts the first character to upper case
a = "yehya ali"
print( a.capitalize() )
print("=" * 75)

# ---> title() => Converts the first character of each word to upper case
a = "yehya ali alaa ahmad"
print( a.title() )
print("=" * 75)

# ---> upper() => Converts a string into upper case
a = "I love Python"
print( a.upper() )
print("=" * 75)

# ---> lower() => Converts a string into lower case
a = "I love Python"
print( a.lower() )
print("=" * 75)

# casefold()	Converts string into lower case
a = "I love Python"
print( a.lower() )
print("=" * 75)

# ---> swapcase() => Swaps cases, lower case becomes upper case and vice versa
a = "I LOve PythOn."
print( a.swapcase() )
print("=" * 75)

# ---> zfill() => Fills the string with a specified number of 0 values at the beginning
a, b, c = "1", "11", "111"
print( a.zfill(3) )
print( b.zfill(3) )
print( c.zfill(3) )
print("=" * 75)


# ---> count(element) => Returns the number of times a specified value occurs in a string
a = "I love Python because Python is easy."
print( a.count("Python") )
print( a.count("e") )
print("=" * 75)


# ---> find() => Searches the string for a specified value and returns the position of where it was found
# ---> index() => Searches the string for a specified value and returns the position of where it was found
a = "I love Python, I love it because Python is easy."
print( a.index("I") )
print( a.index("Python") )
# print( a.index("Z") ) # error

print( a.find("I") )
print( a.find("Python") )
print( a.find("Z") ) # -1
print("=" * 75)

# ---> split(separator) => Splits the string at the specified separator, and returns a list
# ---> separator by default => space
a = "I love Python"
print( a.split() )
print( a.split(" ") )
print( a.split("P") )
print("=" * 75)

a = "I love Python and programming"
print( a.split(" ", 2) )
print( a.rsplit(" ", 2) )
print("=" * 75)

# ---> splitlines() => Splits the string at line breaks and returns a list
a = "I\nlove\nPython"
print(a)
print( a.splitlines() )
print("=" * 75)

# ---> join() => Converts the elements of an iterable into a string
b = ["Yehya", "Ahmad", "Alaa"]
print( " | ".join(b) )
print("=" * 75)

# partition()	Returns a tuple where the string is parted into three parts
a = "I love Python and programming"
print( a.partition("and") )
print( a.partition("zzz") )
print("=" * 75)


# replace()	Returns a string where a specified value is replaced with a specified value
a = "I love Python and programming, because Python is easy."
print( a.replace("Python", "JavaScript") )
print( a.replace("Python", "JavaScript", 1) )
print("=" * 75)

# center()	Returns a centered string
a = "I love Python"
print( len(a) )
print( a.center(21) )
print( a.center(21, "-") )
print("=" * 75)

# ljust()	Returns a left justified version of the string
a = "I love Python"
print( len(a) )
print( a.ljust(21) )
print( a.ljust(21, "-") )
print("=" * 75)

# rjust()	Returns a right justified version of the string
a = "I love Python"
print( len(a) )
print( a.rjust(21) )
print( a.rjust(21, "-") )
print("=" * 75)


# ---> startswith() => Returns True if the string starts with the specified value
a = "I love Python"
print( a.startswith("I") )
print( a.startswith("Z") )
print( a.startswith("P", 7, 13) )
print("=" * 75)

# ---> endswith() => Returns True if the string ends with the specified value
a = "I love Python"
print( a.endswith("n") )
print( a.endswith("e") )
print( a.endswith("e", 2, 6) )
print("=" * 75)

# ---> istitle() => Returns True if the string follows the rules of a titl
a = "I Love Python"
print( a.istitle() )

# ---> isupper() => Returns True if all characters in the string are upper case
a = "I Love Python"
print( a.isupper() )
print("=" * 75)

# ---> islower() => Returns True if all characters in the string are lower case
a = "I Love Python"
print( a.islower() )
print("=" * 75)


# ---> isnumeric() => Returns True if all characters in the string are numeric
a = "1234"
b = "123yehya45"
print( a.isnumeric() )
print( b.isnumeric() )
print("=" * 75)

# ---> isalpha() => Returns True if all characters in the string are in the alphabet
a = "1234"
b = "123yehya45"
c = "yehya"
print( a.isalpha() )
print( b.isalpha() )
print( c.isalpha() )
print("=" * 75)

# ---> isalnum() => Returns True if all characters in the string are alphanumeric
a = "1234"
b = "123yehya45"
c = "yehya"
d = "yehya@"
print( a.isalnum() )
print( b.isalnum() )
print( c.isalnum() )
print( d.isalnum() )
print("=" * 75)

# ---> isidentifier() => Returns True if the string is an identifier
a = "100name" #False
b = "my_name" # True
print( a.isidentifier() )
print( b.isidentifier() )
print("=" * 75)

# isspace()	Returns True if all characters in the string are whitespaces
a = " "
b = ""
print( a.isspace() )
print( b.isspace() )
print("=" * 75)

# print(dir(str))


# ---> Concatenation:
a = "Hello"
b = "Python"
s = " "
c = a + s + b
print(c)
print("=" * 75)


name = "Yehya"
age = 33
print("My name is " + name)
# print("My age is " + age) # TypeError: can only concatenate str (not "int") to str
print("=" * 75)

# ---> String Formatting:
name = "Yehya"
age = 20
ranking = 9.7


print("My name is %s and my age is %s and my ranking is %s " %(name, age, ranking))
print("My name is %s and my age is %d and my ranking is %f" %(name, age, ranking))
print("My name is %s and my age is %d and my ranking is %.2f" % (name, age, ranking))
print("=" * 75)

print("My name is {} and my age is {} and my ranking is {}" .format(name, age, ranking))
print("My name is {:s} and my age is {:d} and my ranking is {:f}" .format(name, age, ranking))
print("My name is {:s} and my age is {:d} and my ranking is {:.2f}" .format(name, age, ranking))
print("=" * 75)

print(f"my name is {name}, my age is {age}, my ranking is {ranking}")
print(f"my name is {name:s}, my age is {age:d}, my ranking is {ranking:f}")
print(f"my name is {name:s}, my age is {age:d}, my ranking is {ranking:.2f}")
print("=" * 75)

# ---> Escape Sequences Characters
# ---> \b
a = "Hello\bPython"
print(a)
print("#" * 75)

# ---> \
a = "Hello \"Python\""
b = 'Hello \'Python\''
c = "Hello \\ Python"
d = "Hello \
Python"
print(a)
print(b)
print(c)
print(d)
print("#" * 75)

# ---> \n
print( "Hello\nPython" )
print("#" * 75)

# ---> \t
a = "Hello\tPython"
print( a )


b = a.expandtabs(20)
print(b)

