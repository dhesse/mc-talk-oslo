import numpy as np

class TrafficMC(object):
    def __init__(self, N, k, M, p):
        self.N, self.p, self.M, self.k = N, p, M, k
        self.x = np.sort(np.random.choice(N, k, False))
        self.v = np.zeros(k, int)
        assert all(self.x[:-1] < self.x[1:])
    def step(self):
        self.v = np.minimum(self.v + 1, self.M)
        d = (np.roll(self.x, -1) - self.x) % self.N
        self.v = np.minimum(self.v, d - 1)
        mask = np.random.uniform(size=self.k) < self.p
        self.v[mask] -= 1
        self.v = np.maximum(self.v, 0)
        self.x += self.v
        self.x %= self.N