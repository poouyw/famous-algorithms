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

n = input()


arr = list(map(int, n.split()))

sorted_arr = merge_sort(arr)


output_string = " ".join(map(str, sorted_arr))

print(output_string)


