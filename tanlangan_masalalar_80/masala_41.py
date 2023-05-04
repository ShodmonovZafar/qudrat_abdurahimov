
def selection_sort(nums: list[int]):
    for i in range(len(nums) - 1):
        eng_kichik = nums[i]
        index = i
        for j in range(i + 1, len(nums)):
            if eng_kichik > nums[j]:
                eng_kichik = nums[j]
                index = j
        nums[index] = nums[i]
        nums[i] = eng_kichik
    return nums

def main():
    # nums = [4, 3, 2, 1]
    nums = [4, 6, 2, 1, 7]
    print(selection_sort(nums))


if __name__ == "__main__":
    main()
