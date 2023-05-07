
def sieve_of_eratosthenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    return prime

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


def main():
    print(eratosfen_elagi(80))

if __name__ == "__main__":
    main()