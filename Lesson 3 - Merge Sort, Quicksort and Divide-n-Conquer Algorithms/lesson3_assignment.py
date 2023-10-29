"""
Given two polynomials represented by two lists, write a function that efficiently 
multiplies given two polynomials. For example, the lists [2, 0, 5, 7] and [3, 4, 2]
represent the polynomials 2+5x^2+7x^3 and 3+4x+2x^2.

The product of these 2 can be represented by the list [6, 8, 19, 41, 38, 14].
"""


def poly_product(poly1: list, poly2: list) -> list:
    # if 1 list is empty, return the other list
    if len(poly1) < 1:
        return poly2
    if len(poly2) < 1:
        return poly1
    product_list: list = [0] * (len(poly1) + len(poly2) - 1)
    # go through list1 in x
    # go through list2 in y
    # when x + y = K then multiply list1[x] and list2[y]
    # add them all together to get product[k]
    for x in range(len(poly1)):
        for y in range(len(poly2)):
            k = x + y
            product_list[k] += poly1[x] * poly2[y]

    # Remove trailing zeros
    while product_list and product_list[-1] == 0:
        product_list.pop()
    return product_list
