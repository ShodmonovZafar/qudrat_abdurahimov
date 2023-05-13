
def f(dic: dict):
    print(type(dic.items()))
    pass

def main():
    dic = {
        1 : "a",
        2 : "b",
        3 : "c"
    }
    f(dic)

if __name__ == "__main__":
    main()