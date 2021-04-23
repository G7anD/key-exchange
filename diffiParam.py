import sys
from random import getrandbits
from random import randrange
import isPrime


class DiffiParam:
    def __init__(self):
        self.p = self.get_random_prime()
        q_list = self.primes(self.p-1)
        self.q = q_list[randrange(0, len(q_list))]

        for i in range(self.q):
            if self.powerR(self.q, i, 1) == 0:
                self.a = i
                break

    def get_random_prime(self):
        while True:
            n = getrandbits(512) + 3
            if isPrime(n, 1, 3, recursive=False)[2] == "Tub son":
                return n

    def calc(self, Ra, Rb, xa, xb):
        self.Ra = Ra
        self.Rb = Rb
        self.xa = xa
        self.xb = xb
        Rb_mult_a = (self.inv(Rb)*self.a) % self.p
        Ra_mult_a = (self.inv(Rb)*self.a) % self.p
        ya = self.y(xa, Ra)
        yb = self.y(xb, Rb)
        Ra_minus_1_mult_yb = (self.inv(Ra)*self.y(xb, Rb)) % self.p
        Rb_minus_1_mult_ya = (self.inv(Rb)*self.y(xa, Ra) % self.p)
        ka = self.k(self.Rab(), 'a')
        kb = self.k(self.Rab(), 'b')
        Ka = self.K(self.k(self.Rab(), 'a'))
        Kb = self.K(self.k(self.Rab(), 'b'))

        return (Ra, Rb, xa, xb, Ra_mult_a, Rb_mult_a,
                ya, yb, Ra_minus_1_mult_yb, Rb_minus_1_mult_ya,
                self.Rab(), ka, kb, Ka, Ka)

    # teskari modulni hisoblash
    def inv(self, n):
        return pow(n, self.p-2, self.p)

    # teskari modulni hisoblash
    def inv_p(self, n, p):
        for i in range(p):
            if (n * i) % p == 1:
                return i
        return 1

    def aRb(self, a, b, R):
        return a+b*(1+R*a) % self.p

    def a2(self, a, R):
        return (a*(2+R*a)) % self.p

    def bits(self, n):
        result = []
        while n:
            result.append(n & 1)
            n >>= 1
        return result

    def powerR(self, n, a, R):
        a_start = a
        c = 0
        addList = []

        for bit in self.bits(n):
            if bit == 0 and c != 0:
                c += 1
                continue

            for times in range(c):
                a = self.a2(a, R)
            addList.append(a)
            c += 1
            a = a_start

        a_mul = 1
        for i in range(len(addList)-1):

            if i != 0:
                a_mul = self.aRb(a_mul, addList[i+1], R)
            else:
                a_mul = self.aRb(addList[i], addList[i+1], R)

        return a_mul % self.p

    def y(self, x, R):
        """ xa, xb va Ra,Rb uchun o'rinli """
        return self.powerR(x, self.a*self.inv(R), R) % self.p

    def Rab(self):
        return (self.Ra*self.Rb) % self.p

    def k(self, Rab, k_type='a'):
        """ ka, kb uchun o'rinli """
        if k_type == 'a':
            return self.powerR(self.xa, self.y(self.xb, self.Rb)*self.inv(self.Ra), Rab) % self.p
        elif k_type == 'b':
            return self.powerR(self.xb, self.y(self.xa, self.Ra)*self.inv(self.Rb), Rab) % self.p

    def K(self, k):
        """k = k(xa, Ra)  yoki k(xb, Rb) """
        return k+((((((self.y(self.xa, self.Ra)*self.y(self.xb, self.Rb)*self.inv(self.a)-k))*self.inv_p(self.p, (self.Ra*self.Rb)))))*self.p) % (self.p*self.Ra*self.Rb)

    def is_prime_calc(self, num):
        return all(num % i for i in range(2, num))

    def primes(self, N):
        tublari = []
        for i in range(pow(2, 163), N+1):
            if isPrime(i+3, 1, 3, recursive=True)[2] == "Tub son":
                tublari.append(i)
                break; 
        return tublari


# export diffiParam class
sys.modules[__name__] = DiffiParam
