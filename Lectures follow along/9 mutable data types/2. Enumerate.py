# Enumerate is used to loop over a list. And makes look like a matrix.
# it sort of converts the input/String into rows and give them numbers in front.


# Starting with index 1
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


#Employee
employees = ["Anna", "Bo", "Clara"]

for id, name in enumerate(employees, start=1001):
    print(f"Employee ID {id}: {name}")


#Find index of a specifict element
numbers = [10, 20, 30, 40, 50]

for index, value in enumerate(numbers):
    if value == 30:
        print(f"Found {value} at index {index}")


# strings
lines = ["Hello", "This is Python", "Enumerate is useful"]

for line_number, line in enumerate(lines, start=1):
    print(f"{line_number}: {line}")

#Another one
colors = ["red", "green", "blue", "yellow"]

for i, color in enumerate(colors, start=10):
    print(f"{i}: {color.upper()}")









