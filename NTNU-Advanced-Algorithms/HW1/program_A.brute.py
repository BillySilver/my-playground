import datetime
import re


tStart = datetime.datetime.now()

article = []
with open('INPUT.txt', encoding='utf8') as file:
    for line in file:
        for word in re.findall(r'[a-zA-Z]+', line):
            word = word.lower()
            article.append(word)

entropy = 0
for i in range(len(article)):
    for j in range(i+1, len(article)):
        if ( article[i] > article[j] ):
            entropy += 1

print('Entropy of this article: %d' % entropy)

tEnd = datetime.datetime.now()
print(tEnd - tStart)


# Entropy of this article: 350243600
# 0:03:44.081962
