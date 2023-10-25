##QUESTION 1: Alice has some list with numbers written on them.
##She arranges the list in decreasing order, and lays them out face down in a sequence on a table.
##She challenges Bob to pick out the card containing a given number by turning over as few list as possible.
##Write a function to help Bob locate the card.


# go through the list 1 by 1
def locate_card_linear(list: list, query: int):
    output = -1
    for index, card in enumerate(list):
        if card == query:
            output = index
            break
    print(output)
    return output


# go to middle card, then go left or right depending on number
# find index of query so that the first instance of this card is reported


def locate_card_no_condition(list: list, query: int):
    lo, hi = 0, len(list) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = list[mid]

        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)

        if mid_number == query:
            return list.index(query)
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1

    return -1


# attempt to allow user to input data
# listtest = input("list").split
# querytest = int(input("query"))
# locate_card(listtest, querytest)


# example of binary function with condition
# condition must have same argument name as in binary_search
def binary_search(lo, hi, condition):
    while lo <= hi:
        # find middle number
        mid = (lo + hi) // 2
        # compare middle card to query
        result = condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def locate_card(list, query):
    def condition(mid):
        if list[mid] == query:
            # check there is no previous occurrence of query card
            if mid > 0 and list[mid - 1] == query:
                return "left"
            else:
                return "found"
        elif list[mid] < query:
            return "left"
        else:
            return "right"

    return binary_search(0, len(list) - 1, condition)


# time complexity of binary function is O(log n) - where log is base 2 (because with
# every iteration, list is halved)
# time complexity of a linear search is  O(N)


# Question2: Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given number.


def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return "left"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"

    return binary_search(0, len(nums) - 1, condition)


def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid + 1] == target:
                return "right"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"

    return binary_search(0, len(nums) - 1, condition)


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)


# question3 You are given list of numbers,
# obtained by rotating a sorted list an unknown number of times.
# Write a function to determine the minimum number of times the original
# sorted list was rotated to obtain the given list. Your function
# should have the worst-case complexity of O(log N), where N is the length
# of the list. You can assume that all the numbers in the list are unique.

# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by
# rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
# We define "rotating a list" as removing the last element of
# the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].
# "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].


# linear method
def count_rot_linear(nums):
    output = 0
    for index, number in enumerate(nums):
        # output 0 if list is <=1 number long, or if function reaches end of list without finding rotate
        if len(nums) <= 1 or index == len(nums) - 1:
            break
        # breaks if value found is greater than next value in list (indicates wrong order of list)
        elif number > nums[index + 1]:
            output = index + 1
            break
    return output


# do this with a binary search-
# if the middle element of the list is smaller than the last element of the range,
# then the answer lies to the left of it. Otherwise, the answer lies to the right.


def count_rotations(array):
    if len(array) <= 1:  # if only 0 or 1 elements, turning point is 0
        return 0
    lo, hi = 0, len(array) - 1
    while lo < hi:
        # find middle number
        mid = (lo + hi) // 2
        # check if this is turn point
        if array[mid] > array[mid + 1]:
            print((mid) + 1)
            return (mid) + 1
        # if index is not 0, and array[index] is smaller than final number on list
        elif mid > 0 and array[mid] < array[len(array) - 1]:
            # highest number becomes index -1 (i.e. go left)
            hi = mid - 1
        # go right if number at [mid] is bigger than first number on list
        elif array[mid] > array[0] and mid < len(array):
            lo = mid + 1
    return 0


# def locate_turnpoint(array: list):
#     if len(array) <= 1: # if only 0 or 1 elements, turning point is 0
#         return 0
#     def condition(mid: int):
#         if mid > 0 and array[mid] < array[len(array)]:
#             return 'left'
#         elif array[mid] > array[0] and mid < len(array):
#             return 'right'
#         elif array[mid] > array[mid+1]:
#             return 'found'
#     return count_rotations(0, len(array) - 1, condition)
