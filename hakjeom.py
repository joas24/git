
grade = []
while True:
    print('작업을 선택하세요.\n1. 입력\n2. 계산')
    n = int(input())
    if n == 1:
        print("학점을 입력하세요:")
        gpa = int(input())
        print("평점을 입력하세요:")
        sco = input()
        score = 0 
        if sco !="F": score = 69-ord(sco[0]) if len(sco) == 1 else 69-ord(sco[0])+0.5 
        grade.append([gpa,score]) 
        print("입력되었습니다.")
    else:
        num_submit = 0
        num_view = 0
        gpa_submit = 0
        gpa_view = 0
        for i in range(len(grade)):
            if grade[i][1] != 0:
                num_submit += grade[i][0]
                gpa_submit += grade[i][0]*grade[i][1]
            num_view += grade[i][0]
            gpa_view += grade[i][0]*grade[i][1]
        print(f'제출용: {num_submit}학점(GPA: {gpa_submit/num_submit})\n열람용: {num_view}학점(GPA: {gpa_view/num_view})\n')
        print('프로그램을 종료합니다.')
        break