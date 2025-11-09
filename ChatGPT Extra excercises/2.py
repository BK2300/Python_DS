from itertools import count

sales = [120, 150, 90, 200, 250, 170, 300, 280, 310, 400, 380, 420]

average = sum(sales)/len(sales)

print(sum(sales)) #3070
print(max(sales)) #420
print(min(sales)) #90
print(average) #255.83333333333334

number = average

if number >= 250:
    print("Excellent performance!")
elif number > 150 and number < 250:
    print("Good performance.")
else:
    print("Needs improvement.")
# chatgpt version:
"""
if average >= 250:
    print("Excellent performance!")
elif 150 < average < 250:
    print("Good performance.")
else:
    print("Needs improvement.")
"""

count_above = 0

for s in sales:
    if s > average:
        count_above += 1

print(f"{count_above} months were above average")

