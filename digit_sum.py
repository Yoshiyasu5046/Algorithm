def digit_sum(n):
    n = str(n)
    total = 0
    for c in n:
        total += int(c)
    return total