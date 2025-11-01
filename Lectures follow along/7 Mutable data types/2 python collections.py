# Tuple is ordered and unchangeable. Allows duplicate members.(Immutable)
t = (1,2,3,1)
# List is ordered and changeable. Allows duplicate members.
l = [1,2,3,1]
# Set is unordered and unindexed. No duplicate members.
s = {1,2,3}
# Dictionary is ordered and changeable. No duplicate members.
d = { "a": 1, "b": 2, "c": 3, "d": 1 }


# Tuples are used to store multiple items in a single variable.
# Tuple items are ordered, unchangeable , and allow duplicate values.
fruits = ("apple", "banana", "cherry", "apple",
"cherry")
# print(type(fruits))

fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(len(fruits))
# 5
for item in fruits:
    print(item) #will output vertical each fruit

# Tuple Methods
fruits = ("apple", "banana", "cherry", "apple",
"cherry")
# fruits.append("orange") #Cant add in this situation
print(fruits.count("apple")) # 2
print(fruits.count("banana")) # 1
print(fruits.index("cherry")) #2
# print(fruits.index("orange")) #Error

print() #Just to start a new line


# Lists [ ]
emptyList = [] # creates an empty list, bound to emptyList
grocery = ["milk", "eggs", "bread"] # creating a list with length 3
print(len(grocery))
print(grocery[-1]) # → bread
# print(grocery[3]) # → IndexError: list index out of range
print(grocery[-3]) # → milk

grocery[0] = "salt"
grocery[-1] = "sugar"
print(grocery) # → ['salt', 'eggs', 'sugar']
for item in grocery:
    print(item)

# List vs Tuple
"""Lists are denoted by square brackets [ ] and Tuples are denoted with parenthesis
(). Once defined, tuples have a fixed length and lists have a dynamic length.
Tuples are generally faster than the Lists
Lists consume more memory compared to Tuples """
import sys
person_info_list = ["Peter Schmeichel", 1960, 1.93]
person_info_tuple = ("Peter Schmeichel", 1960, 1.93)
print(sys.getsizeof(person_info_list)) # 88
print(sys.getsizeof(person_info_tuple)) # 64


# dictionary
weather_today = {
"city": "Copenhagen",
"temperature_celsius": 14,
"humidity_percent": 82,
"condition": "Cloudy",
"wind_kph": 18,
"forecast": ["Cloudy", "Light rain", "Clear"]
}






