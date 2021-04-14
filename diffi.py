from random import getrandbits
from random import randint


def is_prime_calc(num):
    return all(num % i for i in range(2, num))


def is_prime(num):
    return is_prime_calc(num)


def get_random_prime():
    while True:
        n = getrandbits(12) + 3;
        if is_prime(n):
            return n


def ekub(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def primitive_root(modulo):
    required_set = set(num for num in range (1, modulo) if ekub(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range(1, modulo))
        if required_set == actual_set:
            return g


# Maxfiy kalitlarni generatsiya qilish
a = randint(999, 999999)
print('Alisaning ochiq kaliti %d' % a)


b = randint(999, 999999)
print('Bobning ochiq kaliti %d' % b)


# p va g parametrlarni generatsiya qilish
p = get_random_prime()
g = primitive_root(p)


print('\np=%d \ng=%d \n' % (p, g))


# Ochiq kalitlarni generatsiya qilish
A = pow(g, a) % p
B = pow(g, b) % p


print('Alisaning ochiq kaliti %d' % A)
print('Bobning ochiq kaliti %d' % B)


Ka = (pow(B, a)) % p
Kb = (pow(A, b)) % p


print('Ka=%d\nKb=%d' % (Ka, Kb))
