import numpy as np
from random import randint, randrange, getrandbits
import isPrime
import sys


class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init


class EllipDiffiParam:
    def __init__(self, a, B, R):
        self.a = -3
        self.R = getrandbits(160)
        self.p = 6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151
        self.b = int(
            "0x051953eb9618e1c9a1f929a21a0b68540eea2da725b99b315f3b8b489918ef109e156193951ec7e937b1652c0bd3bb1bf073573df883d2c34f1ef451fd46b503f00", 16)
        self.B = self.calc_B()

    def get_random_prime(self):
        while True:
            n = getrandbits(128) + 3
            if isPrime(n, 1, 3, recursive=False)[2] == "Tub son":
                return n

    def calc_B(self):
        return ((self.b+self.a)*self.inv(self.R)) % self.p

    def calc_b(self):
        return (self.B*self.R-self.a) % self.p

    def calc(self):
        # all_points = self.allPoints(param=False)
        # N = all_points[0]+1
        # n = min(primes(N))
        # G, h = self.findP(n, all_points[1], param=False)
        G = (int("0xc6858e06b70404e9cd9e3ecb662395b4429c648139053fb521f828af606b4d3dbaa14b5e77efe75928fe1dc127a2ffa8de3348b3c1856a429bf97e7e31c2e5bd66", 16),
             int("0x11839296a789a3bc0045c8a5fb42c7d1bd998f54449579b446817afbd17273e662c97ee72995ef42640c550b9013fad0761353c7086a272c24088be94769fd16650", 16),)
        n = 6864797660130609714981900799081393217269435300143305409394463459185543183397655394245057746333217197532963996371363321113864768612440380340372808892707005449
        h = 1

        Na, Nb = randint(1, n-1), randint(1, n-1)
        pa = self.double_and_add(Na, G)
        pb = self.double_and_add(Nb, G)
        Pa = self.conv2param(pa)
        Pb = self.conv2param(pb)
        ka = self.double_and_add(Na, pb)
        kb = self.double_and_add(Nb, pa)
        Ka = self.conv2param(ka)
        Kb = self.conv2param(kb)

        return ("N", "primes(N)", self.p, self.a, self.b, G, n, h, Na, Nb, pa, pb, Pa, Pb, ka, kb, Ka, Kb)

    def conv2param(self, x, reverse=False):
        if x is None:
            return None
        if not reverse:
            return (self.powerXYR(x[0], 1), self.powerXYR(x[1], 1))
        else:
            return (self.invXYR(x[0], 1), self.invXYR(x[1], 1))

    def powerXYR(self, cord, power):
        return ((cord**power-1)*self.inv(self.R)) % self.p

    def invXYR(self, cord, power):
        return ((cord*self.R)+1) % self.p

    def inv(self, n):
        return pow(n, self.p-2, self.p)

    def y_inv(self, y):
        return (-(y+2*self.inv(self.R))) % self.p

    def findP(self, prime, points, param=False):
        point_linst = []
        for point in points:
            if not param:
                multiple_for_n = self.double_and_add(prime, point)
            else:
                multiple_for_n = self.p_double_and_add(prime, point)

            h = int((len(points)+1)/prime)
            if multiple_for_n == None:
                point_linst.append((point, h),)
        return point_linst[randrange(0, len(point_linst))]

    def isPoint(self, a1):
        y = a1.y*a1.y
        y = np.mod(y, self.p)
        x = (a1.x*a1.x*a1.x + self.a*a1.x + self.b)
        x = np.mod(x, self.p)
        if(x == y):
            return True
        else:
            return False

    def isPointP(self, a1):
        y = self.powerXYR(a1.y, 2)
        y = np.mod(y, self.p)
        x = (self.powerXYR(a1.x, 3) + self.a*a1.x + self.B)
        x = np.mod(x, self.p)
        if(x == y):
            return True
        else:
            return False

    def allPoints(self, param=False):
        c = 0
        points = []
        for i in range(0, self.p):
            for j in range(0, self.p):
                a2 = Point(i, j)
                if (self.isPoint(a2) == True and not param):
                    c += 1
                    points.append((i, j))
                elif (self.isPointP(a2) == True and param):
                    c += 1
                    points.append((i, j))

        return (c, points)

    def bits(self, n):
        result = []
        while n:
            result.append(n & 1)
            n >>= 1
        return result

    def double_and_add(self, n, x):
        result = None
        addend = x
        for bit in self.bits(n):
            if bit:
                result = self.add(result, addend)
            addend = self.double(addend)
        return result

    def p_double_and_add(self, n, P):
        result = None
        addend = P
        for bit in self.bits(n):
            if bit:
                result = self.addp(result, addend, P)
            addend = self.doublep(addend)
        return result

    def add(self, P, Q):
        if P is None or Q is None:
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

    def addp(self, P, Q, x):
        if P is None or Q is None:
            return x

        x1, y1 = P
        x2, y2 = Q
        if x1 != x2:
            L = ((y2 - y1) * self.inv(x2 - x1)) % self.p
            x3 = (((L**2)-3)*self.inv(self.R) - x1 - x2) % self.p
            y3 = (L * (x1 - x3) + self.y_inv(y1)) % self.p
            return (x3, y3)

        elif x2 == x1 and (y1 == y2) and y1 != 0 and y2 != 0:
            return self.doublep(P)

        elif x2 == x1 and (y2 == self.y_inv(y1)):
            return None

    def doublep(self, P):
        if P is None:
            return None

        x1, y1 = P
        L = ((3*(self.R*self.powerXYR(x1, 2)+1)+self.a)
             * self.inv(2*(self.R*y1+1))) % self.p
        x3 = ((L**2-3)*self.inv(self.R) - 2*x1) % self.p
        y3 = (L * (x1 - x3) + self.y_inv(y1)) % self.p
        return (x3, y3)


# export EllipDiffiParam class
sys.modules[__name__] = EllipDiffiParam
