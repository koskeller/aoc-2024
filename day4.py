with open("day4.input", "r") as file:
    s = file.read().strip()
ans = 0

g = [list(r) for r in s.split("\n")]
height, width = len(g), len(g[0])

for y in range(1, height - 1):
    for x in range(1, width - 1):
        if not g[y][x] == "A":
            continue
        if (
            (g[y - 1][x - 1] == "M" and g[y + 1][x + 1] == "S")
            or (g[y - 1][x - 1] == "S" and g[y + 1][x + 1] == "M")
        ) and (
            (g[y - 1][x + 1] == "M" and g[y + 1][x - 1] == "S")
            or (g[y - 1][x + 1] == "S" and g[y + 1][x - 1] == "M")
        ):
            ans += 1


print(ans)
