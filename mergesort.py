import random
list = random.sample(range(1,60),10)
def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left_half = list[:mid]
    right_half = list[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

print("Sebelum Diurutkan: ", list)
sorted_lst = merge_sort(list)
print("Setelah Diurutkan: ", sorted_lst)
