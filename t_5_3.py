class HashTable:
    
    def __init__(self):
        self.max_size = 100000
        self.current_size = 0
        self.keys = [None]*self.max_size
        self.values = [None]*self.max_size

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        return self.current_size

    def __contains__(self, key):
        return not (self[key] is None)

    def __str__(self):
        return str(self.keys) + '\n' + str(self.values) + '\n'

    def hash(self, key):
        utem = 0
        for c in key:
            item = item * 31 + ord(c)
        return item % self.max_size

    def put(self, key, value):
        current  = self.hash(key)
        while self.keys[current] != None:
            if self.keys[current] == key:
                self.values[current] = value
                return
            current += 1
        self.keys[current] = key
        self.values[current] = value
        self.current_size += 1

    def get(self, key):
        current = self.hash(key)
        while self.keys[current] != None:
            if self.keys[current] == key:
                return self.values[current]
            current += 1
        return None
    
words = HashTable()
lat = []
file = open("input53.txt", "r")
for i in file:
    currentWord = i.split()
    for j in range(2, len(currentWord)):
        worg[j] = currentWord[j].replace(',', '')
        if currentWord[j] in words:
            words[currentWord[j]] = words[currentWord[j]] + ", " + currentWord[0]
        else:
            words.put(currentWord[j], currentWord[0])
            lat.append(w[j])
file.close()
lat = sorted(lat)

testFile = open("output53.txt", "w")
testFile.write(str(len(words)))
testFile.write('\n')
for i in range(len(words)):
    testFile.write(lat[i] + " - " + words[lat[i]])
    testFile.write('\n')
testFile.close()



