# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
# 1
total_score = 0
for subject_score in score.values():
  total_score += subject_score
result = total_score / len(score)
print(result)


# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    '민승': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    '건희': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
# 2
total_score = 0 # 점수 총계
length = 0      # 더한 과목 수
for student_score in scores.values():
  # print(student_score)
  for subject_score in student_score.values():
    total_score += subject_score
    length += 1
print(total_score / length)


# 3. 도시별 최근 3일의 온도입니다.
cities = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
'''
출력 예시)
서울 : 평균온도
대전 : 평균온도
광주 : 평균온도
부산 : 평균온도
'''

for city, temp in cities.items():
  print(f'{city} : {sum(temp) / len(temp)}')


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
count = 0
cold = 0
hot = 0
cold_city = ''
hot_city = ''
for city_name, temp in cities.items():
  # 첫번째 도시를 기준점으로 세팅
  if count == 0:
    cold = min(temp)
    hot = max(temp)
    cold_city = city_name
    hot_city = city_name
  else:
    # 도시의 최저기온을 비교해서 업데이트
    if min(temp) < cold:
      cold = min(temp)
      cold_city = city_name

    # 도시의 최고기온을 비교해서 업데이트
    if max(temp) > hot:
      hot = max(temp)
      hot_city = city_name

    count += 1
print(cold_city)
print(hot_city)




# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')

if 2 in cities['서울']:
  print('네')
else:
  print('아니요')