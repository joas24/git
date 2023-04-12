import random
sbjs = {}
score = []
score_re = []
def gradeToNum(grade):
    if grade[0] == 'F': return 0
    if len(grade)==2: return 69-ord(grade[0])+0.5  
    else: return 69-ord(grade)

while True:
    print("작업을 선택하세요.\n1. 입력\n2. 출력\n3. 계산")
    choice = int(input())
    match choice:
        case 1:
            print("과목명을 입력하세요:")
            sbj_name = input()
            print("학점을 입력하세요:")
            sbj_gpa = int(input())
            print("평점을 입력하세요:")
            sbj_grade = input()

            if sbj_name in sbjs.values():
                score_re.append((n,sbj_gpa,sbj_grade))
            else: 
                n = random.randrange(10000,100000)
                sbjs[n] = sbj_name
                score.append((n,sbj_gpa,sbj_grade))
        
        case 2:
            for i in range(len(sbjs)):
                for j in range(len(score_re)):
                    if score[i][0] == score_re[j][0]:
                        print(f"[{sbjs[score[i][0]]}] {score[i][1]}학점: {score[i][2]} -> 재수강 {score_re[j][2]}")
                        break
                else: print(f"[{sbjs[score[i][0]]}] {score[i][1]}학점: {score[i][2]}")
        
        case 3:
            gpaSum = 0
            gpa_f = 0
            scoreSum = 0
            good = 0
            for i in range(len(score)):
                gpaSum += score[i][1]
                for j in range(len(score_re)):
                    if score_re[j][0] == score[i][0]: #재수강을 했다!
                        if gradeToNum(score_re[j][2]) > gradeToNum(score[i][2]): #재수강 평점이 더 높다!
                            scoreSum += gradeToNum(score_re[j][2])*score[i][1]
                            good = 1 #좋다!
                        break
                if not good:
                    scoreSum += gradeToNum(score[i][2])*score[i][1]
                    if score[i][2] == 'F': gpa_f += score[i][1]
            print(f"제출용: {gpaSum-gpa_f}학점(GPA: {scoreSum/(gpaSum-gpa_f)})\n열람용: {gpaSum}학점(GPA: {scoreSum/gpaSum})")
            break
