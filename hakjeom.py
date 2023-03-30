gpa_sum = 0
gpa_f = 0
score_sum = 0
while True:
    print('작업을 선택하세요.\n1. 입력\n2. 계산')
    n = int(input())
    if n == 1:
        print("학점을 입력하세요:")
        gpa = int(input())
        print("평점을 입력하세요:")
        sco = input()
        score = 0 
        if sco !="F": 
            score = 69-ord(sco[0]) if len(sco) == 1 else 69-ord(sco[0])+0.5 
            gpa_sum += gpa
            score_sum += gpa*score
        else:
            gpa_f += gpa   
        print("입력되었습니다.\n")

    else:
        print(f'제출용: {gpa_sum}학점(GPA: {score_sum/gpa_sum})\n열람용: {gpa_sum+gpa_f}학점(GPA: {score_sum/(gpa_sum+gpa_f)})\n')
        print('프로그램을 종료합니다.')
        break