import datetime
import re


def mergeSort(array, L, R):     # Divide.
    if L < R:
        M = (L + R) // 2
        mergeSort(array, L, M)
        mergeSort(array, M+1, R)
        merge(array, L, R)

def merge(array, L, R):         # Conquer.
    global entropy
    M = (L + R) // 2

    # Left side:  array[L : M+1].
    # Right side: array[M+1 : R+1].
    L_idx = L
    R_idx = M + 1
    k     = L
    while L_idx <= M and R_idx <= R:
        if array[L_idx] <= array[R_idx]:
            tmp[k] = array[L_idx]
            k      += 1
            L_idx  += 1
        else:
            entropy += M - L_idx + 1    # Moving an element in the right side
                                        # which is *greater than* the remaining elements in the left side (array[L : M+1])
                                        # increases entropy.
            tmp[k]  = array[R_idx]
            k       += 1
            R_idx   += 1

    # One side reaches its right bound, but another side doesn't yet.
    while L_idx <= M:
        tmp[k] = array[L_idx]
        k += 1
        L_idx += 1
    while R_idx <= R:
        tmp[k] = array[R_idx]
        k += 1
        R_idx += 1

    for i in range(L, R + 1):
        array[i] = tmp[i]


tStart = datetime.datetime.now()

article = []
with open('INPUT.txt', encoding='utf8') as file:
    for line in file:
       for word in re.findall(r'[a-zA-z]+', line):
           word = word.lower()
           article.append(word)

entropy = 0
tmp     = [0]*(len(article) + 1)
mergeSort(article, 0, len(article) - 1)     # Calculate entropy during merge sort working.

print('Entropy of this article: %d' % entropy)

tEnd = datetime.datetime.now()
print(tEnd - tStart)
