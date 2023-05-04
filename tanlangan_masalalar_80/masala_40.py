
def bubble_sort(nums: list[int]):
    for j in range(len(nums) - 1):
        for i in range(0, len(nums) - j - 1):
            if nums[i] > nums[i + 1]:
                vaqt = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = vaqt
    return nums

def main():
    # nums = [4, 6, 2, 1, 7]
    # nums = [10, 2, 9, 3, 1, 8, 7, 3, 4, 5]
    nums = [-2, 45, 0, 11, -9]
    print(bubble_sort(nums))

if __name__ == "__main__":
    main()