from utils import nums

with open("day.input", "r") as file:
    s = file.read().strip()
ans = 0

# grid
# g = [[int(c) for c in r] for r in s.split("\n")]
# g = [list(r) for r in s.split("\n")]
# n,m = len(g),len(g[0])

for ln in s.split("\n"):
    ln = nums(ln)


print(ans)
