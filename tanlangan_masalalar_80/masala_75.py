
def f(n: int, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        result = 1
    else:
        result = f(n - 2, memo) + f(n - 1, memo)
    memo[n] = result
    return result
