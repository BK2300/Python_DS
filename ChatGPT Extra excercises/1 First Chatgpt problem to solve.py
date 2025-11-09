x = "Data is the new oil! Data drives modern technology, and technology powers the world."

# 1. Gør teksten små bogstaver og del den op
words = x.lower().replace('.', '').replace(',', '').replace('!', '').split()

# 2. Opret en tom dictionary
word_freq = {}

# 3. Loop igennem alle ord
for word in words:
    if word in word_freq:
        word_freq[word] += 1  # hvis ordet findes, læg 1 til
    else:
        word_freq[word] = 1   # ellers opret ordet med værdien 1

# 4. Print resultatet
print(word_freq)

# 5. Find det mest hyppige ord
most_common = max(word_freq, key=word_freq.get)
print(f"The most frequent word is '{most_common}' ({word_freq[most_common]} times).")



