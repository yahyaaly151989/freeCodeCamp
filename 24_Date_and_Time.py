# ========================= Date and Time =========================
import datetime

# print(datetime)

# print(dir(datetime))
# print(dir(datetime.datetime))

print(datetime.datetime.now())
print("=" * 75)

print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print("=" * 75)

print(datetime.datetime.now().time())
print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)
print(datetime.datetime.now().time().second)
print("=" * 75)

my_birth = datetime.datetime(1989, 5, 1)

print(my_birth.strftime("%a"))
print(my_birth.strftime("%A"))
print(my_birth.strftime("%b"))
print(my_birth.strftime("%B"))
print(my_birth.strftime("%y"))
print(my_birth.strftime("%Y"))




