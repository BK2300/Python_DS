# sets{} vs List[] vs tuples()

# If you have variable a, b, c, a

# The differnece between a "List vs tuple" is a threat called mutability.
# Lists can be changed and manipulated afterwards, while tuples cant

A = ('a', 'b', 'c', 'a') #Tuples
A[2] #We ask for the index number


B = ['a', 'b', 'c', 'a'] #List
B[2] = "B"

C = {'a', 'b', 'c', 'a'} #Sets
# Sets eliminates duplicate values and only shows the last one. So result = b, c, a. its unordered
#If we index a set, we'll get an error

#We can convert a list into a set like:
nums = [1, 3, 3, 1, 2, 4, 5, 2, 4]
nums = set(nums) #Oddly enough. since we typecasted it to a set. It's still ordered.
print(nums)


# The differnece between a "List vs tuple" is a threat called mutability.
# Lists can be changed and manipulated afterwards, while tuples cant
B.append("d") #OR!
B.remove("b")
print(B)

