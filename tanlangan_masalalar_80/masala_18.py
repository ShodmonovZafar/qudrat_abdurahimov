nums = [1, 2, 3, 4, 5, 1, 3, 2, 5]

def f(nums: list[int]) -> tuple or 0:
    max_element = None
    indeks = None
    for i, e in enumerate(nums):
        # e = +1 2 3 4 5 1 3 2 5
        # i = +0 1 2 3 4 5 6 7 8
        if not (e % 2 == 0): # e toq son
            if max_element is None: # max_element is None
                max_element = e
                indeks = i
            else:
                if max_element < e:
                    max_element = e
                    indeks = i
                else: # max_element >= e
                    pass
        else: # e juft son
            pass
    if max_element is None:
        return 0
    return max_element, indeks + 1

nums1 = [7, 8, 5, 1, 9, 4, 6, 2, 9]
nums2 = [6, 8, 50, 2, 90, 4, 6, 90, 10, 10]
print(f(nums2))