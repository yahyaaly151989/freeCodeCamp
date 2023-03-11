# ============================ Data Types Overview ============================
# 1- What is Data Type?

# ---> Data is stored in computer memory.
# ---> We use variables to refer to this data.

# 2- What are Data Types in Python?
# ---> type()

# ---> All data in Python is object.

# ---> str => String
print( type( "Yehya" ) )
print( type( 'Ahmad' ) )
print("#" * 75)

# ---> int => Integer
print( type(10) )
print( type(-90) )
print("#" * 75)

# ---> float => Float
print( type( 10.9 ) )
print( type( -8.79 ) )
print("#" * 75)

# ---> complex => Complex
print( type( 2 - 2j ) )
print( type( 12 + 90j ) )
print("#" * 75)

# ---> list => List
print( type(  [1, 2, 3]  )  )
print("#" * 75)

# ---> tuple => Tuple
print( type(  (1, 2, 3)  )  )
print("#" * 75)

# ---> set => Set
print( type(  {1, 2, 3}  )  )
print("#" * 75)

# ---> dict => Dictionary
print( type(  {"one": 1, "two": 2}  )  )
print("#" * 75)

# ---> bool => Boolean
print( type( True ) )
print( type( False ) )
print( type( 10 == 10 ) )
print("#" * 75)

# ---> None => NoneType
print( type( None ) )
print("#" * 75)
