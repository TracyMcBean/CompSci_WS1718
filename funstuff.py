import numpy as np


class numbers:
    def __init__(self):
        self.nr = []

    def number_func(self, n, m):
        nr = np.random.random_sample((n, m))
        return nr


random_nr = numbers
np.reshape(random_nr, 1)
#random_nr = random_nr.number_func()
positions = 0.05 * np.random.random_sample((4, 3))
print(positions)
#print(0.05 * np.random.random_sample((6,3)))
print(positions[1][1])
hallo = positions[1]
hallo = [-1] * 10
print(positions.shape[0])
print(hallo)


