from itertools import combinations
from typing import Set, Tuple
import re

with open("day8.input", "r") as file:
    s = file.read().strip()
ans = 0

g = [list(r) for r in s.split("\n")]
height, width = len(g), len(g[0])


def check(coord: Tuple[int, int]) -> bool:
    y, x = coord
    return 0 <= y < height and 0 <= x < width


r = r"[a-zA-z0-9]"
uniq: Set[str] = set(re.findall(r, s))

nodes = set()

for a in uniq:
    pos: list[Tuple[int, int]] = []
    for y in range(height):
        for x in range(width):
            if g[y][x] == a:
                pos.append((y, x))

    pairs = list(combinations(pos, 2))

    for (ay, ax), (by, bx) in pairs:
        node_a = (ay, ax)
        for i in range(height):
            node_a = (node_a[0] - (ay - by), node_a[1] - (ax - bx))
            if check(node_a) and node_a not in nodes:
                ans += 1
                nodes.add(node_a)

        node_b = (by, bx)
        for i in range(width):
            node_b = (node_b[0] - (by - ay), node_b[1] - (bx - ax))
            if check(node_b) and node_b not in nodes:
                ans += 1
                nodes.add(node_b)

print(ans)
