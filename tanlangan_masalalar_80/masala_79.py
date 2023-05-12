
def f79(s: str):
    # s = "Agent 007"
    raqamlar = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    def f(n):
        for i in range(n):
            if 2 ** i < n < 2 ** (i + 1):
                return 2 ** i, n - 2 ** i
            elif 2 ** i <= n < 2 ** (i + 1):
                return 2 ** (i - 1), 2 ** (i - 1)
            else:
                pass

    if len(s) == 1:
        if s in raqamlar:
            return 1
        else:
            return 0
    else:
        x = f(len(s))
        return int(f79(s[:x[0]])) + int(f79(s[x[1]:]))

def main():
    s = "agent 007"
    print(f79(s))

if __name__ == "__main__":
    main()
