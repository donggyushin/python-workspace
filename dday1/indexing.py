colors = ['red', 'blue', 'green']
print(colors[0])
print(colors[2])
print(len(colors))

cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
print(cities[0:6])
print(cities[6:])
print(cities[::2])
print(cities[::-1])


colors.extend(['black', 'purple'])
print(colors)

colors.insert(0, 'orange')
print(colors)

colors.remove('red')
print(colors)
del colors[0]
print(colors)

t = [1, 2, 3]
a, b, c = t
print(t, a, b, c)

kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
mid_score = [kor_score, math_score, eng_score]
print(mid_score)
