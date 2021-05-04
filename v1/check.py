def inv(n):
    for i in range(37):
        if (n * i) % 37 == 1:
            return i
    return 1

print(inv(-5), pow(-5, 37-2, 37))