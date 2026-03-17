a = input("Enter string: ")
result = ""
count = 1

for i in range(len(a)):
    if i + 1 < len(a) and a[i] == a[i + 1]:
        count += 1
    else:
        result += a[i] + str(count)
        count = 1

print(result)
