import datetime
import re


tStart = datetime.datetime.now()

counters = {}
with open('INPUT.txt', encoding='utf8') as file:
    for line in file:
        for word in re.findall(r'[a-zA-Z]+', line):
            word = word.lower()
            if word not in counters:
                counters[word] = 0
            counters[word] += 1

with open('OUTPUT-B.txt', 'w') as file:
    nNow = 40000
    for key, value in sorted(counters.items(), key=lambda kv: (-kv[1], kv[0])):
        if value < nNow:
            if 40000 != nNow:
                file.write('\n')
            nNow = value
            file.write(str(value) + ':')
        file.write(' ' + key)

tEnd = datetime.datetime.now()
print(tEnd - tStart)
