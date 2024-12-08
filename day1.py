from utils import nums
from collections import Counter

with open("day1.input", "r") as file:
    s = file.read().strip()

left = []
right = []

for ln in s.split("\n"):
    ln = nums(ln)
    left.append(ln[0])
    right.append(ln[1])

right = Counter(right)
a = 0

for ln in left:
    a += right[ln] * ln

print(a)
