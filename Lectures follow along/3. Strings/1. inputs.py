# Define variables that we need
nbr_nimutes = 0 #input: number of minutes (int) --> input
nbr_hours = 0 #output: number og hours (int) --> output
nbr_remaining_minutes = 0 #output:
str_message = "" #output: message to be printed (string) --> output


user_input = int(input("Enter the number of minutes: ")) # input as string
nbr_minutes = int(user_input) #convert to interger

nbr_hours = nbr_minutes//60 #// division
nbr_remaining_minutes = nbr_minutes % 60

print(f"this is the hours: {nbr_hours} This is the remaining numbers of minutes : {nbr_remaining_minutes}")


"""we use tree double quotes
for multiline comments
string"""


"""use a \ before a ' or " if you want to use it in a string. or else itss might mess
up your string or print output"""


"""\n starts a new line
\t starts a new tab
\\ writes a backslash"""





