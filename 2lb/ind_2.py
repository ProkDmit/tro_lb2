import numpy as np


def longest_sequence(matrix):
    return np.argmax([np.max(np.diff(np.where(np.concatenate(([row[0]], row[:-1] != row[1:],
                                                              [True])))[0])) + 1 for row in matrix])


if __name__ == '__main__':
    matrix = np.array([
        [1, 2, 1, 4, 4, 4, 4, 4, 4],
        [1, 1, 1, 1, 1, 2, 2, 2, 2],
        [1, 4, 2, 2, 2, 2, 2, 2, 2]
    ])
    print(longest_sequence(matrix))
