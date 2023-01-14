# 반복문 (while, for)

# for를 사용해서 hello 3번하기
for 임시변수 in range(3):
    print('hello')


# 임시변수 : while에서 i를 값으로 사용했지만 for에서는 임시변수로 사용 
i = 0
while i < 3:
    print(i,'번째 Hello')
    i += 1

for j in range(3):
    print(j,'번쨰 Hello')

print('=======================================================================')

# i = 1
for i in range(1, 4):
    print(i,'번째 Hello')

print('=======================================================================')

# range(3) == range(0, 3)      # 0부터 2까지 (0~2)
# range(1, 4) == 1부터 4전까지(1~3)

# 1월~12월 출력
for m in range(1,13):
    print(m,'월')

for m in range(12):
    print((m+1),'월')

for i in range(1, 101):
    if i % 7 == 0:
        print(i)

for i in range(7, 101, 7):
    print(i)

# 짝수만 출력하기
for j in range(0, 11, 2):
    print(j)

print('======================================================================')

# 문제1
# '''
# 5
# 4
# 3
# 2
# 1
# '''

# 1.
for n in reversed(range(1, 6)):
    print(n)
# 2.
num = 5
for n in range(5):
    print(num)
    num -= 1
# 3.
for n in range(5, 0, -1):
    print(n)

print('===================================================')

# 문제2
'''
양의 정수 1개를 입력받아서 
1부터 입력한 숫자까지 합계를 알려주는 프로그램

ex) 10
1~10을 모두 더해서 55
ex) 1~9
1~9를 모두 더해서 45

'''
count = int(input('양의 정수를 입력하세요>> '))
sum = 0
for n in range(1, count+1):
    sum += n
print(sum)

print('=======================================================')

# 문제 3
num1 = 1
num2 = 2
backup = 0
backup = num1
num1 = num2
num2 = backup
print(num1, num2) 









