name = input("What is your name?: ")
while not name.isalpha():
    name = input("plz. Try again. With no numbers and only letters this time: ")

print(f"hello {name}")

age = input("What is your age?: ")
while not age.isdigit():
    age = input("plz. Try again. With only numbers this time: ")

print(f"hello {name}, you're {age} young")

adress = input("where do you live?: ")
while not adress.isalpha():
    adress = input("plz. Try again. With no numbers and only letters this time: ")

print((f"Name = {name}, Age = {age}, Adress = {adress}"))
confirmation = input("Are all your information correctly written? (Yes/No): ")
if confirmation.lower() == "no":
    print("You have to reset this program.")
    exit()
else:
    print("Great")
print(f"Your name is {name}. You're {age} years old & you live in {adress}")
print("Its really nice to meet you. Hope you pass you midterms exam")



