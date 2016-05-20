def is_int(x):
    try:
        return x % 1 == 0
    except:
        return False