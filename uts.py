print ("hello world")
import numpy as np
def soal_matrix():
    
    C = np.array([
        [44, 55, 54, 10],
        [33, 5, 32, 13],
        [21, 7, 21, 11],
        [33, 88, 32, 15]
    ])

    D = np.array([
        [2, 1, 1, 1],
        [2, 1, 0, 2],
        [2, 0, 1, 2],
        [1, 1, 1, 2]
    ])

    result = np.dot(C, D)

    
    print("Matrix C:")
    print(C)
    print("\nMatrix D:")
    print(D)
    print("\nHasil Dari C x D:")
    print(result)

if __name__ == "__main__":
    soal_matrix()
