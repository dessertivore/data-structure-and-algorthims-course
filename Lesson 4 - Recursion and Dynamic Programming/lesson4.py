"""
QUESTION 1: Write a function to find the length of the longest common subsequence 
between two sequences. E.g. Given the strings "serendipitous" and "precipitation", the 
longest common subsequence is "reipito" and its length is 7.

A "sequence" is a group of items with a deterministic ordering. Lists, tuples and 
ranges are some common sequence types in Python.

A "subsequence" is a sequence obtained by deleting zero or more elements from another 
sequence. For example, "edpt" is a subsequence of "serendipitous".
"""

# code from tutor


def lcs_recursive(seq1, seq2, idx1=0, idx2=0) -> int:
    # when you reach end of list, return 0
    if idx1 >= len(seq1) or idx2 >= len(seq2):
        return 0
    # if there is a match, add 1 to counter
    elif seq1[idx1] == seq2[idx2]:
        return 1 + (lcs_recursive(seq1, seq2, idx1 + 1, idx2 + 1))
    # if not a match, increment through rest of seq1 or seq2, and check for matches there
    else:
        option1 = lcs_recursive(seq1, seq2, idx1 + 1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2 + 1)
        return max(option1, option2)


"""
Number of subtrees is 2(m+n), where left and right subtrees have m and n internal nodes
respectively, and each subtree has 2 subtrees.
Time complexity of going through all the subtrees in a binary tree recursively is 
O(2^(m+n)). This is because at each node, the algorithm makes 2 recursive calls. These
2 recursive calls are made for every internal node.
"""


"""
Improve time complexity with memoization.
"""


def lcs_mem(seq1, seq2):
    memo = {}

    def recurse(idx1=0, idx2=0):
        key = (idx1, idx2)

        if idx1 >= len(seq1) or idx2 >= len(seq2):
            memo[key] = 0
        # if key already has value saved, access this instead of recalculating
        if key in memo:
            return memo[key]
            # if there is a match, add 1 to counter
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + (recurse(idx1 + 1, idx2 + 1))
        # if not a match, increment through rest of seq1 or seq2, and check for matches there
        else:
            memo[key] = max(recurse(idx1 + 1, idx2), recurse(idx1, idx2 + 1))
        return memo[key]

    # recurse (0,0) as this will go through whole string
    return recurse(0, 0)


"""
Time complexity with memoization (dynamic programming) is now O(m*n).
The memoization table has a size of O(m * n) in this case because it can potentially 
store results for all combinations of m and n subproblems. You have m choices 
for the left subtree and n choices for the right subtree, leading to a memoization 
table of size O(m * n).
"""


"""
Using memoization for the knapsack problem.
0-1 Knapsack Problem
Problem statement
You are in charge of selecting a football (soccer) team from a large pool of players. 
Each player has a cost, and a rating. You have a limited budget. What is the highest 
total rating of a team that fits within your budget. Assume that there is no minimum or 
maximum team size.

General problem statemnt:

Given n elements, each of which has a weight and a profit, determine the maximum profit 
that can be obtained by selecting a subset of the elements weighing no more than w.
"""


def optimise_rating(cost, rating, budget_input) -> int:
    team: dict = {}

    def recurse(idx=0, budget=budget_input):
        key = (idx, budget)
        # if key already has value saved, access this instead of recalculating
        if key in team:
            return team[key]
        # if idx longer than length of team, return 0
        if idx >= len(cost):
            return 0

        # if cost too high, go to next player, budget remains same
        if cost[idx] > budget:
            team[key] = recurse(idx + 1, budget)
        # if cost within budget, ignore and move to next player
        # or add on to possible rating and subtract from budget
        elif cost[idx] <= budget:
            option1 = recurse(idx + 1, budget)
            option2 = rating[idx] + recurse(idx + 1, budget - cost[idx])
            team[key] = max(option1, option2)
        return team[key]

    # empty recurse() will run with default states, i.e. what was inputted to main func
    return recurse()


"""
Dynamic programming uses bottom up approach - make a table first and solve
each cell, then find the best path.
Code below from tutor, with my notes, to solve common subsequence with DP
"""


def lcs_dp(seq1: list, seq2: list) -> int:
    n1, n2 = len(seq1), len(seq2)
    # create results table full of 0s, n1+1 long and n2+1 deep (needs 1 extra so it can
    # start at the corner at 0, in case no elements are chosen)
    results = [[0 for x in range(n2 + 1)] for x in range(n1 + 1)]
    for idx1 in range(n1):
        for idx2 in range(n2):
            # if letter/num at indexes match, add 1 to appropriate table cell (+1
            # because it starts at -1 technically)
            # use value from previous cell and add 1 to that.
            if seq1[idx1] == seq2[idx2]:
                results[idx1 + 1][idx2 + 1] = 1 + results[idx1][idx2]
            # if they don't match, find which previous cell had a higher number
            # and copy that value into the appropriate cell, as that is still the
            # highest
            else:
                results[idx1 + 1][idx2 + 1] = max(
                    results[idx1][idx2 + 1], results[idx1 + 1][idx2]
                )
    # return bottom right corner of table (remember negative numbers go from the end)
    return results[-1][-1]


"""
Use DP for knapsack problem - code from tutor but edited by me, and comments from me
"""


def knapsack_dp(budget: int, cost: list, rating: list) -> int:
    n = len(cost)
    # make a table with x and y as budget and team players
    results = [[0 for x in range(budget + 1)] for y in range(n + 1)]

    for idx in range(n):
        for c in range(budget + 1):
            # if cost is more than budget available, results cell has same value as
            # previous cell
            if cost[idx] > c:
                results[idx + 1][c] = results[idx][c]
            # if player n within budget, result cell shows the max value between
            # option a: previous cell, or
            # option b: rating of player n + value from result cell at [idx][c-cost of player n]
            else:
                results[idx + 1][c] = max(
                    results[idx][c], rating[idx] + results[idx][c - cost[idx]]
                )
    # show value in bottom right corner of table
    return results[-1][-1]


"""
Time complexity is O(n*c) as maximum number of calculations is limited to number
of table cells
"""
