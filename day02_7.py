# '반복문 실행' 5번만 해주고 싶다
# print('반복문 실행')
# print('반복문 실행')
# print('반복문 실행')
# print('반복문 실행')
# print('반복문 실행')


기준점 = 0          # 보통 기준점을 i로 표현함
while 기준점 < 5:
    print('반복문 실행')
    기준점 += 1
print('while 종료')

# 1 자신의 이름을 변수에 담고 반복문을 통해서 10번 출력해 보세요
i = 0
name ='백미르'
while i < 10:
    print(name)
    i +=1

i = 0
name ='백미르'
while i < 10:
    print(name, i,'번')
    i +=1




# 초기값(기준점)이 반드시 0일 필요는 없음
# 증감량이 반드시 += 1일 필요도 없음
# 1~12월

i = 1
while i < 13:
    print(i,'월')
    i += 1

#역순으로 
print('===============')

i = 12
while i > 0:
    print(i,'월')
    i -= 1





