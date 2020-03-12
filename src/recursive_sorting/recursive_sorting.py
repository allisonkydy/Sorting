
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # initialize array indexes
    i_A = 0
    i_B = 0

    # for the length of the merged array
    for i in range(elements):
        # if an index lies beyond the bounds of the array,
        # we've reached the end, so add element from the other array
        if len(arrA) <= i_A:
            # add element to the merged array and shift index
            merged_arr[i] = arrB[i_B]
            i_B += 1
        elif len(arrB) <= i_B:
            merged_arr[i] = arrA[i_A]
            i_A += 1
        # compare the two smallest unmerged values
        elif arrB[i_B] < arrA[i_A]:
            # if the right is smaller
            merged_arr[i] = arrB[i_B]
            i_B += 1
        else:
            # if the left is smaller than or equal to right
            merged_arr[i] = arrA[i_A]
            i_A += 1
    
    return merged_arr


def merge_sort( arr ):
    # if array contains one element, it is sorted
    if len(arr) <= 1:
        return arr
    # if array contains more than one element, split in half and 
    # sort each half, then merge together
    else:
        mid = len(arr) // 2
        arr_left = arr[:mid]
        arr_right = arr[mid:]
        return merge(merge_sort(arr_left), merge_sort(arr_right))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    r_start = mid + 1
    # if start == mid or r_start == end,
    # return after next comparison
    while start <= mid and r_start <= end:
        # compare left start to right start
        # if left is smaller than or equal to right, leave in place and move start 
        if arr[start] <= arr[r_start]:
            start += 1
        # if right is smaller, store in temp and move everthing over by one, 
        # then put temp at start and move pointers
        elif arr[start] > arr[r_start]:
            # arr[start:r_start + 1] = [arr[r_start], *arr[start:r_start]]
            temp = arr[r_start]
            for i in range(r_start, start, -1):
                arr[i] = arr[i - 1]
            arr[start] = temp

            r_start += 1
            mid += 1
            start += 1

    return arr


def merge_sort_in_place(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort_in_place(arr, l, mid)
        merge_sort_in_place(arr, mid + 1, r)
        return merge_in_place(arr, l, mid, r)
    else:
        return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
