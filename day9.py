with open("day9.input", "r") as file:
    s = file.read().strip()
ans = 0


def is_file(number):
    return number % 2 == 0


def get_length(arr: list[int], value: int, index: int) -> int:
    length = 0
    while index >= 0 and arr[index] == value:
        length += 1
        index -= 1
    return length


blocks = [int(n) for n in s]
a = []

for i in range(len(blocks)):
    for n in range(blocks[i]):
        if i % 2:
            a.append(-1)
        else:
            a.append(i // 2)

moved_files = set()

i = len(a) - 1
file_id = -1
file_len = 0
while i >= 10:
    if a[i] == -1:
        i -= 1
        continue

    # We found a file
    file_id = a[i]
    file_len = get_length(a, file_id, i)
    # Update index to the next block
    i -= file_len
    if file_id in moved_files:
        continue
    moved_files.add(file_id)

    # Find a spot
    for n in range(0, i - file_len + 2):
        if a[n] != -1:
            continue

        if all(x == -1 for x in a[n : n + file_len]):
            # Found spot
            a[n : n + file_len] = [file_id] * file_len
            a[i + 1 : i + 1 + file_len] = [-1] * file_len
            break

for i in range(len(a)):
    if a[i] == -1:
        continue
    ans += i * a[i]

print(ans)
