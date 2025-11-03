# Typecasting:
# Fra heltal til decimaltal
x = 5
y = float(x)   # y = 5.0

# Fra decimaltal til heltal
a = 3.7
b = int(a)     # b = 3

# Fra tal til tekst
num = 10
text = str(num)   # text = "10"

# Fra tekst til tal
s = "25"
n = int(s)        # n = 25

# Fra liste til tuple
lst = [1, 2, 3]
tup = tuple(lst)  # tup = (1, 2, 3)
"""Tuples kan ikke ændres – de er immutable, så dataene bliver beskyttet mod utilsigtede ændringer.
→ Bruges til data, der ikke må ændres.
Tuples er hurtigere end lister, især ved store datamængder.
Tuples kan bruges som nøgler i dictionaries, fordi de er uforanderlige."""






