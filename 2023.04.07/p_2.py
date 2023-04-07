words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']


myset = set()
for i in range(len(words)):
    wrd = words[i].lower()
    l = wrd[:1]
    myset.add(l)


print(*sorted(myset))
