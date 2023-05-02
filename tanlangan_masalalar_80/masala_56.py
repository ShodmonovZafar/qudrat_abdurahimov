s = "Assalomu alaykum"
s1 = "Assalomu alaykum aziz do'stlar"

def f(s: str) -> tuple:
    l = s.split()
    min_uzunlik = None
    soz = None
    for i in l:
        if min_uzunlik is None:
            min_uzunlik = len(i)
            soz = i
        else:
            if min_uzunlik > len(i):
                min_uzunlik = len(i)
                soz = i
            else:
                pass
        
    return soz, min_uzunlik

print(f(s1))