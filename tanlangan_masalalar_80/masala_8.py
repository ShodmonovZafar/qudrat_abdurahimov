
def f8(summa: float | int, foiz: int) -> tuple:
    foiz = 1 + foiz * (1/100)
    oy = 0
    summa_2 = summa * 2
    while not (summa_2 < summa):
        oy += 1
        summa *= foiz
    return oy, summa

def main():
    summa = float(input("Boshlang'ich summani kiriting: "))
    foiz = int(input("Foizni kiriting: "))
    x = f8(summa, foiz)
    print("Natija: ", "{} oyda {} so'm".format(x[0], x[1]))

if __name__ == "__main__":
    main()