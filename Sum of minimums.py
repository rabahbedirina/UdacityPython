"""
Given a 2D list of size m * n. Your task is to find the sum of minimum value in each row.

For Example:

[
  [1, 2, 3, 4, 5],       # minimum value of row is 1
  [5, 6, 7, 8, 9],       # minimum value of row is 5
  [20, 21, 34, 56, 100]  # minimum value of row is 20
]
So, the function should return 26 because sum of minimums is as 1 + 5 + 20 = 26

Note: You will be always given non-empty list containing Positive values.

ENJOY CODING :) 
"""
import numpy as np


def sum_of_minimums(numbers, ax):

    return print(sum(np.min(numbers, axis=ax)))

  # ax row or column
sum_of_minimums([[7, 9, 8, 6, 2], [6, 3, 5, 4, 3], [5, 8, 7, 4, 5]], 1)
sum_of_minimums([[11, 12, 14, 54], [67, 89, 90, 56],
                 [7, 9, 4, 3], [9, 8, 6, 7]], 0)
