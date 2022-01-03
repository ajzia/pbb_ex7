import numpy as np
import json
from time import time

gen = np.random.default_rng() # random number generator

class Simulation():
    def __init__(self, n_beg: int, n_end: int, k: int, change: int):
        self.n_beg = n_beg
        self.n_end = n_end
        self.k = k
        self.change = change

        self.keys = dict.fromkeys(['cmp', 's', 'time'], 0)

        for i in self.keys:
            self.keys[i] = [[0 for i in range(self.k)] for j in range(self.n_beg, self.n_end + 1)] # list for every dict value filled with zeros 

    def run(self):
        for i in range(self.n_beg, self.n_end + 1):  # n_end + 1 - end_beg - times

            print(i)

            n = i * self.change

            perm = [gen.permutation(n) for l in range (self.k)] # k-permutations
            
            for j in range(self.k):     # number of tries

                compares = 0
                switches = 0
                curr_perm = perm[j]     # current permutation

                start = time()

                for h in range(1, n):
                    
                    key = curr_perm[h]
                    l = h - 1
                    
                    while l >= 0 and curr_perm[l] > key:
                        compares += 1
                        curr_perm[l + 1] = curr_perm[l]
                        switches += 1
                        l = l - 1
                    curr_perm[l + 1] = key
                    switches += 1

                end = time()

                self.keys['cmp'][i - 1][j] = compares
                self.keys['s'][i - 1][j] = switches
                self.keys['time'][i - 1][j] = end - start


# k = 1
sim = Simulation(n_beg=1, n_end=100, k=1, change=100)
sim.run()
print(sim.keys)
json.dump(sim.keys, open('k1_zad3.json','w'))

# k = 10
sim = Simulation(n_beg=1, n_end=100, k=10, change=100)
sim.run()
print(sim.keys)
json.dump(sim.keys, open('k10_zad3.json','w'))

# k = 100
sim = Simulation(n_beg=1, n_end=100, k=100, change=100)
sim.run()
print(sim.keys)
json.dump(sim.keys, open('k100_zad3.json','w'))
