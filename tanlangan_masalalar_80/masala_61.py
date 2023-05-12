
def f61(s: str):
    start = None
    end = None
    for i, e in enumerate(s):
        if (e == "\\") and (start is None):
            start = i
        elif (e == "\\") and (end is None):
            end = i
        elif (end is not None):
            break
        else:
            pass
    if (end is None):
        return "\\"
    return s[(start + 1) : end]

def main():
    s = input("Fayl nomini kiriting: ")
    print("Natija: ", f61(s))

if __name__ == "__main__":
    main()