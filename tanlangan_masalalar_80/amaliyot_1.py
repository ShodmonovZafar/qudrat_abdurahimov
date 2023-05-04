
# masalalar = [6, 18, 40, 47, 73]


def f6(n):
    asosiy = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if asosiy[p]:
            for i in range(p * p, n + 1, p):
                asosiy[i] = False
        p += 1
    rel = []
    for i in range(2, n + 1):
        if asosiy[i]:
            rel.append(i)
    return rel

def f18(nums):
    eng_katta = None
    index = None
    for i, e in enumerate(nums):
        if e % 2 != 0:
            if eng_katta != None:
                if eng_katta < e:
                    eng_katta = e
                    index = i
            else:
                eng_katta = e
                index = i
    if eng_katta == None:
        return 0
    return eng_katta, index + 1

def f40(nums):
    for i in range(len(nums) - 1):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                vaqt = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = vaqt
    return nums

def f47(M):
    rel = []
    for j in range(len(M[0])):
        s = 1
        for i in range(len(M)):
            s *= M[i][j]
        rel.append(s)
    return rel

def f73(n):
    p = 1
    for i in range(n, 0, -2):
        p *= i
    return p

def main():
    pass

if __name__ == "__main__":
    main()