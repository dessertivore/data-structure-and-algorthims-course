import random
import pytest
from lesson3_sorting import merge_sort


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
