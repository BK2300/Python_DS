# I Have no idea how to tackle this without "hardcoding" or what a docstring is...

#1)
cart = ["Apple", "Apple", "Pomegranate", "Kaki", "Kaki", "Banana", "Kaki", "Apple", "Kaki", "Banana"]
# My dictionary ive created. Tought of the first list i could make with strings, that made sense to repeat

#2 & 3)
def word_frequency(words: list) -> dict:
# A function looping through my list
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1 #Counting each unique words repeated
        else:
            word_freq[word] = 1 #Dont count. Just give 1 if its unique
    return word_freq

def get_unique_words(words: list) -> set: #function converting my list to a set
    return set(words)

def most_common_word(freq_dict: dict) -> str:
# a function that finds the word with the highest frequency in a dictionary.
    return max(freq_dict, key=freq_dict.get)

x = word_frequency(cart)
y = get_unique_words(cart)
z = most_common_word(x)

print(x)
print(y)
print(z)