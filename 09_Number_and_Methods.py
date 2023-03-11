# ============================ Number and Methods ============================
# ---> int => Integer
print( type( 10 ) )
print( type( -10 ) )
print("=" * 75)

# ---> float => Floating-Point Numbers
print( type( 10.9 ) )
print( type( -10.89 ) )
print("=" * 75)

# ---> comples => Complex Numbers
print( type( 10 + 2j ) )
print( type( -4.8 + 4j ) )
print( type( 4.1 - 8.9j ) )
print("=" * 75)

# ---> We can convert int to float and complex using float() and complex() methods.
i = 15
f = float( i )
print( f )
print( type( f ) )

c = complex( i )
print( c )
print( type( c ) )
print("=" * 75)

# ---> We can convert float to int and complex using int() and complex() methods.
f = 15.9
i = int( f )
print( i )
print( type( i ) )

c = complex( f )
print( c )
print( type( c ) )
print("=" * 75)

# ---> We cannot convert complex to int or float
c = 10 + 2j

real_part = c.real
print( real_part )
print( type( real_part ) )

imaginary_part = c.imag
print( imaginary_part )
print( type( imaginary_part ) )
print("=" * 75)


# Arithmetic Operators:
print(10 + 2)
print(10 - 8)
print(20 * 3)
print(100 / 4)
print(103 // 4) 
print(104 // 4)
print(2 ** 4) # 2 * 2 * 2 * 2 
print(5 ** 3) # 5 * 5 * 5
print(10 % 3) # 1
print(26 % 3) # 2
print(4 % 2) # 0
print("=" * 75)

