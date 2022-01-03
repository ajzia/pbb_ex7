from tqdm import tqdm
import numpy as np
import json

gen = np.random.default_rng() # random number generator

class Simulation():
    def __init__(self, n_beg: int, n_end: int, k: int, d: int, change: int):
        assert(d <= 3)
        self.n_beg = n_beg
        self.n_end = n_end
        self.k = k
        self.d = d
        self.change = change
        self.keys = dict.fromkeys(['Ln'], 0)

        for i in self.keys:
            self.keys[i] = [[0 for i in range(self.k)] for j in range(self.n_beg, self.n_end + 1)] # list for every dict value filled with zeros 

        self.end = False;

    def run(self):
        for i in range(self.n_beg, self.n_end + 1):  # n_end + 1 - end_beg - times
            print(i)
            for j in range(self.k):  # number of tries

                ln = 0
                n = i * self.change
                
                urns = [0] * n   # creating n urns

                random = [] 
                for l in range(0, self.d):
                    random.append(gen.integers(low=n, size=n))   # random urn numbers
                m = 0  # ball number
                min_balls = 0
                random_urn = 0

                while not(self.end):    # until n == m

                    if self.d == 1:
                        random_urn = random[0][m]
                    elif self.d == 2:
                        min_balls = min(urns[random[0][m]], urns[random[1][m]])

                        if min_balls == urns[random[0][m]]:
                            random_urn = random[0][m]
                        else:
                            random_urn = random[1][m]

                    elif self.d == 3:
                        min_balls = min(urns[random[0][m]], urns[random[1][m]], urns[random[2][m]])

                        if min_balls == urns[random[0][m]]:
                            random_urn = random[0][m]
                        elif min_balls == urns[random[1][m]]:
                            random_urn = random[1][m]
                        else:
                            random_urn = random[2][m]

                    urns[random_urn] += 1
                    m += 1

                    # max number of balls in an urn
                    if m <= n and urns[random_urn] > ln:
                        ln = urns[random_urn]
                    
                    # ln - maximum number of balls in an urn after n balls
                    if m == n:
                        self.keys['Ln'][i - 1][j] = ln
                        self.end = True
                        break
                
                self.end = False

# d = 1
sim = Simulation(n_beg=1, n_end=100, k=50, d=1, change=10000)
sim.run()
print(sim.keys)
json.dump(sim.keys, open('d1_zad2.json','w'))
# d = 2
sim2 = Simulation(n_beg=1, n_end=100, k=50, d=2, change=10000)
sim2.run()
print(sim2.keys)
json.dump(sim2.keys, open('d2_zad2.json','w'))

# d = 3
sim3 = Simulation(n_beg=1, n_end=100, k=50, d=3, change=10000)
sim3.run()
print(sim3.keys)
json.dump(sim3.keys, open('d3_zad2.json','w'))