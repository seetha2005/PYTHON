
input1 = int(input("Enter first 4-digit num1 "))
input2 = int(input("Enter second 4-digit num2 "))
input3 = int(input("Enter third 4-digit num3 "))

digits1 = [int(d) for d in str(input1)]
digits2 = [int(d) for d in str(input2)]
digits3 = [int(d) for d in str(input3)]

max_sum = max(digits1) + max(digits2) + max(digits3)

min_sum = min(digits1) + min(digits2) + min(digits3)

key = max_sum * min_sum

print("Key =", key)