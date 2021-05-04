import random


def rand_a(n):
    global a
    a = 2 + random.randint(1, n - 4)


def isPrime(n, t, k, recursive):
    global a

    # check is not less than 4 and not 0 or negative
    if (n <= 1 or n == 4):
        return (n-1, n, "Murakkab son", "Tanlanmadi")  # non prime
    if (n <= 3):
        return (n-1, n, "Tub son", "Tanlanmadi")  # prime

    # count 2
    r = n - 1
    s = 0
    while (r % 2 == 0):
        r //= 2
        s += 1

    # set a rand
    rand_a(n)

    for i in range(t):
        if a < 2 or a >= n-1:
            rand_a(n)
            continue

    # 1) first condition
        y = pow(a, r, n)
        if (y == 1 or y == n-1):
            rand_a(n)
            continue

        cont = False
    # 2) iters untill s-1
        for j in range(1, s):
            y = (y * y) % n
            if (y == 1):
                return (r, n, "Murakkab son", a)
            if (y == n - 1):
                if recursive:
                    jj = 1
                    D = a
                    while D != n-1 and jj < k:
                        D = (D+(D+1)*(a+jj)) % n
                        jj += 1
                    a = D
                else:
                    pass
                cont = True
                break
        if cont:
            continue
        else:
            return (r, n, "Murakkab son", a)
    return (r, n, "Tub son", a)

# export isPrime funtions
import sys
sys.modules[__name__] = isPrime
