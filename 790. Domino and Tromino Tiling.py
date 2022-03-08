import math


class Solution:

    def numTilings(self, n: int) -> int:
        f = [0, 1, 2]
        g = [0, 0, 2]

        for i in range(3, n + 1):
            f.append(g[i - 1] + f[i - 1] + f[i - 2])
            g.append(g[i - 1] + 2 * f[i - 2])

        return int(f[n] % (math.pow(10, 9) + 7))

    