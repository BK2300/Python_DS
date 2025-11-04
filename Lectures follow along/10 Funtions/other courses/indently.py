# reuseable data

from datetime import datetime

def show_date() -> None:
    print("This is the current time: ")
    print(datetime.now())

show_date()
show_date()


# what if we want to use parameters?
def greet(name: str) -> None:
    print(f"Hello, {name}")

greet("Bob")
greet("Alex")


# Functions can return results
def add(a: float, b: float) -> float:
    return a+b

print(add(1,2)) #the output here is argument

