HongGilDongScore = {'kor': 80, 'eng': 75, 'math': 55}
HongGilDongTotalScore = 0
for k in HongGilDongScore:
    HongGilDongTotalScore += HongGilDongScore[k]
HongGilDongAverage = HongGilDongTotalScore / HongGilDongScore.__len__()
print(HongGilDongAverage)
