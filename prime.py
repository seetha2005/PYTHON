num = int(input("Enter any number: "))

print("Prime factors of", num, "are:")

i = 2
while i <= num:
    if num % i == 0:
        print(i)
        num = num // i
    else:
        i += 1