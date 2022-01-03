import numpy as np
import json

gen = np.random.default_rng() # random number generator

class Simulation():
    def __init__(self, n_beg: int, n_end: int, k: int, change: int):
        self.n_beg = n_beg
        self.n_end = n_end
        self.k = k
        self.change = change
        self.keys = dict.fromkeys(['Bn', 'Un', 'Ln', 'Cn', 'Dn', 'Dn_Cn'], 0)

        for i in self.keys:
            self.keys[i] = [[0 for i in range(self.k)] for j in range(self.n_beg, self.n_end + 1)] # list for every dict value filled with zeros 

        self.flags = {
            'bn': True,
            'dn': True,
        }

    def run(self):
        for i in range(self.n_beg, self.n_end + 1): # n_end + 1 - end_beg - times
            print(f'curr: {i}')
            for j in range(0, self.k):  # number of tries

                ln = 0
                cn_count = 0
                dn_count = 0
                n = i * self.change
                size = n * self.change

                urns = [0] * n   # creating n urns
                random = gen.integers(low=n, size=size)   # array n * 1000 with random numbers from 0 to n

                m = 0;  # ball number

                while self.flags['dn']:    # until dn is satisfied
                    
                    if m < size: # using already generated numbers
                        random_urn = random[m]
                        urns[random_urn] += 1
                        m += 1
                    else:
                        random_urn = gen.integers(low=n) # random number from 0 to n
                        urns[random_urn] += 1
                        m += 1
                    
                    if urns[random_urn] == 1:
                        cn_count += 1
                    elif urns[random_urn] == 2:
                        dn_count += 1

                    # max number of balls in an urn
                    if m < n and urns[random_urn] > ln:
                        ln = urns[random_urn]

                    # bn - first collision
                    if(self.flags['bn']):
                        if urns[random_urn] == 2:
                            self.keys['Bn'][i - 1][j] = m
                            self.flags['bn'] = False

                    # un and ln - nof empty urns and maximum number of balls in an urn after n balls
                    if m == n:
                        empty = 0
                        for urn in range(len(urns)):
                            if urns[urn] == 0:
                                empty += 1
                        
                        self.keys['Un'][i - 1][j] = empty
                        self.keys['Ln'][i - 1][j] = ln

                    # cn
                    if cn_count == n and self.keys['Cn'][i - 1][j] == 0:
                        self.keys['Cn'][i - 1][j] =  m

                    # dn
                    if dn_count == n:
                        self.keys['Dn'][i - 1][j] = m
                        self.flags['dn'] = False

                    # dn-cn
                    if not(self.flags['dn']):
                        self.keys['Dn_Cn'][i - 1][j] = m - self.keys['Cn'][i - 1][j]
                
                self.flags['bn'] = True
                self.flags['dn'] = True


sim = Simulation(n_beg=1, n_end=100, k=50, change=1000)
sim.run()
print(sim.keys)
json.dump(sim.keys, open('zad1.json','w'))

