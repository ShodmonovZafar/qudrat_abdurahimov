
def f(s: str) -> str:
    l = s.split(".")
    return l[-1]

s = "D:\A\B\data.py"
print(f(s))