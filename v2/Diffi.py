from random import getrandbits
from random import randint
import isPrime

def is_prime_calc(num):
    return all(num % i for i in range(2, num))


def is_prime(num):
    return is_prime_calc(num)


class Diffi:
    def __init__(self, g):
        self.g = g

    def get_random_prime(self,):
        while True:
            n = getrandbits(512) + 3;
            if isPrime(n, 1, 3, recursive=False)[2]=="Tub son":
                return n

    def ekub(self, a,b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    def primitive_root(self, modulo):
        required_set = set(num for num in range (1, modulo) if ekub(num, modulo) == 1)
        for g in range(1, modulo):
            actual_set = set(pow(g, powers) % modulo for powers in range(1, modulo))
            if required_set == actual_set:
                return g

    def calc(self):
        # Yopiq kalitlarni generatsiya qilish
        a = randint(999, 999999)
        b = randint(999, 999999)
        p = self.get_random_prime()

        # Ochiq kalitlarni generatsiya qilish
        A = pow(self.g, a, p)
        B = pow(self.g, b, p)

        Ka = pow(B, a, p)
        Kb = pow(A, b, p)

        # print('Alisaning yopiq kaliti %d' % a)
        # print('Bobning yopiq kaliti %d' % b)
        # print('\np=%d \ng=%d \n' % (p, self.g))
        # print('Alisaning ochiq kaliti %d' % A)
        # print('Bobning ochiq kaliti %d' % B)
        # print('Ka=%d\nKb=%d' % (Ka, Kb))
        return (a, b, p, self.g, A, B, Ka, Kb)


# export Diffi class
import sys
sys.modules[__name__] = Diffi