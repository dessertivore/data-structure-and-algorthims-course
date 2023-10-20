from lesson1 import locate_card, count_rot_linear, count_rotations
import pytest

# query is the first element
testdata1 ={
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
}

# print(locate_card(testdata1['input']['cards'], testdata1['input']['query']))

def test_1() -> None:
    assert locate_card(testdata1['input']['cards'], testdata1['input']['query']) == 0


# below are tests suggested by course

# store tests as list
tests = []

# query occurs in the middle
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})
# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})
# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})
# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

# cards does not contain query, assuming then that -1 is expected output
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})
# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})



# rotated list tests

testsrotate=[]

# rotated once
testsrotate.append({
    'input': {
        'cards': [5, 1, 2, 3, 4],
    },
    'output': 1
})

# A list that wasn't rotated at all.
testsrotate.append({
    'input': {
        'cards': [1, 2, 3, 4, 5, 6, 7, 8],
    },
    'output': 0
})

# A list that was rotated n-1 times, where n is the size of the list
testsrotate.append({
    'input': {
        'cards': [2, 3, 4, 5, 6, 7, 8, 1],
    },
    'output': 7 
})

# A list containing just one element.
testsrotate.append({
    'input': {
        'cards': [1],
    },
    'output': 0
})

# tests for problem 1
@pytest.mark.parametrize("input_data", tests)
def test_locate_card(input_data)-> None:
    cards = input_data['input']['cards']
    query = input_data['input']['query']
    expected_output = input_data['output']
    assert locate_card(cards, query) == expected_output

# tests for rotated list
@pytest.mark.parametrize("input_data", testsrotate)
def test_rotate_card(input_data)-> None:
    nums = input_data['input']['cards']
    expected_output = input_data['output']
    assert count_rot_linear(nums) == expected_output

@pytest.mark.parametrize("input_data", testsrotate)
def test_binary_rotate(input_data)-> None:
    nums = input_data['input']['cards']
    expected_output = input_data['output']
    assert count_rotations(nums) == expected_output