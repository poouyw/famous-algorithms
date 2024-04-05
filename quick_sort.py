import random
import time
import matplotlib.pyplot as plt



def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left=[]
    middle=[]
    right=[]

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else :
            middle.append(i)
    
    return quicksort(left) + middle + quicksort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


time_merge = []
time_quick = []

values = range(2000,5000,100)
for size in values:
    array =[random.randint(1,5000) for n in range(size)]
    mergeStart=time.time()
    merge_sort(array)
    mergeEnd=time.time()
    time_merge.append((mergeEnd - mergeStart)*1000)


    quickStart=time.time()
    quicksort(array)
    quickEnd=time.time()
    time_quick.append((quickEnd - quickStart)*1000)

    
plt.plot(values, time_quick, label='quicksort', c='r', linestyle='-')
plt.plot(values, time_merge, label='mergesort', c='b' , linestyle='-')
plt.xlabel('Array Size')
plt.ylabel('Time(ms)')
plt.legend()
plt.show()

