
def eratosfen_elagi(n):
    asosiy = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (asosiy[p] == True):
            for i in range(p * p, n + 1, p):
                asosiy[i] = False
        p += 1
    rel = []
    for j in range(2, n + 1):
        if asosiy[j]:
            rel.append(j)
    return rel

def tub_kopaytuvchilar(n):
    def eratosfen_elagi(n):
        asosiy = [True for i in range(n + 1)]
        p = 2
        while (p * p <= n):
            if (asosiy[p] == True):
                for i in range(p * p, n + 1, p):
                    asosiy[i] = False
            p += 1
        rel = []
        for j in range(2, n + 1):
            if asosiy[j]:
                rel.append(j)
        return rel
    tub = eratosfen_elagi(n)
    redict = {}
    for i in tub:
        sana = 0
        while True:
            if (n % i == 0):
                n //= i
                sana += 1
            else:
                break
        redict[i] = sana
        if n == 1:
            break
    return redict

def ekub_list(nums):
    def tub_kopaytuvchilar(n):
        def eratosfen_elagi(n):
            asosiy = [True for i in range(n + 1)]
            p = 2
            while (p * p <= n):
                if (asosiy[p] == True):
                    for i in range(p * p, n + 1, p):
                        asosiy[i] = False
                p += 1
            rel = []
            for j in range(2, n + 1):
                if asosiy[j]:
                    rel.append(j)
            return rel
        tub = eratosfen_elagi(n)
        redict = {}
        for i in tub:
            sana = 0
            while True:
                if (n % i == 0):
                    n //= i
                    sana += 1
                else:
                    break
            redict[i] = sana
            if n == 1:
                break
        return redict
    tub_map = []
    for e in nums:
        tub_map.append(tub_kopaytuvchilar(e))
    A = None
    for i, e_dict in enumerate(tub_map):
        if i == 0:
            A = set(e_dict.keys())
        else:
            A &= set(e_dict.keys())
    remap = {}
    for i_set in list(A):
        for i1, i_map in enumerate(tub_map):
            if i1 == 0:
                B = i_map[i_set]
            else:
                B = min(i_map[i_set], B)
        remap[i_set] = B
    s = 1
    for k in remap.items():
        s *= (k[0] ** k[1])
    return s


if __name__ == "__main__":
    l = [24, 16]
    print(ekub_list(l))
