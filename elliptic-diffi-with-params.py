import numpy as np
from random import randint, randrange

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

def y_inv(y):
    return (-(y+2*inv(R)))%p

# egri chiziqga tegisli nuqtami
def isPoint(a1):
    y = a2(a1.y)
    y = np.mod(y, p)
    x = (aRb(a2(a1.x),a1.x) + a*a1.x + b)
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


def a_inv(a, R, p):
    return (-a*(1+R*a)-1)%р


def aRb(a, b):
    return a+b*(1+R*a)%p


def a2(a):
    return (a*(2+R*a))%p


def powerR(n, a, b, p, R):
    a_start = a
    c = 0
    addList = []
    for bit in bits(n):
        if bit==0 and c!=0:
            c += 1
            continue

        for times in range(c):
            a = a2(a, R, p)
        addList.append(a)
        c += 1
        a = a_start


    a_mul = 1
    for i in range(len(addList)-1):

        if i!=0:
            a_mul = aRb(a_mul, addList[i+1])
        else:
            a_mul = aRb(addList[i], addList[i+1])

    return a_mul%p


def add(P, Q):
    if P is None or Q is None:
        return P or Q
    x1, y1 = P
    x2, y2 = Q

    if x2 == x1 and (y1==y2) and y1!=0 and y2!=0:
        return double(P)

    elif x1!=x2:
        L = ((y2 - y1) * inv(x2 - x1)) % p
        x3 = ((L**2-3)*inv(R) - x1 - x2) % p
        y3 = (L * (x1 - x3) - y_inv(y1)) % p
        return (x3, y3)

    elif x2 == x1 and (y2==y_inv(y1)):
        return None


def double(P):
    if P is None:
        return None

    x1, y1 = P
    L = ((3*(R*a2(x1)+1)+a)*inv(2*(R*y1+1)))%p
    x3 = ((L**2-3)*inv(R) - 2*x1) % p
    y3 = (L * (x1 - x3) - y_inv(y1)) % p
    return (x3, y3)


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
            print(multiple_for_n, prime)
            if multiple_for_n==None:
                point_linst.append((point, h),)
    return point_linst[randrange(0, len(point_linst))]


def showResult(a, b, p):
    if not check_ab(a, b):
        print("Bu parametrlar mos tushmaydi(a, b)")
        # return None

    all_points = allPoints(a, b, p)
    N = all_points[0]+1
    n = min(primes(N))
    print(all_points[1])
    G, h = findP(n, all_points[1])

    print()
    print(N, " - Nuqtalar soni(N)")
    print(primes(N), " - tub bo'luvchilari(n)")
    print(all_points[1], " - Egri chiziqdagi nuqtalar")
    print(G, " - Ixtiyoriy nuqta")
    print(f"\np={p}\na={a}\nb={b}\nG={G}\nn={n}\nh={h}")
    print("\n\n\n")

if __name__ == "__main__":
    # a, b, p = int(input("a=")), int(input("b=")), int(input("p="))
    # # a, b, p = (-1, 3, 29)
    # showResult(a, b, p)


    # if not check_ab(a, b):
    #     print("Bu parametrlar mos tushmaydi(a, b)")
    #     # return None
    
    # all_points = allPoints(a, b, p)
    # N = all_points[0]+1
    # n = min(primes(N))
    # G, h = findP(n, all_points[1])

    # # Maxfiy kalitlar
    # a_maxfiy = randint(1, n-1)
    # b_maxfiy = randint(1, n-1)
    # print(a_maxfiy)
    # print(b_maxfiy)

    # A_nuqta = double_and_add(a_maxfiy, G)
    # B_nuqta = double_and_add(b_maxfiy, G)
    # print(A_nuqta)
    # print(B_nuqta)

    # K_a = double_and_add(a_maxfiy, B_nuqta)
    # K_b = double_and_add(b_maxfiy, A_nuqta)

    # print(f'K_a={K_a}\nK_b={K_b}')

    # print()
    # print(N, " - Nuqtalar soni(N)")
    # print(primes(N), " - tub bo'luvchilari(n)")
    # print(all_points[1], " - Egri chiziqdagi nuqtalar")
    # print(G, " - Ixtiyoriy nuqta")
    # print(f"\np={p}\na={a}\nb={b}\nG={G}\nn={n}\nh={h}")
    # print("\n\n\n")

    # print(powerR(7, 3, 1, 11, 2))
    # print(y_inv(3, 2, 7))

    p = 229
    a = 1
    B = 137
    R = 2
    b = B

    # showResult(a, B, p)
    # print(a2(4))
    # print(aRb(a2(4), 115))
    # print(double_and_add(207, (115, 4)))
    print(inv(2))
