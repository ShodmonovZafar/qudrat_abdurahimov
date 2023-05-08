
def f(n):
    for i in range(n):
        if 2 ** i < n < 2 ** (i + 1):
            return 2 ** i, n - 2 ** i
        elif 2 ** i <= n < 2 ** (i + 1):
            return 2 ** (i - 1), 2 ** (i - 1)
        else:
            pass


def f78(nums):
    def f(n):
        for i in range(n):
            if 2 ** i < n < 2 ** (i + 1):
                return 2 ** i, n - 2 ** i
            elif 2 ** i <= n < 2 ** (i + 1):
                return 2 ** (i - 1), 2 ** (i - 1)
            else:
                pass
    
    if len(nums) == 1:
        return nums[0]
    else:
        x = f(len(nums))
        return max(f78(nums[:x[0]]), f78(nums[x[1]:]))

def main():
    nums = [10, 2, 9, 3, 1, 8, 7, 3, 4, 5]
    print(f78(nums))

if __name__ == "__main__":
    main()
