
def f(nums: list[int]) -> tuple or 0:
    max_element = None
    indeks = None
    for i, e in enumerate(nums):
        if not (e % 2 == 0):
            if max_element is None:
                max_element = e
                indeks = i
            else:
                if max_element < e:
                    max_element = e
                    indeks = i
    if max_element is None:
        return 0
    return max_element, indeks + 1
