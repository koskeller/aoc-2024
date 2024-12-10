from utils import nums

with open("day5.input", "r") as file:
    s = file.read().strip()
ans = 0

ordering, updates = s.split("\n\n")

for ln in s.split("\n"):
    ln = nums(ln)


print(ans)
