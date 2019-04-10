sum_score = 0
honggildong_s_score = {
    "kor": 80,
    "eng": 75,
    "math": 55
}
for k in honggildong_s_score:
    sum_score += honggildong_s_score[k]
average = round(float(sum_score/honggildong_s_score.__len__()), 1)
print(average)
