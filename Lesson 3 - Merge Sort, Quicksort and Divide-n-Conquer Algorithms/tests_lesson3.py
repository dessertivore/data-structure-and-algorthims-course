import random
import pytest
from lesson3_sorting import merge_sort
from lesson3_mainproblem import Notebook, quicksort_nbs, compare_likes
from lesson3_assignment import poly_product


tests = []
longlist = list(range(10000))
random.shuffle(longlist)

tests.append(
    {"input": [4, 2, 6, 3, 4, 6, 2, 1], "output": [1, 2, 2, 3, 4, 4, 6, 6]}
)  # unsorted list
tests.append({"input": [4], "output": [4]})  # only 1 integer
tests.append({"input": [], "output": []})  # empty list
tests.append({"input": [1, 2, 3, 4, 5], "output": [1, 2, 3, 4, 5]})  # already sorted
tests.append(
    {"input": [1, 1, 1, 1], "output": [1, 1, 1, 1]}
)  # same integer multiple times
tests.append({"input": longlist, "output": list(range(10000))})  # long list


@pytest.mark.parametrize("input_data", tests)
def test_sort(input_data) -> None:
    nums = input_data["input"]
    expected_output = input_data["output"]
    assert merge_sort(nums) == expected_output


test_notebooks = []
chrisp = Notebook("strange-new-worlds", "chrisp", 373)
kathrynj = Notebook("voyager", "kathrynj", 532)
jimk = Notebook("original-series", "jimk", 31)
jeanlucp = Notebook("next-gen", "jeanlucp", 94)
captainarcher = Notebook("enterprise", "captainarcher", 2)
dessertivore = Notebook("clinical-dietetics-manual", "dessertivore", 29)

test_notebooks.append(
    [
        [chrisp, kathrynj, jimk, jeanlucp, captainarcher, dessertivore],
        [kathrynj, chrisp, jeanlucp, jimk, dessertivore, captainarcher],
    ]
)  # unsorted list

test_notebooks.append([[chrisp], [chrisp]])  # 1 item in list

test_notebooks.append([[chrisp, chrisp, chrisp], [chrisp, chrisp, chrisp]])
# repeated same item

test_notebooks.append([[], []])  # empty list


@pytest.mark.parametrize("input_data", test_notebooks)
def test_sort_notebooks(input_data) -> None:
    input, expected_output = input_data[0], input_data[1]
    assert quicksort_nbs(input) == expected_output


tests_assignment: list = []
tests_assignment.append(
    {
        "input": {"poly1": [2, 0, 5, 7], "poly2": [3, 4, 2]},
        "output": [6, 8, 19, 41, 38, 14],
    }
)

tests_assignment.append(
    {
        "input": {"poly1": [0, 0, 0], "poly2": [0, 0, 0]},
        "output": [],
    }
)

tests_assignment.append(
    {
        "input": {"poly1": [1, 1, 1], "poly2": [1, 1, 1]},
        "output": [1, 2, 3, 2, 1],
    }
)

tests_assignment.append(
    {
        "input": {"poly1": [1, 2, 3, 4], "poly2": [1, 2]},
        "output": [1, 4, 7, 10, 8],
    }
)


@pytest.mark.parametrize("input_data", tests_assignment)
def test_assignment3(input_data) -> None:
    input1, input2 = input_data["input"]["poly1"], input_data["input"]["poly2"]
    expected_output = input_data["output"]
    assert poly_product(input1, input2) == expected_output
