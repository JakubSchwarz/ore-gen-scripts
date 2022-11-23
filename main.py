import numpy as np
from rich import print

ore_matrix = np.zeros((30,180), dtype=np.int8)


def print_ore():
    for i in range(30):
        for j in range(180):
            print(ore_matrix[i][j], end='')

        print("")
print_ore()