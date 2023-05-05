
def f45(M):
    kesuvchi = len(M)
    rel = []
    for i in range(len(M)):
        A = []
        for j in range(len(M)):
            
            if j < kesuvchi:
                A.append(M[i][j])
            else:
                break
        rel.append(A)
        
        kesuvchi -= 1
    kesuvchi = 0
    for i in range(len(M) - 1, 0, -1):
        
        for j in range(len(M)):
            if kesuvchi < j:
                rel[(len(M) - 1) - i].append(M[j][i])
        kesuvchi += 1
    return rel

def main():
    M = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    f45(M)

if __name__ == "__main__":
    main()