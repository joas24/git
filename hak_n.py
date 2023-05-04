import random
sbjs = {}
score = []
score_re = []

courses = []
class CourseInfo:
    
    global courses

    def __init__(self, name, gpa, grade):
        self.name = name
        self.gpa = gpa
        self.grade = grade
        courses.append(name)
        
    def call(self):
        print(f"[{self.name}] {self.gpa}학점 : {self.grade}")

    def call_all():
        for i in courses:
            globals()[i].call()


def gradeToNum(grade):
    if grade[0] == 'F': return 0
    if len(grade)==2: return 69-ord(grade[0])+0.5  
    else: return 69-ord(grade)

while True:
    print("작업을 선택하세요.\n1. 입력\n2. 출력\n3. 조회\n4. 계산\n5. 종료")
    choice = int(input())
    match choice:
        case 1:
            print("과목명, 학점, 평점을 입력하세요 : ")
            sbj_name, sbj_gpa, sbj_grade = input().split(',')

            if sbj_name in courses:#재수강 과목일 경우
                score_re.append((n,sbj_gpa,sbj_grade))
            else: #신규 과목일 경우
                globals()[sbj_name] = CourseInfo(sbj_name, sbj_gpa, sbj_grade)

        
        case 2:
            CourseInfo.call_all()

        case 3: 
            course_name = input("과목명을 입력하세요 : ")
            if course_name in courses:
                globals()[course_name].call()
            else: print("해당하는 과목이 없습니다.")

        case 4:
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

        case 5:
            break
