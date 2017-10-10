import datetime
import re


class BinaryIndexedTree():
    def __init__(self, size):
        self.size  = size
        self.nodes = [0]*(size + 1)

    def __lowBit(self, k):
        return k & -k

    def addIndex(self, index, delta):
        # Range: 0 .. size-1 -> 1 .. size.
        index += 1
        while index <= self.size:
            self.nodes[index] += delta
            index += self.__lowBit(index)

    def sum(self, index):
        # Range: 0 .. size-1 -> 1 .. size.
        index  += 1
        result = 0
        while index > 0:
            result += self.nodes[index]
            index  -= self.__lowBit(index)
        return result


tStart = datetime.datetime.now()

article    = []
vocabulary = {}
with open('INPUT.txt', encoding='utf8') as file:
    for line in file:
        for word in re.findall(r'[a-zA-Z]+', line):
            word = word.lower()
            article.append(word)
            if word not in vocabulary:
                vocabulary[word] = True

vocabulary = dict(zip(sorted(vocabulary, reverse=True), range(len(vocabulary))))
counterRev = BinaryIndexedTree(len(vocabulary))
entropy    = 0
for word in article:
    nWordRevIndex = vocabulary[word]
    entropy += counterRev.sum(nWordRevIndex - 1)
    counterRev.addIndex(nWordRevIndex, 1)

print('Entropy of this article: %d' % entropy)
with open('OUTPUT-A.txt', 'w') as file:
    file.write('%d\n' % entropy)

tEnd = datetime.datetime.now()
print(tEnd - tStart)
