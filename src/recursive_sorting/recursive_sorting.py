# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # position in arrA
    a = 0
    # postition in arrB
    b = 0

    for k in range(0, elements):
        # if pos in arrA is out of the bounds of arrA, set the current 
        # position in merged_arr to arrB[b] and increment pos in arrB
        if a >= len(arrA):
            merged_arr[k] = arrB[b]
            b += 1
        # if pos in arrB is out of the bounds of arrB, set the current 
        # position in merged_arr to arrA[a] and increment pos in arrA
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a += 1
        # if the current value of arrA is less than that of arrB, set the current 
        # position in merged_arr to arrA[a] and increment pos in arrA
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1
        # if the current value of arrA is greater than that of arrB, set the current 
        # position in merged_arr to arrB[b] and increment pos in arrB
        elif arrA[a] > arrB[b]:
            merged_arr[k] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # if the array has more than 1 item, split it in half
    if len(arr) > 1:
        left = merge_sort(arr[0:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])

        arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):

    return arr


def merge_sort_in_place(arr, l, r):

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
