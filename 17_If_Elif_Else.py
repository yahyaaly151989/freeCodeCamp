# ========================== Control Flow - If, Elif, Else ===========================


# Syntax:
# if condition:
#     Code to run if this condition True
# elif condition:
#     Code to run if this condition True
# else:
#     Code to run if all are false

# x = 0

# if x > 0:
#     print("Positive.")
# elif x < 0:
#     print("Negative.")
# else:
#     print("Zero")
    

# number = int(input("Enter a number. ").strip())

# if number < 18:
#     print(f"The number {number} is less than 18.")
# elif number >= 18 and number <= 40:
#     print(f"The number {number} is between 18 and 40")
# else:
#     print(f"The number {number} is greater than 40.")

age = 20
has_skills = False

if age > 18:
    print("Good, the age > 18")
    
    if has_skills:
        print("Good, you are accepted!")
    else:
        print("Bad, you are NOT accepted!")
        
is_subsribed = True

print("Welcome to my channel" if is_subsribed else "Please subsribe to our channel")

