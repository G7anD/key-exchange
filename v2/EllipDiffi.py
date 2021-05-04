import numpy as np
from random import randint, randrange, getrandbits
import isPrime
import sys

class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init


class EllipDiffi:
    def __init__(self, a, b):
        self.p = self.get_random_prime()
        self.a = a
        self.b = b

    def get_random_prime(self):
        while True:
            n = getrandbits(12) + 3
            if isPrime(n, 1, 3, recursive=False)[2] == "Tub son":
                return n


    def inv(self, n):
        return pow(n, self.p-2, self.p)


    def isPoint(self, a1):
        y = a1.y*a1.y
        y = np.mod(y, self.p)
        x = (a1.x*a1.x*a1.x + self.a*a1.x + self.b)
        x = np.mod(x, self.p)
        if(x == y):
            return True
        else:
            return False

    def allPoints(self):
        c = 0
        points = []
        for i in range(0, self.p):
            for j in range(0, self.p):
                print(i, j)
                a2 = Point(i, j)
                if(self.isPoint(a2) == True):
                    c += 1
                    points.append((i, j))
        return (c, points)

    def bits(self, n):
        result = []
        while n:
            result.append(n & 1)
            n >>= 1
        return result

    def add(self, P, Q):
        if P is None or Q is None:  # check for the zero point
            return P or Q
        xp, yp = P
        xq, yq = Q

        if xp == xq and yp == yq:
            return self.double(P)

        if xp == xq and yp != yq:
            return None

        m = ((yp - yq) * self.inv(xp - xq)) % self.p
        xr = (m**2 - xp - xq) % self.p
        yr = (m * (xp - xr) - yp) % self.p
        return (xr, yr)

    def double(self, P):
        if P is None:
            return None
        xp, yp = P
        m = ((3 * xp ** 2 + self.a) * self.inv(2 * yp)) % self.p
        xr = (m**2 - 2*xp) % self.p
        yr = (m * (xp - xr)-yp) % self.p
        return (xr, yr)

    def double_and_add(self, n, x):
        result = None
        addend = x
        for bit in self.bits(n):
            if bit:
                result = self.add(result, addend)
            addend = self.double(addend)
        return result

    def primes(self, N):
        tublari = []
        for i in range(2, N+1):
            if N % i == 0 and i % 2 != 0:
                c = 0
                for j in range(1, i+1):
                    if i % j == 0:
                        c += 1
                if c < 3:
                    tublari.append(i)
        return tublari

    def findP(self, prime, points):
        point_linst = []
        for point in points:
            multiple_for_n = self.double_and_add(prime, point)
            h = int((len(points)+1)/prime)
            if multiple_for_n == None:
                point_linst.append((point, h),)
        return point_linst[randrange(0, len(point_linst))]


    def calc(self):
        # all_points = self.allPoints()
        # print(all_points)
        # N = all_points[0]+1
        # prim = self.primes(N)
        # n = min(prim)
        # G, h = self.findP(n, all_points[1])
        self.a = -3
        self.b = int("0x051953eb9618e1c9a1f929a21a0b68540eea2da725b99b315f3b8b489918ef109e156193951ec7e937b1652c0bd3bb1bf073573df883d2c34f1ef451fd46b503f00", 16)
        self.p = 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151
        G = (int("0xc6858e06b70404e9cd9e3ecb662395b4429c648139053fb521f828af606b4d3dbaa14b5e77efe75928fe1dc127a2ffa8de3348b3c1856a429bf97e7e31c2e5bd66", 16), 
                    int("0x11839296a789a3bc0045c8a5fb42c7d1bd998f54449579b446817afbd17273e662c97ee72995ef42640c550b9013fad0761353c7086a272c24088be94769fd16650", 16),)
        n = 6864797660130609714981900799081393217269435300143305409394463459185543183397655394245057746333217197532963996371363321113864768612440380340372808892707005449
        h=1
        a_maxfiy = randint(1, n-1)
        b_maxfiy = randint(1, n-1)
        A_nuqta = self.double_and_add(a_maxfiy, G)
        B_nuqta = self.double_and_add(b_maxfiy, G)
        K_a = self.double_and_add(a_maxfiy, B_nuqta)
        K_b = self.double_and_add(b_maxfiy, A_nuqta)

        # print(N, " - Nuqtalar soni(N)")
        # print(prim, " - tub bo'luvchilari(n)")
        # print(all_points[1], " - Egri chiziqdagi nuqtalar")
        # print(G, " - Ixtiyoriy nuqta")
        # print(f"\np={self.p}\na={self.a}\nb={self.b}\nG={G}\nn={n}\nh={h}")
        # print(f'K_a={K_a}\nK_b={K_b}')
        return ("N", "prim", "all_points[1]", G, self.p, self.a, self.b, G, h, a_maxfiy, b_maxfiy, A_nuqta, B_nuqta, K_a, K_b)

# export EllipDiffiParam class
sys.modules[__name__] = EllipDiffi
# elp = EllipDiffi(-1, 3)
# print(elp.calc())

# if __name__ == "__main__":
#     # a, b, p = int(input("a=")), int(input("b=")), int(input("p="))
#     a, b, p = (-1, 3, 29)

#     all_points = allPoints(a, b, p)
#     N = all_points[0]+1
#     n = min(primes(N))
#     G, h = findP(n, all_points[1])

#     # Maxfiy kalitlar
#     a_maxfiy = randint(1, n-1)
#     b_maxfiy = randint(1, n-1)
#     print(a_maxfiy)
#     print(b_maxfiy)

#     A_nuqta = double_and_add(a_maxfiy, G)
#     B_nuqta = double_and_add(b_maxfiy, G)
#     print(A_nuqta)
#     print(B_nuqta)

#     K_a = double_and_add(a_maxfiy, B_nuqta)
#     K_b = double_and_add(b_maxfiy, A_nuqta)

#     print(f'K_a={K_a}\nK_b={K_b}')

    # print()
    # print(N, " - Nuqtalar soni(N)")
    # print(primes(N), " - tub bo'luvchilari(n)")
    # print(all_points[1], " - Egri chiziqdagi nuqtalar")
    # print(G, " - Ixtiyoriy nuqta")
    # print(f"\np={p}\na={a}\nb={b}\nG={G}\nn={n}\nh={h}")
    # print("\n\n\n")
