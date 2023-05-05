
def f48(M):
    for i in range(len(M)):
        musbat = 0
        manfiy = 0
        for j in range(len(M[0])):
            if M[i][j] > 0:
                musbat += 1
            elif M[i][j] < 0:
                manfiy += 1
            else:
                pass
        if musbat == manfiy and musbat != 0 and manfiy != 0:
            return i
    return "Bunday satr yo'q"

def main():
    M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f48(M))

if __name__ == "__main__":
    main()