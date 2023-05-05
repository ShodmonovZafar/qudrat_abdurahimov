
def f73(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return f73(n - 2) * n

def main():
    print(f73(6))

if __name__ == "__main__":
    main()