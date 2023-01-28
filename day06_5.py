# return : 함수의 결과를 활용할 수 있게 해준다
# def 절대값더하기(a, b):
#     if a < 0:
#         a *= -1
#     if b < 0:
#         b *= -1
#     return a+b          # return 옆에 있는 값이 사용한 곳으로 전달

# 결과1 = 절대값더하기(3, 7)         #10
# 결과2 = 절대값더하기(-4, 결과1)        #7
# print(결과2)
# print(절대값더하기(-1,-1))

# 문제1
lst = [10,20,30,40,50]

def 총합(a_lst):
    변수1 = 0        # 함수 안에서 만든 변수는 함수가 끝나면 사라진다(지역변수),(안에서는 가능 함수 밖으로 나가면 인식하지 못함)
    for i in a_lst:
        변수1 += i
    return 변수1


   


# sum = 총합(lst)
# avg = sum / len(lst)

# print('총합은',sum)
# print('평균은',avg)

# # 문제2 입력한 갯수만큼 *를 표시하는 함수
# num = int(input('별의 갯수를 입력해주세요>> '))
# def star(num1,num2):
#     print(num1*num2)
# star(num,'*')
    
print('================================================================')

def star(num=1):
    result = ''
    for i in range(num):
        result += '*'
    return result

num = int(input('별의 갯수를 입력해주세요>> '))
'''
실행 예)
별의 개수를 입력하세요>>> 
***

힌틔) 문자열은 더하면 합쳐집니다.
'''
