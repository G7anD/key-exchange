import numpy as np
import random

class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init


# teskari modulni hisoblash
def inv(n):
    for i in range(p):
        if (n * i) % p == 1:
            return i
    return 0


# egri chiziqga tegisli nuqtami
def isPoint(a1):
    y = a1.y*a1.y
    y = np.mod(y, p)
    x = (a1.x*a1.x*a1.x + a*a1.x + b)
    x = np.mod(x, p)
    if(x == y):
        return True
    else:
        return False


# egri chiziqdagi nuqtalarni chiqarish
def allPoints(a, b, p):
    c = 0
    points = []
    for i in range(0, p):
        for j in range(0, p):
            a2 = Point(i, j)
            if(isPoint(a2) == True):
                # print((i, j))
                c += 1
                points.append((i, j))
    return (c, points)


def bits(n):
    result = []
    while n:
        result.append(n & 1)
        n >>= 1
    return result


def add(P, Q):
    if P is None or Q is None:  # check for the zero point
        return P or Q
    xp, yp = P
    xq, yq = Q

    if xp == xq and yp==yq:
        return double(P)

    if xp == xq and yp != yq:
        return None

    m = ((yp - yq) * inv(xp - xq)) % p
    xr = (m**2 - xp - xq) % p
    yr = (m * (xp - xr) - yp) % p
    return (xr, yr)


def double(P):
    if P is None:
        return None
    xp, yp = P
    m = ((3 * xp ** 2 + a) * inv(2 * yp)) % p
    xr = (m**2 - 2*xp) % p
    yr = (m * (xp - xr)-yp) % p
    return (xr, yr)


def double_and_add(n, x):
    result = None
    addend = x
    for bit in bits(n):
        if bit:
            result = add(result, addend)
        addend = double(addend)
    return result


def check_ab(a, b):
    return (4 * a*a*a + 27 * b * b) != 0


def primes(N):
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


def findP(prime, points):
    point_linst = []
    for point in points:
            multiple_for_n = double_and_add(prime, point)
            h = int((len(points)+1)/prime)
            if multiple_for_n==None:
                point_linst.append((point, h),)
    return point_linst[random.randrange(0, len(point_linst))]


if __name__ == "__main__":
    a, b, p = int(input("a=")), int(input("b=")), int(input("p="))
    # a, b, p = (-1, 3, 37)

    if not check_ab(a, b):
        print("Bu parametrlar mos tushmaydi(a, b)")
        # return None
    
    all_points = allPoints(a, b, p)
    N = all_points[0]+1
    n = min(primes(N))
    G, h = findP(n, all_points[1])
    
    print()
    print(N, " - Nuqtalar soni(N)")
    print(primes(N), " - tub bo'luvchilari(n)")
    print(all_points[1], " - Egri chiziqdagi nuqtalar")
    print(G, " - Ixtiyoriy nuqta")
    print(f"\np={p}\na={a}\nb={b}\nG={G}\nn={n}\nh={h}")
    print("\n\n\n")
    # p, a, b, G, n, h


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
