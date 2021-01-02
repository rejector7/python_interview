"""
select sort, insert sort, bubble sort, merge sort, quick sort, shell sort, heap sort, radix sort(bucket sort)
"""
import random
import numpy as np
import math


# select sort
def select_sort(lists):
    length = len(lists)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if lists[j] < lists[min_index]:
                min_index = j
            else:
                continue
        lists[i], lists[min_index] = lists[min_index], lists[i]
    return lists


# insert sort
def insert_sort(lists):
    length = len(lists)
    for i in range(1, length):
        to_insert = lists[i]
        for j in range(i - 1, -1, -1):
            if to_insert < lists[j]:
                lists[j], lists[j + 1] = to_insert, lists[j]
            else:
                break
    return lists


# bubble sort
def bubble_sort(lists):
    length = len(lists)
    for _ in range(length):
        for i in range(length - 1):
            if lists[i] > lists[i + 1]:
                lists[i], lists[i + 1] = lists[i + 1], lists[i]
            else:
                continue
    return lists


# merge sort
def merge(left_list, right_list):
    i, j = 0, 0
    merged_list = []
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            merged_list.append(left_list[i])
            i += 1
        else:
            merged_list.append(right_list[j])
            j += 1
    if i < len(left_list):
        for k in range(i, len(left_list)):
            merged_list.append(left_list[k])
    if j < len(right_list):
        for k in range(j, len(right_list)):
            merged_list.append(right_list[k])
    return merged_list


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    left_list = merge_sort(lists[0: len(lists) // 2])
    right_list = merge_sort(lists[len(lists) // 2:])
    merged_list = merge(left_list, right_list)
    return merged_list


# quick sort
def quick_sort(lists, low, high):
    if low >= high:
        return
    key = lists[low]
    i = low
    j = high
    while i < j:
        while i < j and lists[j] > key:
            j -= 1
        lists[i] = lists[j]
        while i < j and lists[i] <= key:
            i += 1
        lists[j] = lists[i]
    lists[i] = key
    quick_sort(lists, low, i - 1)
    quick_sort(lists, i + 1, high)
    return lists


# shell sort
def shell_sort(lists):
    step = 2
    length = len(lists)
    group = length // step
    while group > 0:
        for i in range(group):
            j = i + group
            while j < length:
                for k in range(j, i, -group):
                    if lists[k] >= lists[k - group]:
                        continue
                    else:
                        lists[k], lists[k - group] = lists[k - group], lists[k]
                j += group
        group = group // step
    return lists


def build_heap(lists):
    size = len(lists)
    for i in range(size//2, -1, -1):
        adjust_heap(lists, size, i)
    return lists


# adjust the adjust_start item to its suitable place
def adjust_heap(lists, size, adjust_start):
    i = adjust_start
    while 2 * i + 1 < size:
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        larger_child = left_child
        if right_child < size and lists[right_child] > lists[left_child]:
            larger_child = right_child
        if lists[i] < lists[larger_child]:
            lists[i], lists[larger_child] = lists[larger_child], lists[i]
            i = larger_child
        else:
            break
    return lists


def heap_sort(lists):
    lists = build_heap(lists)
    for i in range(len(lists) - 1, 0, -1):
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, i, 0)
    return lists


# radix sort
def radix_sort(lists, radix):
    max_item = max(lists)
    k = int(math.floor(math.log(max_item, radix)) + 1)
    # print(k)
    for i in range(k):
        buckets = [[] for i in range(radix)]
        for num in lists:
            buckets[(num//(radix ** i)) % radix].append(num)
        print(buckets)
        lists = []
        # print(lists)
        # j = 0
        for bucket in buckets:
            for num in bucket:
                lists.append(num)
        # print(lists)
    return lists


if __name__ == "__main__":
    test_list = np.random.randint(0, 100, 10)
    print(test_list)
    print(radix_sort(test_list, 10))



