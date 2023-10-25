"""
Write a function to sort a list in ascending order
"""


def sort_asc(inputlist: list) -> list:
    # create new variable so we aren't messing with the input list
    sortedlist = list(inputlist)
    # repeat process x-1 times
    for x in range(len(sortedlist) - 1):
        # iterate through entire array, except last element
        for i in range(len(sortedlist) - 1):
            # if value is greater than value next to it, they swap places
            if sortedlist[i] > sortedlist[i + 1]:
                sortedlist[i], sortedlist[i + 1] = sortedlist[i + 1], sortedlist[i]
    return sortedlist


""" 
Time complexity is On^2 (2 loops of n-1 length, therefore n^2 is highest power), 
space complexity is O(n) (no extra variables stored)
"""


"""
Insertion sort code from tutor:
keep the initial portion of the array sorted and insert the remaining elements one by one at the right position.
"""


def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)  # remove current element from list
        j = i - 1  # Initialize the index for comparing with previous elements
        while (
            j >= 0 and nums[j] > cur
        ):  # Move backwards through the sorted portion of the list until we reach a number greater than current
            j -= 1
        nums.insert(j + 1, cur)  # Insert the current element into its correct position
    return nums


"""
while both insertion sort and bubble sort have a worst-case time complexity of O(n^2), 
insertion sort tends to be more efficient than bubble sort in practice due to its better performance 
in nearly sorted or partially sorted lists.
"""

"""
Divide and Conquer = Merge sort has the following general steps:

Divide the inputs into two roughly equal parts.
Recursively solve the problem individually for each of the two parts.
Combine the results to solve the problem for the original inputs.
Include terminating conditions for small or indivisible inputs.
"""


def merge_sort(inputlist: list):
    if len(inputlist) <= 1 or inputlist is None:
        return inputlist
    mid = len(inputlist) // 2
    left = merge_sort(inputlist[0:mid])
    right = merge_sort(inputlist[mid : (len(inputlist))])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    # go through both halves of the list
    while i < len(left) and j < len(right):
        # find which one is smaller, and put it in the result list first
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # get the remaining parts of list
    result.extend(left[i:])
    result.extend(right[j:])

    return result


"""
Counting from the top and starting from 0, the kth level of the above tree involves 
2^k invocations of merge with sublists of size roughly n/2^k, where 
n is the size of the original input list. Therefore the total number of comparisons at 
each level of the tree is 2^k x n/2^k = n

Thus, if the height of the tree is h, the total number of comparisons is n*h. Since 
there are n sublists of size 1 at the lowest level, it follows that 2^(h-1)=n ie. 
h = log(n+1). Thus the time complexity of the merge sort algorithms is O(nlogn).

Since the original sublists can be discarded after the merge operation, 
the additional space can be freed or reused for future merge calls. Thus, merge sort requires 
O(n) additional space i.e. the space complexity is O(n)
"""


"""
Another divide and conquer: quicksort - code from tutor
"""


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


# worst case time complexity is O(n^2),
# although in practice it's usually closer to O(nlogn)
