print('작업을 선택하세요.\n1. 입력\n2. 계산')
n = int(input())
while True:
    if n == 1:
        print("학점을 입력하세요:")
        ha = int(input())
        print("평점을 입력하세요:")
        pyo = input()
        print("입력되었습니다.")
    else:
        a = '3'
        print(f'제출용: {a}학점(GPA: {a})\n열람용: {a}학점(GPA: {a})\n')
        print('프로그램을 종료합니다.')
        break