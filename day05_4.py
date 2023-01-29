# 3개더하기, 빼기, 곱하기, 나누기
# +, - *, / : 보통 2개만 할 수 있음

def 더하기(num1, num2, num3):
    print(num1+num2+num3)

print(1+2)
더하기(1,2,3)

# 빼기, 곱하기, 나누기

def 빼기(num1, num2, num3):
    print(num1-num2-num3)

빼기(10,5,2)

def 곱하기(num1, num2, num3):
    print(num1*num2*num3)

곱하기(10,5,8)

def 나누기(num1, num2, num3):
    print(int(num1/num2/num3))

나누기(20,2,5)

def 절대값더하기(a, b):
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    print(a+b)

절대값더하기(3, 7)
절대값더하기(-4, 3)