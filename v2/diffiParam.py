import sys
from random import getrandbits
from random import randrange
import isPrime
from numpy import mod as nmodule, arange


class DiffiParam:
    def __init__(self):
        # self.p = 37
        self.p: int = self.get_random_prime()
        self.q: int = self.primes(self.p-1)
        for i in range(1, self.q, int(self.q/1000000)):
            res: int = self.powerR(self.q, i, 1)
            print(res)
            if res == 0:
                self.a: int = i
                break

    def get_random_prime(self) -> int:
        while True:
            n: int = getrandbits(256) + 3
            if isPrime(n, 1, 3, recursive=False)[2] == "Tub son":
                return n

    def calc(self, Ra, Rb, xa, xb):
        self.Ra: int = getrandbits(256)
        self.Rb: int = getrandbits(256)
        self.xa: int = getrandbits(256)
        self.xb: int = getrandbits(256)
        Rb_mult_a: int = (self.inv(Rb)*self.a) % self.p
        Ra_mult_a: int = (self.inv(Rb)*self.a) % self.p
        ya: int = self.y(xa, Ra)
        yb: int = self.y(xb, Rb)
        Ra_minus_1_mult_yb: int = (self.inv(Ra)*self.y(xb, Rb)) % self.p
        Rb_minus_1_mult_ya: int = (self.inv(Rb)*self.y(xa, Ra) % self.p)
        ka: int = self.k(self.Rab(), 'a')
        kb: int = self.k(self.Rab(), 'b')
        Ka: int = self.K(self.k(self.Rab(), 'a'))
        Kb: int = self.K(self.k(self.Rab(), 'b'))

        return (Ra, Rb, xa, xb, Ra_mult_a, Rb_mult_a,
                ya, yb, Ra_minus_1_mult_yb, Rb_minus_1_mult_ya,
                self.Rab(), ka, kb, Ka, Ka, self.p)

    def inv(self, n: int) -> int:
        return pow(n, self.p-2, self.p)

    def inv_p(self, n: int, p: int) -> int:
        return pow(n, self.p-2, self.p)

    def aRb(self, a: int, b: int, R: int) -> int:
        return nmodule(a+b*(1+R*a), self.p)

    def a2(self, a: int, R: int) -> int:
        return nmodule((a*(2+R*a)), self.p)

    def bits(self, n: int) -> None:
        while n:
            yield n & 1
            n >>= 1

    def powerR(self, n: int, a: int, R: int) -> int:
        a_start: int = a
        c: int = 0
        a_mul: int = -1

        for bit in self.bits(n):
            if bit != 0:
                for _ in range(0, c):
                    a = self.a2(a, R)

                if a_mul == -1 and c != 0:
                    a_mul = self.aRb(a_start, a, R)
                elif a_mul == -1 and a == a_start:
                    a_mul = a
                else:
                    a_mul = self.aRb(a_mul, a, R)
                a = a_start
            c += 1

        return nmodule(a_mul, self.p)

    def y(self, x: int, R: int) -> int:
        """ xa, xb va Ra,Rb uchun o'rinli """
        return nmodule(self.powerR(x, self.a*self.inv(R), R), self.p)

    def Rab(self) -> int:
        return nmodule((self.Ra*self.Rb), self.p)

    def k(self, Rab: int, k_type='a') -> int:
        """ ka, kb uchun o'rinli """
        if k_type == 'a':
            return nmodule(self.powerR(self.xa, self.y(self.xb, self.Rb)*self.inv(self.Ra), Rab), self.p)
        elif k_type == 'b':
            return nmodule(self.powerR(self.xb, self.y(self.xa, self.Ra)*self.inv(self.Rb), Rab), self.p)

    def K(self, k: int) -> int:
        """k = k(xa, Ra)  yoki k(xb, Rb) """
        return k+nmodule(((((((self.y(self.xa, self.Ra)*self.y(self.xb, self.Rb)*self.inv(self.a)-k))*self.inv_p(self.p, 1))))*self.p), (self.p*self.Ra*self.Rb))

    def primes(self, N: int) -> int:
        start: int = 1461501637330902918203684832716283019655932542976 #2^160
        start += randrange(1, 100) # for getting random prime
        for i in range(start, N+1):
            if isPrime(i+3, 1, 3, recursive=False)[2] == "Tub son":
                return i+3


# import time
diff = DiffiParam()
# start_time = time.time()
# print(diff.powerROLD(221332423432432423423412333, 3213, 312312))
# end_time = (time.time() - start_time)*1000
# print(end_time)
# start_time = time.time()
# print(diff.powerR(221332423432432423423412333, 3213, 312312))
# end_time = (time.time() - start_time)*1000
# print(end_time)
# tester = [
#     [213, 32, 32],
#     [2321312312, 3213123, 123123],
#     [213213, 2313213, 32321321321],
#     [123123, 21321, 21321],
#     [2643513, 6666, 34324662],
#     [3123123, 6666213123, 213123],
#     [2643513213123, 6123123666, 32423],
#     [261232143513,3123213, 32432]
# ]
# for _ in range(200):
# tester.append([randrange(0, 3123213123), randrange(0, 3123213123), randrange(0, 3123213123)])

# for i in tester:
#     res = (diff.powerRold(*i)==diff.powerR(*i)) and (diff.powerRold(*i)==diff.powerRR(*i))
#     print(diff.powerRold(*i), diff.powerRR(*i))


# export diffiParam class
# sys.modules[__name__] = DiffiParam
