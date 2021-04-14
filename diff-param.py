from random import getrandbits
from random import randint, randrange


# teskari modulni hisoblash
def inv(n):
    for i in range(p):
        if (n * i) % p == 1:
            return i
    return 1


# teskari modulni hisoblash
def inv_p(n, p):
    for i in range(p):
        if (n * i) % p == 1:
            return i
    return 1


def a_inv(a, R, p):
    return (-a*(1+R*a)-1)%р


def aRb(a, b, R):
    return a+b*(1+R*a)%p


def a2(a, R):
    return (a*(2+R*a))%p


def bits(n):
    result = []
    while n:
        result.append(n & 1)
        n >>= 1
    return result


def powerR(n, a, R):
    a_start = a
    c = 0
    addList = []

    for bit in bits(n):
        if bit==0 and c!=0:
            c += 1
            continue

        for times in range(c):
            a = a2(a, R)
        addList.append(a)
        c += 1
        a = a_start

    a_mul = 1
    for i in range(len(addList)-1):

        if i!=0:
            a_mul = aRb(a_mul, addList[i+1], R)
        else:
            a_mul = aRb(addList[i], addList[i+1], R)

    return a_mul%p


def y(x, R):
    """ xa, xb va Ra,Rb uchun o'rinli """
    return powerR(x, a*inv(R), R)%p


def Rab():
    return (Ra*Rb)%p


def k(Rab, k_type = 'a'):
    """ ka, kb uchun o'rinli """
    if k_type=='a':
        return powerR(xa, y(xb, Rb)*inv(Ra), Rab)%p
    elif k_type=='b':
        return powerR(xb, y(xa, Ra)*inv(Rb), Rab)%p


def K(k):
    """k = k(xa, Ra)  yoki k(xb, Rb) """
    return k+((((((y(xa, Ra)*y(xb, Rb)*inv(a)-k))*inv_p(p, (Ra*Rb)))))*p)%(p*Ra*Rb)


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


if __name__ == "__main__":
    a, p, q = (9, 107, 53)
    q_list = primes(p-1)
    q = q_list[randrange(0, len(q_list))]
    # q > 2^163
    # powerR(q, a, 1)==0 -> a

    print("q", q)

    Ra, Rb = (3, 5) # ikkala tomondan olinadi
    xa, xb = (13, 27) # ikkala tomondan olinadi

    print("Ra", Ra)
    print("Rb", Rb)
    print("Rb*a", (inv(Ra)*a)%p)
    print("Rb*a", (inv(Rb)*a)%p)
    print("ya", y(xa, Ra))
    print("yb", y(xb, Rb))
    print("Ra-1*yb", (inv(Ra)*y(xb, Rb))%p)
    print("Rb-1*ya", (inv(Rb)*y(xa, Ra)%p))
    print("Rab", Rab())
    print("ka", k(Rab(), 'a'))
    print("kb", k(Rab(), 'b'))

    print("Ka", K(k(Rab(), 'a')))
    print("Kb", K(k(Rab(), 'b')))
