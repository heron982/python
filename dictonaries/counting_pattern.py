counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')

for word in words:
    counts[word] = counts.get(word, 'eae') + ' hello'
print('Counts', counts)

