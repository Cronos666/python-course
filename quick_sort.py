def quicksort(tab, low, high):
    mid = tab[int((low+high)/2)]
    l = low
    h = high
    while True:
        while tab[l]<mid:
            l += 1
        while tab[h]>mid:
            h -= 1
        if l <= h:
            buffor = tab[l]
            tab[l] = tab[h]
            tab[h] = buffor
            l += 1
            h -= 1
        if h > low:
            quicksort(tab, low, h)
        if l < high:
            quicksort(tab, l, high)
        if l >= h:
            break
#testing algorithm:
"""
array = []
import random
for i in range(1000):
    array.append(random.randint(0, 1000))

quicksort(array, 0, 999)

print(array)
"""