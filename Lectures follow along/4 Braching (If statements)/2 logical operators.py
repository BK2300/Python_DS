# More logical operators examples:

# And & or
age = 25
has_ticket = True
is_vip = False

if (age >= 18 and has_ticket) or is_vip:
    print("Access granted")
else:
    print("Access denied")


# is and is not
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True  (samme objekt)
print(a is c)   # False (samme indhold, men forskelligt objekt)
print(a is not c)   # True


# combination:
age = 20
has_ticket = True
guest_list = ["Anna", "Bo", "Clara"]
name = "Bo"

if (age >= 18 and has_ticket) and (name in guest_list):
    print("Welcome in!")
else:
    print("Access denied.")

