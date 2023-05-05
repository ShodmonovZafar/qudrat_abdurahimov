
def f46(M):
    rel = []
    for i in range(len(M)):
        s = 0
        for j in range(len(M[0])):
            s += M[i][j]
        rel.append(s)
    return rel

def main():
    M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f46(M))

if __name__ == "__main__":
    main()