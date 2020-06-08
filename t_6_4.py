import re
class Node:
    def __init__(self,word):
        self.word =  word
        self.amount  = 0
        self.next=None
        self.valid = True

class HashTable:
    M= 100007
    N=31
    def __init__(self):
        self.values = [None for i in range(HashTable.M)]

    def add_word(self,word):
        itemKey = self.hash_str(word)
        var = self.values[itemKey]
        while var != None:
            if var.word == word:
                var.amount +=1
                var.valid = True
                return
            var = var.next
        var = Node(word)
        var.next = self.values[itemKey]
        self.values[itemKey] = var

    def  hash_str(self,s):
        hashItem = 0
        for i in range(len(s)):
            hashItem = hashItem * HashTable.N + ord(s[i])
        return hashItem % HashTable.M

    def open_file(self):
        file = open('input64.txt', 'r', encoding="UTF-8")
        for l in file:
            currentLine = re.sub('[^A-Za-z]', ' ', l)
            lineArray = currentLine.lower().split()
            for word in lineArray:
                self.add_word(word)
        file.close()

    def write(self):
        testFile = open('output64.txt', 'w')
        tetList = []
        for i in range(HashTable.M):
            if self.values[i]==None:
                continue
            else:
                tetList.append(self.values[i].word)
        tetList = sorted(tetList)
        for i in tetList:
            testFile.write(i + "\n")
        testFile.close()

test = HashTable()
test.open_file()
test.write()
