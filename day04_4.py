# 문자열을 저장하는 리스트
let = ['아메리카노','라떼','스무디','에스프레소']
num =0
# 사용자에게 입력을 받아 리스트를 구성
# 1: 추가하기, 2: 수정하기, 3; 삭제하기, 4: 전체보기
while True:
    num = int(input('1:추가, 2:수정, 3:삭제, 4:조회'))
    if num == 1:
        변수1 = input('추가할 값을 입력하세요>> ')
        let.append(변수1)              # 추가할 값을 입력
    elif num == 2:
        변수3 = input('수정하고자 하는 값을 입력하세요>> ')
        변수4 = let.index(변수3)
        변수2 = input('수정할 값을 입력해주세요>> ')
        let[변수4] = 변수2             # 값을 수정 (수정하고자나느 값, 수정할 값)
    elif num == 3:
        변수5 = input('삭제할 값을 입력하세요>> ')
        let.remove(변수5)                  # 삭제할 값 입력
    elif num == 4:           
        for i in let:
            print(i)                   # 전체조회
    elif num == 0:
        print('프로그램 종료')
        break                  # 프로그램 종료
    else:
        print('없는 번호입니다.')

