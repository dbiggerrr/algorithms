class Node:
    def __init__(self,lat,eng):
        self.lat =  lat
        self.eng  = [eng]
        self.next=None
        self.valid = True


class HashTable:
    M= 503
    N=31
    def __init__(self):
        self.values = [None for i in range(HashTable.M)]
        self.lat = []
        self.leng=0

    def  hashString(self,s):
        hashItem = 0
        for i in range(len(s)):
            hashItem = hashItem * HashTable.N + ord(s[i])
        return hashItem % HashTable.M

    def open(self):
        with open("input63.txt", "r") as file:
            for line in file:
                eng, latString = line.strip().split(' - ')
                latList = latString.split(', ')
                for lat in latList:
                    self.addNewItem(lat,eng)

    def addNewItem(self,lat,eng):
        hash_key = self.hashString(lat)
        slot = self.values[hash_key]
        while slot != None:
            if slot.lat == lat:
                slot.eng.append(eng)
                slot.valid = True
                return
            slot = slot.next
        self.leng += 1
        slot = Node(lat, eng)
        self.lat.append(lat)
        slot.next = self.values[hash_key]
        self.values[hash_key] = slot

    def findByLat(self,lat):
        hash_key = self.hashString(lat)
        slot = self.values[hash_key]
        temp = []
        while slot != None:
            temp.append(slot.eng)
            slot = slot.next
        return temp

    def write(self):
        with open('output63.txt', 'w') as file1:
            file1.write(str(self.leng) + '\n')
            self.lat = sorted(self.lat)
            for word in self.lat:
                answer = word + " - "
                temp  = self.findByLat(word)
                count = 0
                for eng in temp:
                    eng.sort()
                    for el in eng:
                        if count == 0:
                            count+=1
                            answer+= el
                        else:
                            answer+= ", " + el
                file1.write(answer+'\n')

test = HashTable()
test.open()
test.write()
