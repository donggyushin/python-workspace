# What's the average score of class A?
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in A:
    sum += i
average = sum / A.__len__()
print(average)
