freq = {}   # frequency of words in text
line = input("Enter you text here: ")
for word in line.split():
    word = word.lower()
    freq[word] = freq.get(word, 0) + 1 # It checks whether the value for word is already there if not it defaults to 0, only for dicts

words = freq.keys()
numb = freq.values()
# freq.items()
#print(words, numb)
#for i in words:
#    print(words[i], numb[i])

#print(freq)
for word in sorted(words):
    print(f'The frequency of the word "{word}" is {freq[word]}')
