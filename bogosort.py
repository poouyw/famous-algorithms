import random

def fisher_yates_shuffle(lst):
    n = len(lst)
    
    for i in range(n-1, 0, -1):
        
        j = random.randint(0, i)


        lst[i], lst[j] = lst[j], lst[i]


    return lst[:n]


def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def bogo_sort(lst):
    while is_sorted(lst) == False:
        lst = fisher_yates_shuffle(lst)
    return (print(lst))

my_list = [7,4,90,45,200,341,312312]

bogo_sort(my_list)

