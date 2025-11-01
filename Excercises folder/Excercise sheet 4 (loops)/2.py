# Write a program to print the sum of digits of a given number.
# example: input:1234, output:  10


num = 1234
total = 0

while num > 0:
    total += num % 10
    num //= 10

print("the sum of digits:", total)






