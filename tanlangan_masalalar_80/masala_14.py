
def f14(nums: list[int]):
    eng_kichik = nums[0] 
    eng_katta = nums[0]
    eng_kichik_index = 0
    eng_katta_index = 0
    for i, e in enumerate(nums):
        if i == 0:
            continue
        if eng_kichik > e:
            eng_kichik = e
            eng_kichik_index = i
        else:
            pass
        if eng_katta <= e:
            eng_katta = e
            eng_katta_index = i
        else:
            pass
    return [(eng_kichik, eng_kichik_index), (eng_katta, eng_katta_index)]

def main():
    n = int(input("n ni kiriting: "))
    x = input("Elementlarni kiriting: ").split()
    nums = []
    for i in x:
        nums.append(int(i))
    natija = f14(nums)
    print(natija[0][0], natija[0][1] +1, ";", natija[1][0], natija[1][1] + 1)

if __name__ == "__main__":
    main()