# sets{} vs List[] vs tuples()

# If you have variable a, b, c, a

# The differnece between a "List vs tuple" is a threat called mutability.
# Lists can be changed and manipulated afterwards, while tuples cant


#Tuples
A = ('a', 'b', 'c', 'a')
A[0] #We ask for the index number
print(A)

#List
B = ['a', 'b', 'c', 'a']
B[0] = "B" #Ive added "B" into index 0
B.append("d") #Ive added "d" to the end of our list
B.remove("b") #Ive removed "b" from our list (Where ever it is)
print(B)


#Sets
C = {'a', 'b', 'c', 'a'}
# Sets eliminates duplicate values and only shows the last one. So result = b, c, a. its unordered
#If we index a set, we'll get an error

#We can convert a list into a set like:
nums = [1, 3, 3, 1, 2, 4, 5, 2, 4]
nums = set(nums) #Oddly enough. since we typecasted it to a set. It's still ordered.
print(nums)


