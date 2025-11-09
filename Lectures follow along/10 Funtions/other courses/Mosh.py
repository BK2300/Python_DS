
               # Parameters. they are all required to be used. If you miss one. You'll get an error
def greet(first_name, last_name):
    #if you press enter. its going to give an indentation, which is like "next line, plus tab". Meaning the following code belongs to this function
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")

greet("Long", "Schlong") # arguments
greet("John", "Cena")


# Types of functions
"""There is two types of functions. 
1: That performs a task
    print and greet Performs a task.
2: That returns a value
    While "round(1.9)" calculates and returns a value
"""

def get_greetign(name):
    return f"hi {name}"

message = get_greetign("Long")
# file = open("content.txt", "w")
# file.write(message) #Creates a txt file for us. a bit more advanced then we're used to yet






