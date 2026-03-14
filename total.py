s= input()
values = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

total = 0

for ch in s:
    total = total + values[ch]

print(total)

