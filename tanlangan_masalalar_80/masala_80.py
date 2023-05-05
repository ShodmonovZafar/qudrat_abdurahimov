
def f80(s):
    if len(s) == 3:
        return s[0] == s[2]
    elif len(s) == 2:
        return s[0] == s[1]
    else:
        if f80(s[1:-1]):
            return True
        else:
            False

def main():
    s = "abclkhjhba"
    print(f80(s))

if __name__ == "__main__":
    main()