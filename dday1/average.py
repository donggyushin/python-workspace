kor_score = [49, 80, 20, 100, 80]
math_score = [43, 60, 85, 30, 90]
eng_score = [49, 82, 48, 50, 100]
score = [kor_score, math_score, eng_score]
total_score = [0, 0, 0, 0, 0]
for i in range(0, score.__len__()):
    for j in range(0, score[i].__len__()):
        total_score[j] = total_score[j] + score[i][j]

for i in range(0, total_score.__len__()):
    total_score[i] = total_score[i] / 3
sum = 0
for i in total_score:
    sum = sum + i
average = sum / 5
print(average)
