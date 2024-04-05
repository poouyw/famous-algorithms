import random
import time
import matplotlib.pyplot as plt
#----------------------------------------------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # be 2 gesmat tagsim mikonim araye ra
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # be joda krdn edame midim
    left = merge_sort(left)
    right = merge_sort(right)

    # ezafe krdn be list result bar asas kochik va bozorgi
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # ezafe krdn onsor haye bagi mande
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
#--------------------------------------------------------------------------------------
def k_select_random(arr, k):
    if len(arr) != 0:
        pivot = random.choice(arr)
        lower=[]
        higher=[]
        pivot_counter = 0
    
        for i in arr:
            if i < pivot:
                lower.append(i)
            elif i > pivot:
                higher.append(i)
            else :
                pivot_counter += 1
                
        if k < len(lower):
            sorted_lower = merge_sort(lower)
            return(sorted_lower[k])
        elif k < len(lower) + pivot_counter:
            return pivot
        else:
            sorted_higher = merge_sort(higher)
            return(sorted_higher[k - len(lower) - pivot_counter])
#----------------------------------------------------------------------------
def k_select_random_r(arr, k):
    if len(arr) != 0:
        pivot = random.choice(arr)
        lower=[]
        higher=[]
        pivot_counter = 0
    
        for i in arr:
            if i < pivot:
                lower.append(i)
            elif i > pivot:
                higher.append(i)
            else :
                pivot_counter += 1
                
        if k < len(lower):
            return k_select_random_r(lower, k)
        elif k < len(lower) + pivot_counter:
            return pivot
        else:
            return k_select_random_r(higher, k - len(lower) - pivot_counter)


#---median------------------------------------------------------------------------
def median_of_medians(arr):
    groups = []    
    
    medians = []
    
    for i in range(0, len(arr), 5):
        group = arr[i:i+5]
        groups.append(group)
        
    for group in groups:
        medians.append(sorted(group)[len(group) // 2])

    if len(medians) <= 5:
        return sorted(medians)[len(medians) // 2]
    else:
        k = len(medians)//2
        #return median_of_medians(medians)
        return k_select_random_r(medians, k)
        #return k_select_median_k(medians, k)
#---------------------------------------------------------------------------------
def k_select_median(arr, k):
    if len(arr) != 0:
        pivot = median_of_medians(arr)
        lower=[]
        higher=[]
        pivot_counter = 0
    
        for i in arr:
            if i < pivot:
                lower.append(i)
            elif i > pivot:
                higher.append(i)
            else :
                pivot_counter += 1
                
        if k < len(lower):
            sorted_lower = merge_sort(lower)
            return(sorted_lower[k])
        elif k < len(lower) + pivot_counter:
            return pivot
        else:
            sorted_higher = merge_sort(higher)
            return(sorted_higher[k - len(lower) - pivot_counter]) 
#---------------------------------------------- joda kardan 100 tai vas ejra



def k_select_median_k(arr, k):
    if len(arr) != 0:
        pivot = median_of_medians(arr)
        lower=[]
        higher=[]
        pivot_counter = 0
    
        for i in arr:
            if i < pivot:
                lower.append(i)
            elif i > pivot:
                higher.append(i)
            else :
                pivot_counter += 1
                
        if k < len(lower):
            return k_select_median_k(lower, k)
        elif k < len(lower) + pivot_counter:
            return pivot
        else:
            return k_select_median_k(higher, k - len(lower) - pivot_counter)



#---------------------------------------------
time_median = []
time_random = []
time_k=[]
time_r=[]
values = range(2000,5000,100)
for size in values:
    array =[random.randint(1,5000) for n in range(size)]
    k = random.randint(1,size)
    randomStart=time.time()
    k_select_random(array, k)
    randomEnd=time.time()
    time_random.append((randomEnd - randomStart)*1000)


    medianStart=time.time()
    k_select_median(array, k)
    medianEnd=time.time()
    time_median.append((medianEnd - medianStart)*1000)


    kStart=time.time()
    k_select_median_k(array, k)
    kEnd=time.time()
    time_k.append((kEnd - kStart)*1000)
    
    
    rStart=time.time()
    k_select_random_r(array, k)
    rEnd=time.time()
    time_r.append((rEnd - rStart)*1000)
    
plt.plot(values, time_random, label='k_select_random', c='r', linestyle='-')
plt.plot(values, time_median, label='k_select_median', c='b' , linestyle='-')
plt.plot(values, time_k, label='k_select_k', c='g' , linestyle='-')
plt.plot(values, time_r, label='k_select_r', c='y' , linestyle='-')
plt.xlabel('Array Size')
plt.ylabel('Time(ms)')
plt.legend()
plt.show()





