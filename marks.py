name=['GILL','ABI','RAHUL','JOHN','ANU']
marks=[[30,40,50],[67,88,90],[90,76,72],[90,76,67],[80,70,60]]

for i in range(len(name)):
    total = sum(marks[i])
    percentage = total / 3

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "B"
    else:
        grade = "F"

    print(name[i], "Percentage:", percentage, "Grade:", grade)