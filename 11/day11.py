from functools import lru_cache

lines = list(map(str.strip, [*open("day11.txt")]))

fromTo = {}

for i in lines:
    _from, _to = i.split(": ")
    _to = _to.split(" ")
    fromTo[_from] = _to

@lru_cache(None)
def findPaths(start: str, fft: bool, dac: bool):
    if start == "fft": fft = True
    if start == "dac": dac = True

    if "out" in fromTo.get(start, []) and fft and dac:
        return 1

    return sum(findPaths(i, fft, dac) for i in fromTo.get(start, []))

print(findPaths("you", True, True))
print(findPaths("svr", False, False))