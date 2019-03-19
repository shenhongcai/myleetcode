"""   
@Project Name: LeetCode
@Author: Shen Hongcai
@Time: 2019-03-19, 17:14
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""

def generatetriangle(n):

    if n < 1:
        return []
    triangle = []
    for row_num in range(n):
        row_array = [None for _ in range(row_num+1)]
        row_array[0], row_array[-1] = 1, 1
        for j in range(1, len(row_array)-1):
            row_array[j]=triangle[row_num-1][j-1]+triangle[row_num-1][j]
        triangle.append(row_array)
        print(row_array)
    return triangle


generatetriangle(5)












