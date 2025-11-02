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


