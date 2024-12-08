from utils import nums
import re

with open("day3.input", "r") as file:
    s = file.read().strip()
ans = 0

r = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"

do = True
for n in re.findall(r, s):
    if n == "do()":
        do = True
    elif n == "don't()":
        do = False
    else:
        if do:
            a, b = nums(n)
            ans += a * b


print(ans)
