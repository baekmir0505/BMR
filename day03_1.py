# 1번
# 횟수를 입력받아서 그 수만큼 Hello 출력하는 프로그램 만들기
# 5를 입력하면 
# 1번째 hello
# 2번째 hello
# 3번째 hello
# 4번째 hello
# 5번째 hello

# 이건 내가 한거
# i = 1
# while i < 6:
#     print(i,'번째 hello')  
#     i += 1

# count = int(input('횟수를 입력하세여>> '))
# i = 0
# while i < count:
#     i += 1
#     print(i,'번째 hello')

# print('====================================')


# 2번
# 1~100 사이의 7의 배수만 출력하는 프로그램 (while안에서 if를 사용)
# i = 1
# while i < 101:
#     if i % 7 == 0:
#         print(i)
#     i += 1


# print('===================================')




# 3번
# 커피 1잔에 300원, 금액(가진돈)을 입력하여 몇잔의 커피와 잔돈이 얼마가 남는지 출력
# == 출력 예==
#금액은 얼마인가요>> 1400원
#커피 1잔, 잔돈 1100원
#커피 2잔, 잔돈 800원
#커피 3잔, 잔돈 500원
#커피 4잔, 잔돈 2000원


# price = 300
# 금액 = int(input('금액을 입력해주세요>>'))
# 커피잔수 = 0

# # 저번에는 횟수로서 i = 0, 현재는 범위로써 금액 >= pirce
# while 금액 >= price:
#     금액 -= price
#     커피잔수 += 1
#     print('커피',커피잔수,'잔, 잔돈',금액,'원')

# ============================================================================
# 자료형/변수
'''
변수(variable) : 저장공간
    - 대입연산자를 사용 (=)
    - 사용이유 : 자주 변경될 것 같은 혹은 자주 사용될 것 같은 값은 미리 저중해둬서 관리한다.
    - 변수에 있는 값만 수정하면 변수를 사용한 코드는 일괄 수정이 가능해진다.
    - 변수명1 = '값'
    - 변수명1 이라는 공간이 생성되면서(재활용되면서) '값' 이라는 데이터가 들어간다.

자료형(type) : 데이터의 타입
    - srt, int, float
    - 컴파일러 오류검출, 실수 검출, 의도명확화
    - 뺄셈으로 사용하고자 하는지, 핸드폰 번호로 사용하고자 하는지 컴퓨터는 알 수 없음 그래서 자료형을 부여하여 구분한다.
    - 파이썬에서 제공해주는 기능(함수)를 잘 못 사용했을 때 오류로 검출
    - str :문자열(글자), int : 정수(숫자), float : 실수(소수점 있는 숫자)
    - 변수의 타입은 데이터의 타입과 일치해야만 저장이 가능하다.
    - 자료형 변환 
        (1) '33-4', = 를 숫자로 바꾸려면 ==>  int('33-4')   ==> 29
        (2) 변환하고자 하는 자료형으로 감싸준다, float(정수 변수) 
        (3) '나는 문자열이지'  ==> int('나는 문자열이지') ==> 컴파일 오류, 그래서(아래 이어짐)
        (4) 데이터가 맞아야지만 타입 변환이 가능
'''
변수1 = 123
변수2 = '문자열'
int(변수1)
# int(변수2)          # 변환하고자 하는 자료형과 호환 가능한 값만 변환가능

# 출력/입력
print('안녕')
print(3.14)   # 숫자는'' 사용없이 가능
print(변수2)    # 변수 사용
print('안녕',변수2)
print('안녕{},{}'.format(변수2,변수1,314))
print(f'안녕 {변수2},{변수1},{314}')

# 조건문/반복문
'''
if 조건식 : 
    조건식이 Ture 일때만 실행할 문장1
    조건식이 Ture 일때만 실행할 문장2
if조건문은 실행후에 밑으로 내려오지만

while 조건식 : 
    조건식이 Ture 일때만 실행할 문장1
    조건식이 Ture 일때만 실행할 문장2    
반복문은 실행되면 다시 위로 올라감(while부분으로 올라가서 조건식 검사부터 다시한다.)
'''
# if ~ elif ~ else
i = 3
if i == 3:
    print('조건이 맞네요')
    print('조건이 맞으면 이 문장은 실행이 됩니다')
print('조건문이 끝났습니다')

#while (반복문은 설계가 필요함)
i = 0
while i < 3:
    print('반복문이 실행됩니다.')
    print('조건이 맞는 동안에는 이 문장이 실행되겠네요', i)
    i +=1
print('반복문이 끝났습니다.')







