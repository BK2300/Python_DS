# Continueation of folder 7. Mutable and immutable data types
# its more like a excercise day

# converting a string to a list
abcde = "a,b,c,d,e"
chars = abcde.split(',')
print(chars)
# ['a','b','c','d','e']
text = "In the beginning was the Word"
print(text.split())
# ['In', 'the', 'beginning', 'was', 'the', 'Word']



#Excercise1. (receive a line of text and find the longest inputted word)
"""
a = input("Write a sentence: ")
words = a.split()
Longest_word = max(words, key=len)

print(f"Maximum = {Longest_word}")
    #The inputted sentence is been splittet into seperate elements
    #Then max find outs whats the longest word you used by characters and outputs that
"""

#Excercise2. (calculates the total number of words and The average word length)
b = input("Write a sentence: ")
words = b.split()
total_words = len(words)
total_length = sum(len(word) for word in words)
average_length = total_length / total_words

print(f"\nTotal number of words: {total_words}")
print(f"Average word length: {average_length:.2f}")


# Sets
# A Sets order is randomized orddly enough. even if converted from a list to a set. or directly taken from a set
fruits_list = ["apple", "banana", "orange"]
fruits_set = {"apple", "banana", "orange"}

fruits_set = set(fruits_list)
print(fruits_set) # {'banana', 'orange', 'apple'}


#Dictionary
months = {}
months["January"] = 31
months["February"] = 28
months["March"] = 31
months["April"] = 30
months["May"] = 31
print(len(months)) # 5
print(months) # {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31}
print(months.keys()) #show the keys of months ['January', 'February', 'March', 'April', 'May']
print(months.values()) #Shows values of the motnh [31, 28, 31, 30, 31]
print(months.items())
# shows both keys and values([('January', 31), ('February', 28), ('March', 31), ('April', 30), ('May', 31)])
print("June" in months) # False
print("January" in months) # True

#Looping through dictonary(months)
for key, value in months.items():
print("Key=", key, ", Value=", value)
    # Key= January , Value= 31
    # Key= February , Value= 28
    # Key= March , Value= 31
    # Key= April , Value= 30
    # Key= May , Value= 31


# Dictionaries vs. lists
- print({"a":7,"b":5}=={"b":5,"a":7}) # prints True
- print(["a", "b"] == ["b", "a"])







