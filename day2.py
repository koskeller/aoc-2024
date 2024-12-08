from utils import nums
from itertools import pairwise

with open("day2.input", "r") as file:
    s = file.read().strip()
ans = 0


for ln in s.split("\n"):
    for r in range(len(ln)):
        vals = nums(ln)
        if all(a < b for a, b in pairwise(vals[:r] + vals[r + 1 :])) or all(
            a > b for a, b in pairwise(vals[:r] + vals[r + 1 :])
        ):
            if all(1 <= abs(a - b) <= 3 for a, b in pairwise(vals[:r] + vals[r + 1 :])):
                ans += 1
                break

print(ans)
