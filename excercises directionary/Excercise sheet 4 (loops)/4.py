# Write a program to display the pattern like a diamond.  Example:

triangle_line = ""
direction = 1
number_wildcards = 12

for i in range(1, number_wildcards * 2):
    print(triangle_line + "*")
    triangle_line += "*"

    if len(triangle_line) == number_wildcards: #
        direction = -1

    if direction == -1:
        triangle_line = triangle_line[:-2]