# Description:
    """Write a program that iterates over all even numbers between 1 and 100.
    If thenumber is divisible by 6,  increment a counter.
    At the end of your program,print how many numbers are divisible by 6"""

x = 2
counter = 0

while x <= 100:
    if x % 6 == 0:
        counter += 1
    x += 2   # hopper direkte til næste lige tal

print("The amount of numbers from 1- 100, that is divisibel with 6:", counter)










