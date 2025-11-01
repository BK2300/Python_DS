# Mutable data types are those whose values can be modified after they are created,
# While Immutable data types are those whose values cannot be modified once created.

# the type of data that are:
# Immutable = int, float, bool, str, tuple, fronzenset
# Mutable = List, dict, set, bytearray
# if you can use "obj.append() || obj.update()" then its mutable

# List is mutable
numbers = [1, 2, 3]
numbers[0] = 99 #Ive replaced integer = 99 into index 0
print(numbers)

# Tuples is immutable
"""coords = (1, 2, 3)
coords[0] = 99
"""

# Sets is mutable
fruits = {"apple", "banana", "orange", "apple"}
print(fruits) # {'banana', 'apple', 'orange'}
# Its cool, because it removes duplicates

# Can also be used for Set theory. Read more in file "1.2 set theory"



# Dictionary is mutable
# is a combination of keys and values paired
person = {
#    Keys : Values
    "name": "Anna",
    "age": 25,
    "city": "Odense"
}

print(person["name"])  # Anna
print(person["age"])   # 25

#Adding extra keys
person["job"] = "Data Scientist" #Adding a key
print(person["job"])
person["age"] = 26 #Changing a key
del person["city"] #Removing a key

for key, value in person.items():
    print(key, "→", value)

