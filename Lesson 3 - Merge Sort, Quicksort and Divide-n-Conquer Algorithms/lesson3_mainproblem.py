"""
QUESTION 1: You're working on a new feature on Jovian called "Top Notebooks of the 
Week". Write a function to sort a list of notebooks in decreasing order of likes. 
Keep in mind that up to millions of notebooks can be created every week, so your 
function needs to be as efficient as possible.
"""


class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes

    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(
            self.username, self.title, self.likes
        )


# sample notebooks
nb0 = Notebook("strange-new-worlds", "chrisp", 373)
nb1 = Notebook("voyager", "kathrynj", 532)
nb2 = Notebook("original-series", "jimk", 31)
nb3 = Notebook("next-gen", "jeanlucp", 94)
nb4 = Notebook("enterprise", "captainarcher", 2)
nb5 = Notebook("clinical-dietetics-manual", "dessertivore", 29)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5]


# compare notebooks function - sort highest to lowest number likes
def compare_likes(nb1: Notebook, nb2: Notebook) -> str:
    if nb1.likes > nb2.likes:
        return "lesser"
    elif nb1.likes == nb2.likes:
        return "equal"
    elif nb1.likes < nb2.likes:
        return "greater"
    else:
        raise ValueError


# sort list of notebooks - default is to sort by likes but can input
# other compare function
def quicksort_nbs(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    # this preserves duplicates when sorting
    # if duplicates are to be removed, change 'right' so it only accepts
    # "greater" rather than greater AND equal
    else:
        pivot: Notebook = arr[0]
        left = [x for x in arr[1:] if compare_likes(x, pivot) == "lesser"]
        right = [x for x in arr[1:] if compare_likes(x, pivot) != "lesser"]

        return quicksort_nbs(left) + [pivot] + quicksort_nbs(right)


# sort list of notebooks by title
def compare_titles(nb1: Notebook, nb2: Notebook) -> str:
    if nb1.title < nb2.title:
        return "lesser"
    elif nb1.title == nb2.title:
        return "equal"
    elif nb1.title > nb2.title:
        return "greater"
    else:
        raise ValueError


# could change quicksort function to accept 'compare' as an input
# then can choose either compare titles or compare likes
# sorted_alphabetically = quicksort_nbs(notebooks, compare_titles)
# print(sorted_alphabetically)

print(quicksort_nbs(notebooks))
