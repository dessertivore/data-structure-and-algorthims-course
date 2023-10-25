import random
import pytest
from lesson3_sorting import merge_sort
from lesson3_mainproblem import Notebook, quicksort_nbs, compare_likes

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
