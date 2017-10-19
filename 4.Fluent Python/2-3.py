symbols = '$&&^%$aa'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 70]
print beyond_ascii

beyond_ascii2 = list(filter(lambda c: c > 70, map(ord, symbols)))
print beyond_ascii2