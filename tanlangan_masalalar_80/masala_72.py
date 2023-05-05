
def f72(n):
    if n == 1 or n == 0:
        return 1
    else:
        return f72(n - 1) * n

def main():
    print(f72(5))

if __name__ == "__main__":
    main()