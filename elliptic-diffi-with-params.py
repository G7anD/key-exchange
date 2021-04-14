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


# def conv2param(Point):
#     x0, y0 = Point
#     x = ((x0-1)*inv(R))%p
#     y = ((y0-1)*inv(R))%p

#     return (x, y)


def isPoint(a1):
    y = a1.y*a1.y
    y = np.mod(y, p)
    x = (a1.x*a1.x*a1.x + a*a1.x + b)
    x = np.mod(x, p)
    if(x == y):
        return True
    else:
        return False


def isPointP(a1):
    y = powerXYR(a1.y, 2)
    y = np.mod(y, p)
    x = (powerXYR(a1.x, 3) + a*a1.x + B)
    x = np.mod(x, p)
    if(x == y):
        return True
    else:
        return False


# egri chiziqdagi nuqtalarni chiqarish
def allPoints(a, b, p, param=False):
    c = 0
    points = []
    for i in range(0, p):
        for j in range(0, p):
            a2 = Point(i, j)
            if (isPoint(a2) == True and not param):
                c += 1
                points.append((i, j))
            elif (isPointP(a2) == True and param):
                c += 1
                points.append((i, j))

    return (c, points)


def bits(n):
    result = []
    while n:
        result.append(n & 1)
        n >>= 1
    return result


def powerXYR(cord, power):
    return ((cord**power-1)*inv(R))%p

def invXYR(cord, power):
    return ((cord*R)+1)%p

def inv_b(B):
    return ((B*R)-a)%p

# def a_inv(a, R, p):
#     return (-a*(1+R*a)-1)%р


# def aRb(a, b):
#     return a+b*(1+R*a)%p


# def a2(a):
#     return (a*(2+R*a))%p


# def powerR(n, a, b, p, R):
#     a_start = a
#     c = 0
#     addList = []
#     for bit in bits(n):
#         if bit==0 and c!=0:
#             c += 1
#             continue

#         for times in range(c):
#             a = a2(a, R, p)
#         addList.append(a)
#         c += 1
#         a = a_start


#     a_mul = 1
#     for i in range(len(addList)-1):

#         if i!=0:
#             a_mul = aRb(a_mul, addList[i+1])
#         else:
#             a_mul = aRb(addList[i], addList[i+1])

#     return a_mul%p


def addp(P, Q, x):
    if P is None or Q is None:
        return x

    x1, y1 = P
    x2, y2 = Q
    if x1!=x2:
        L = ((y2 - y1) * inv(x2 - x1)) % p
        x3 = (((L**2)-3)*inv(R) - x1 - x2) % p
        y3 = (L * (x1 - x3) + y_inv(y1)) % p
        return (x3, y3)

    elif x2 == x1 and (y1==y2) and y1!=0 and y2!=0:
        return doublep(P)

    elif x2 == x1 and (y2==y_inv(y1)):
        return None


def doublep(P):
    if P is None:
        return None

    x1, y1 = P
    L = ((3*(R*powerXYR(x1, 2)+1)+a)*inv(2*(R*y1+1)))%p
    x3 = ((L**2-3)*inv(R) - 2*x1) % p
    y3 = (L * (x1 - x3) + y_inv(y1)) % p
    return (x3, y3)


def conv2param(x, reverse=False):
    if x is None:
        return None
    if not reverse:
        return (powerXYR(x[0], 1), powerXYR(x[1], 1))
    else:
        return (invXYR(x[0], 1), invXYR(x[1], 1))


def p_double_and_add(n, P):
    result = None
    addend = P
    for bit in bits(n):
        if bit:
            result = addp(result, addend, P)
        addend = doublep(addend)
    return result


def add(P, Q):
    if P is None or Q is None:
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


def calc_b(B):
    return (B*R-a)%p

def findP(prime, points, param=False):
    point_linst = []
    for point in points:
            if not param:
                multiple_for_n = double_and_add(prime, point)
            else:
                multiple_for_n = p_double_and_add(prime, point)

            h = int((len(points)+1)/prime)
            if multiple_for_n==None:
                point_linst.append((point, h),)
    return point_linst[randrange(0, len(point_linst))]


def showResult(a, b, p):
    if not check_ab(a, b):
        print("Bu parametrlar mos tushmaydi(a, b)")
        # return None

    all_points = allPoints(a, b, p, param=False)
    N = all_points[0]+1
    n = min(primes(N))
    print(all_points[1])
    G, h = findP(n, all_points[1], param=False)

    print()
    print(N, " - Nuqtalar soni(N)")
    print(primes(N), " - tub bo'luvchilari(n)")
    print(all_points[1], " - Egri chiziqdagi nuqtalar")
    print(G, " - Ixtiyoriy nuqta")
    print(f"\np={p}\na={a}\nb={b}\nG={G}\nn={n}\nh={h}")
    print("\n\n\n")

    print("===========================")

    all_points = allPoints(a, b, p, param=True)
    Na = randint(1, n-1)
    Nb = randint(1, n-1)
    pG = powerXYR(G, 1)
    print(Na, pG)
    P = p_double_and_add(Na, pG)
    print(P, )
    print(all_points[1], " - Parametrli egri chiziqdagi nuqtalar")
    print("\n\n\n")

    # Pa = p_double_and_add(Na, pG)
    # Pb = p_double_and_add(Nb, pG)
    # Ka = p_double_and_add(Na, Pb)
    # Kb = p_double_and_add(Nb, Pa)
    # print(f"Ka={Ka}\nKb={Kb}")


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
    b = calc_b(B) # 44

    # print(p_double_and_add(2, (57, 116)))
    # print(powerXYR(115, 1), "x")
    # print(powerXYR(4, 2), "y2")
    # print(powerXYR(115, 3), "x3")
    # print(powerXYR(57, 2), "- 57\\2")
    # print(p_double_and_add(5, (115, 4)))

    # print(powerXYR(38, 2), "38p")
    # showResult(a, b, p)
    # print(conv2param(double_and_add(17, (115, 4))))
    # print(p_double_and_add(17, conv2param((115, 4))))
    # print(powerXYR(57, 2))
    # print(inv(57-130))

    Na, Nb = 207, 17
    pG = (115, 4)
    Pa = conv2param(double_and_add(Na, pG))
    Pb = conv2param(double_and_add(Nb, pG))
    print(Pa, Pb)
    Ka = conv2param(double_and_add(Na, conv2param(Pb, reverse=True)))
    Kb = conv2param(double_and_add(Nb, conv2param(Pa, reverse=True)))
    print(f"Ka={Ka}\nKb={Kb}")
