
def f38(nums: list):
    red = {}
    for e in nums:
        if (e in red):
            red[e] += 1
        else:
            red[e] = 1
    return list(red.keys()), list(red.values())

def main():
    nums1 = input("Massivni kiriting: ")
    nums1 = nums1.split()
    nums = []
    for i in nums1:
        nums.append(int(i))
    a = f38(nums)
    print("Numbers = ", a[0])
    print("Frequency = ", a[1])

if __name__ == "__main__":
    main()
