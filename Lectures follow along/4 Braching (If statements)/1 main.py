# Braching is If statements
# Is the moment when you typically have the option to take a decision
# An If-statement always starts out with "If". Then ends with a "else"
# In between, if you want to put more options in between. You use a "elif"

# Good for comparison operators & Logic operators

# Comparison operators:
"""
| Operator | Betydning                | Eksempel  | Resultat |
| -------- | ------------------------ | --------- | -------- |
| `==`     | Er lig med               | `5 == 5`  | `True`   |
| `!=`     | Er ikke lig med          | `5 != 3`  | `True`   |
| `>`      | Større end               | `10 > 7`  | `True`   |
| `<`      | Mindre end               | `4 < 2`   | `False`  |
| `>=`     | Større end eller lig med | `8 >= 8`  | `True`   |
| `<=`     | Mindre end eller lig med | `6 <= 10` | `True`   |
"""

# Logical operators:
"""
| Operator | Betydning                           | Eksempel              | Resultat |
| -------- | ----------------------------------- | --------------------- | -------- |
| `and`    | Begge betingelser skal være sande   | `(5 > 3) and (8 > 6)` | `True`   |
| `or`     | Mindst én betingelse skal være sand | `(5 > 3) or (8 < 6)`  | `True`   |
| `not`    | Gør sand til falsk (og omvendt)     | `not (5 > 3)`         | `False`  |
"""

#Simple If/Else
temperature = int(input("What the temperature today: " ))

if temperature >= 20:
    print("It’s a warm day.")
else:
    print("It’s a cold day.")


# if/elif/else
number = int(input("Enter a number: "))

if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")


#Nested if
age = 25

if age >= 18:
    if age >= 65:
        print("You are a senior citizen.")
    else:
        print("You are an adult.")
else:
    print("You are a minor.")






