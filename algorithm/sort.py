#! /usr/bin/python
# -*- coding: utf-8 -*-

def _range_check(arr, low, high):
    if low > high:
        raise OverflowError('low(%s) > high(%s)' % (low, high))
    if low < 0:
        raise OverflowError(low)
    if high > (len(arr) - 1):
        raise OverflowError(high)


def quick_sort(arr, low, high):

    _range_check(arr, low, high)

    if low < high:
        i = low
        j = high
        temp = arr[low]

        while i < j:

            while i < j and arr[j] >= temp:
                j = j - 1
            if i < j:
                arr[i] = arr[j]
                i = i + 1

            while i < j and arr[i] < temp:
                i = i + 1
            if i < j:
                arr[j] = arr[i]
                j = j - 1

        arr[i] = temp
        quick_sort(arr, low, i - 1)
        quick_sort(arr, i + 1, high)


if __name__ == '__main__':
    arr = [23, 2, 234, 12, 3] # 1 --> [3,2,234,12,] 2--> [3,2,,12,234] 3 --> [3,2,23,12,243] 4 --> quick_sort[3,2] quick_sort[12,243]
    quick_sort(arr, 0, len(arr) - 1)
    print list(arr)


