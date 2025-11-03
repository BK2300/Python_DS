# program name: lectures on site
# file name: lecture

#Definition: this program decides if the lecture will held the lecture on site or online
#input: we ask the user if the weather is good or not(True /False)
# output: The program outputs if the lecture will be held on site or online

# declaration of constants, variables, and data types
weatherGood = True
inDenmark = True

str_weatherGood = input("is the weather good? (Yes/No): ")

weatherGood = bool(str_weatherGood == "True")

if str_weatherGood.lower() == "yes":
    weatherGood = True
elif str_weatherGood.lower() == "no":
    weatherGood = False
else:
    print("Invalid answer. Please answer with YES or NO")

print(f"\nYou answered {str_weatherGood}\n")

if weatherGood:
    print("The lecture will be held on site. ")
else:
    print("the lecture will be held online. ")

# fun fact. a boolean dont care if you right true or false. in "Caps" or "ALL CAPS"









