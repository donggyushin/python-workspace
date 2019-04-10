korean_score = [49, 80, 20, 100, 80]
math_score = [43, 60, 85, 30, 90]
eng_score = [49, 82, 48, 50, 100]
score = [korean_score, math_score, eng_score]
total_score = [0, 0, 0, 0, 0]
average = [0, 0, 0, 0, 0]
for i in range(score.__len__()):
    for j in range(score[i].__len__()):
        total_score[j] += score[i][j]
for i in range(score[0].__len__()):
    average[i] = total_score[i]/3
print(average)
