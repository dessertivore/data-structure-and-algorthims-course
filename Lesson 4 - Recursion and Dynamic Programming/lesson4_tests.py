from lesson4 import lcs_recursive, lcs_mem, optimise_rating, knapsack_dp, lcs_dp
import pytest

tests = []
# General case (string)
tests.append(
    {
        "input": {"seq1": "serendipitous", "seq2": "precipitation"},
        "output": 7,
    }
)
# General case (list)
tests.append(
    {
        "input": {
            "seq1": [1, 3, 5, 6, 7, 2, 5, 2, 3],
            "seq2": [6, 2, 4, 7, 1, 5, 6, 2, 3],
        },
        "output": 5,
    }
)

# No common subsequence
tests.append(
    {
        "input": {
            "seq1": "asdfwevad",
            "seq2": "opkpoiklklj",
        },
        "output": 0,
    }
)
# One is a subsequence of the other
tests.append(
    {
        "input": {
            "seq1": "dense",
            "seq2": "condensed",
        },
        "output": 5,
    }
)
# One sequence is empty
tests.append(
    {
        "input": {
            "seq1": "",
            "seq2": "sdfgjlkrt",
        },
        "output": 0,
    }
)
# Both sequences are empty
tests.append(
    {
        "input": {
            "seq1": "",
            "seq2": "",
        },
        "output": 0,
    }
)
# Multiple subsequences with same length
tests.append(
    {
        "input": {
            "seq1": "condensecondense",
            "seq2": "denserdenser",
        },
        "output": 10,
    }
)
# “abcdef” and “badcfe”
tests.append(
    {
        "input": {
            "seq1": "abcdef",
            "seq2": "badcfe",
        },
        "output": 3,
    }
)


# @pytest.mark.parametrize("input_data", tests)
# def test_lesson4(input_data) -> None:
#     input1, input2 = input_data["input"]["seq1"], input_data["input"]["seq2"]
#     expected_output = input_data["output"]
#     assert lcs_recursive(input1, input2) == expected_output


@pytest.mark.parametrize("input_data", tests)
def test_lesson4(input_data) -> None:
    input1, input2 = input_data["input"]["seq1"], input_data["input"]["seq2"]
    expected_output = input_data["output"]
    assert lcs_mem(input1, input2) == expected_output


@pytest.mark.parametrize("input_data", tests)
def test_lesson4_lcsdp(input_data) -> None:
    input1, input2 = input_data["input"]["seq1"], input_data["input"]["seq2"]
    expected_output = input_data["output"]
    assert lcs_dp(input1, input2) == expected_output


test_knapsack = []

test_knapsack.append(
    {
        "input": {
            "capacity": 165,
            "weights": [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
            "profits": [92, 57, 49, 68, 60, 43, 67, 84, 87, 72],
        },
        "output": 309,
    }
)

test_knapsack.append(
    {
        "input": {"capacity": 3, "weights": [4, 5, 6], "profits": [1, 2, 3]},
        "output": 0,
    }
)

test_knapsack.append(
    {
        "input": {"capacity": 4, "weights": [4, 5, 1], "profits": [1, 2, 3]},
        "output": 3,
    }
)
test_knapsack.append(
    {
        "input": {
            "capacity": 170,
            "weights": [41, 50, 49, 59, 55, 57, 60],
            "profits": [442, 525, 511, 593, 546, 564, 617],
        },
        "output": 1735,
    }
)

test_knapsack.append(
    {
        "input": {"capacity": 15, "weights": [4, 5, 6], "profits": [1, 2, 3]},
        "output": 6,
    }
)

test_knapsack.append(
    {
        "input": {
            "capacity": 15,
            "weights": [4, 5, 1, 3, 2, 5],
            "profits": [2, 3, 1, 5, 4, 7],
        },
        "output": 19,
    }
)


@pytest.mark.parametrize("input_data", test_knapsack)
def test_team_opt(input_data) -> None:
    input1, input2, input3 = (
        input_data["input"]["weights"],
        input_data["input"]["profits"],
        input_data["input"]["capacity"],
    )
    expected_output = input_data["output"]
    assert optimise_rating(input1, input2, input3) == expected_output


@pytest.mark.parametrize("input_data", test_knapsack)
def test_team_opt_dp(input_data) -> None:
    input1, input2, input3 = (
        input_data["input"]["capacity"],
        input_data["input"]["weights"],
        input_data["input"]["profits"],
    )
    expected_output = input_data["output"]
    assert knapsack_dp(input1, input2, input3) == expected_output
