import timeit
import random

def merge_sort():
    pass

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

lst = [random.random() for _ in range(100)]

print(f'sorted for 100: {timeit.timeit(stmt= lambda: sorted(lst), number=100)}')
print(f'insertion_sort for 100: {timeit.timeit(stmt= lambda: insertion_sort(lst), number=100)}')
print(f'sorted is faster than insertion_sort in {timeit.timeit(stmt= lambda: insertion_sort(lst), number=100)/timeit.timeit(stmt= lambda: sorted(lst), number=100)} times')
print(f'merge_sort for 100: {timeit.timeit(stmt= lambda: merge_sort(lst), number=100)}')
print(f'sorted is faster than merge_sort in {timeit.timeit(stmt= lambda: merge_sort(lst), number=100)/timeit.timeit(stmt= lambda: sorted(lst), number=100)} times')


print('-------------------------------')
print(f'sorted for 10000: {timeit.timeit(stmt= lambda: sorted(lst), number=10000)}')
print(f'insertion_sort for 10000: {timeit.timeit(stmt= lambda: insertion_sort(lst), number=10000)}')
print(f'sorted is faster than insertion_sort in {timeit.timeit(stmt= lambda: insertion_sort(lst), number=10000)/timeit.timeit(stmt= lambda: sorted(lst), number=10000)} times')
print(f'merge_sort for 10000: {timeit.timeit(stmt= lambda: merge_sort(lst), number=10000)}')
print(f'sorted is faster than merge_sort in {timeit.timeit(stmt= lambda: merge_sort(lst), number=10000)/timeit.timeit(stmt= lambda: sorted(lst), number=10000)} times')

print('-------------------------------')
print(f'sorted for 1000000: {timeit.timeit(stmt= lambda: sorted(lst), number=1000000)}')
print(f'insertion_sort for 1000000: {timeit.timeit(stmt= lambda: insertion_sort(lst), number=1000000)}')
print(f'sorted is faster than insertion_sort in {timeit.timeit(stmt= lambda: insertion_sort(lst), number=1000000)/timeit.timeit(stmt= lambda: sorted(lst), number=1000000)} times')
print(f'merge_sort for 1000000: {timeit.timeit(stmt= lambda: merge_sort(lst), number=1000000)}')
print(f'sorted is faster than merge_sort in {timeit.timeit(stmt= lambda: merge_sort(lst), number=1000000)/timeit.timeit(stmt= lambda: sorted(lst), number=1000000)} times')

print('-------------------------------')
lst2 = [random.random() for _ in range(10)]
print(f'sorted for 10000: {timeit.timeit(stmt= lambda: sorted(lst2), number=10000)}')
print(f'insertion_sort for 10000: {timeit.timeit(stmt= lambda: insertion_sort(lst2), number=10000)}')
print(f'sorted is faster than insertion_sort in {timeit.timeit(stmt= lambda: insertion_sort(lst2), number=10000)/timeit.timeit(stmt= lambda: sorted(lst2), number=10000)} times')
print(f'merge_sort for 10000: {timeit.timeit(stmt= lambda: merge_sort(lst2), number=10000)}')
print(f'sorted is faster than merge_sort in {timeit.timeit(stmt= lambda: merge_sort(lst2), number=10000)/timeit.timeit(stmt= lambda: sorted(lst2), number=10000)} times')

print('-------------------------------')
lst3 = [random.random() for _ in range(1000)]
print(f'sorted for 10000: {timeit.timeit(stmt= lambda: sorted(lst3), number=10000)}')
print(f'insertion_sort for 10000: {timeit.timeit(stmt= lambda: insertion_sort(lst3), number=10000)}')
print(f'sorted is faster than insertion_sort in {timeit.timeit(stmt= lambda: insertion_sort(lst3), number=10000)/timeit.timeit(stmt= lambda: sorted(lst3), number=10000)} times')
print(f'merge_sort for 10000: {timeit.timeit(stmt= lambda: merge_sort(lst3), number=10000)}')
print(f'sorted is faster than merge_sort in {timeit.timeit(stmt= lambda: merge_sort(lst3), number=10000)/timeit.timeit(stmt= lambda: sorted(lst3), number=10000)} times')
