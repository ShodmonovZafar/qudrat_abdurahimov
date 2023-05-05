
def f44(M):
    for i in range(len(M)):
        if i % 2 != 0:
            M[i].reverse()
    return M
    
def main():
    M = [[1,2,3],
         [4,5,6],
         [7,8,9],
         [10,11,12]]
    print(f44(M))

if __name__ == "__main__":
    main()