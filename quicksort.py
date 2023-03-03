import random
list = random.sample(range(1,60),10)

def quicksort(list):
    if len(list) <= 1:
        return list
    pivot = list[random.randint(0, len(list)-1)]
    left = []
    right = []
    equal = []
    for i in list:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)
    return quicksort(left) + equal + quicksort(right)
print("Sebelum Diurutkan :", list)
print("Setelah Diurutkan :", quicksort(list))



