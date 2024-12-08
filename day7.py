with open("day7.input", "r") as file:
    s = file.read().strip()

lines = s.split("\n")

a = 0
for ln in lines:
    parts = ln.split(" ")
    value = int(parts[0][:-1])
    nums = [int(num) for num in parts[1:]]
    print(value, nums)

print(a)
