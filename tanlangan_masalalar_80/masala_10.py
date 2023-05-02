
def f(a, b):

    while True:
        if a > b:
            if (a % b) == 0:
                return b
            else:
                a %= b
        elif b > a:
            if (b % a) == 0:
                return a
            else:
                b %= a
        else:
            return a
        
print(f(17, 37))