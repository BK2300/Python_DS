user_input = input("how was you doing today?: ")


if len(user_input) < 10:
    print("Thats was brief!")
elif len(user_input) > 30:
    print("Wow, you had a lot to say")
else:
    print("Thanks for sharing")



