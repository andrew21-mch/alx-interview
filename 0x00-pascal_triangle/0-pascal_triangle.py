#!/usr/bin/python3
def pascal_triangle(n):
    """
    Return a list of lists representing Pascal's triangle of n rows.
    """
    # if n <= 0:
    #     return []
    # if n == 1:
    #     return [[1]]
    # triangle = [[1]]
    # for i in range(1, n):
    #     row = [1]
    #     for j in range(1, i):
    #         row.append(triangle[i-1][j-1] + triangle[i-1][j])
    #     row.append(1)
    #     triangle.append(row)
    # return triangle
    pascal = [[1]]
    if n == 1:
        return pascal

    for i in range(1, n):
        left = -1
        right = 0
        in_pas = []
        for j in range(i + 1):
            num = 0 
            if left > -1:
                num += pascal[i - 1][left]
            if right < i:
                num += pascal[i - 1][right]
            left += 1
            right += 1
            in_pas.append(num)
        pascal.append(in_pas)
    return pascal