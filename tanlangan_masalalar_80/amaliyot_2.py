import random
# [7, 17, 26, 39, 53]
# Boshlanadi: 13:34
# Tugaydi: 15:34
# Tugadi: 15:30

def f7(n):

    def f(n):
        yigindi  = 0
        for i in range(1, n):
            if n % i == 0:
                yigindi += i
        return yigindi
    
    dost_sonlar = []
    for birinchi_son in range(1, n + 1):
        boluvchilari_yigindisi_1 = f(birinchi_son)
        for ikkinchi_son in range(birinchi_son + 1, n + 1):
            boluvchilari_yigindisi_2 = f(ikkinchi_son)
            if birinchi_son == boluvchilari_yigindisi_2 and ikkinchi_son == boluvchilari_yigindisi_1:
                dost_sonlar.append((birinchi_son, ikkinchi_son))
    return dost_sonlar

def f17(nums):
    eng_kichik = None
    for i in nums:
        if i > 0:
            if eng_kichik is None:
                eng_kichik = i
            else:
                eng_kichik = min(eng_kichik, i)
    if eng_kichik is None:
        return 0
    return eng_kichik
    
def f26(a, b):
    while True:
        if a > b:
            a = a - b
        elif b > a:
            b = b - a
        else:
            return a

def f39(m: int, n: int):
    rel = []
    test_baza = list(range(1, m + 1))
    for i in range(n):
        if len(test_baza) == 1:
            rel.append(test_baza[0])
            continue
        element = random.choice(test_baza)
        rel.append(element)
        test_baza.remove(element)
    return rel

def f53(M):
    eng_kichik = None
    indeks = None
    for i in range(len(M)):

        for j in range(len(M[0])):
            if eng_kichik is None:
                eng_kichik = M[i][j]
                indeks = i
            else:
                if eng_kichik > M[i][j]:
                    eng_kichik = M[i][j]
                    indeks = i
    del M[indeks]
    return M

def main():
    pass

if __name__ == "__main__":
    main()
