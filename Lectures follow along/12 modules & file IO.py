#Modules is a files with a bounce of functions. Like Pandas or Numpy


# File IO
"""
- Open() return a file object
- most commonly used with two arguments:
open(filename, mode)

Tror det betyder du har gemt en file eller dokument, som en variable. Så den er lettere at få adgang til
"""


# Absolute vs relative path
# Absolute path = er den fulde linje "C\Bacon\Fizz\spam.txt" (eksempel fra leksionen)
# Relative path = den kompakte linge "...\Fizz\spam.txt"


# example from lectures
        import pandas as pd

        csv_path = "netflix_titles.csv" #CSV-filen er ikke oploadet endnu

        df = pd.read_csv (csv_path)
        print(df.head())

        print (df.columns)

        print (list(df.columns))

        for col in df.columns:
            print(col)



