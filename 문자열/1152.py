words = input('')
words = words.split(' ')
words = [w for w in words if w]
print(len(words))

words = input('')
words = words.split(' ')
words = list(filter(None, words))
print(len(words))