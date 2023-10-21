# import pytest
# from lesson2 import tree_to_tuple, parse_tuple

# teststree = []

# teststree.append({
#     'input': tree_to_tuple((1,3,None),2,((None,3,4),5,(6,7,8)))
#         ,
#     'output': ((1,3,None),2,((None,3,4),5,(6,7,8)))
#     }
# )


# teststree.append({
#     'input': tree_to_tuple(((2, 4, 5), 1, (3, 6, 7)))
#     ,
#     'output': ((2, 4, 5), 1, (3, 6, 7))
#     }
# )


# @pytest.mark.parametrize("input_data", teststree)
# def test_trees(input_data)-> None:
#     input_data = input_data['input']
#     expected_output = input_data['output']
#     assert tree_to_tuple(input_data) == expected_output
