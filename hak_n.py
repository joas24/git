courses = []
class CourseInfo:

    def __init__(self, name, gpa, grade):
        self.name = name
        self.gpa = int(gpa)
        self.grade = grade
        
    def __str__(self):
        return self.name
    
    def call(self):
        print(f"[{self.name}] {self.gpa}학점 : {self.grade}")

    def call_all():
        for c in courses:
            c.call()


def gradeToNum(grade):
    if grade[0] == 'F': return 0
    if len(grade)==2: return 69-ord(grade[0])+0.5  
    else: return 69-ord(grade)

def clas(str):
    return globals()[str]

while True:
    print("작업을 선택하세요.\n1. 입력\n2. 출력\n3. 조회\n4. 계산\n5. 종료")
    try:
        choice = int(input())
    except ValueError:
        print("잘못된 입력입니다.")
        continue
    match choice:
        case 1:
            print("과목명, 학점, 평점을 입력하세요 : ")
            try:
                sbj_name, sbj_gpa, sbj_grade = input().split(',')
            except ValueError:
                print("잘못된 입력입니다.")
                continue

            if (float(sbj_gpa)%1!= 0) or (gradeToNum(sbj_grade) < 0 or gradeToNum(sbj_grade) > 4.5):
                print("잘못된 입력입니다.")
                continue

            if sbj_name not in [str(i) for i in courses]:
                globals()[sbj_name] = CourseInfo(sbj_name, sbj_gpa, sbj_grade)
                courses.append(clas(sbj_name))

            elif gradeToNum(sbj_grade) > gradeToNum(clas(sbj_name).grade):
                clas(sbj_name).grade = sbj_grade
        
        case 2:
            if len(courses) == 0:
                print("입력된 과목이 없습니다.")
                continue
            
            CourseInfo.call_all()

        case 3: 
            try:
                course_name = input("과목명을 입력하세요 : ")
            except ValueError:
                print("잘못된 입력입니다.")
                continue
            
            if course_name in [str(i) for i in courses]:
                globals()[course_name].call()
            else: print("해당하는 과목이 없습니다.")

        case 4:
            if len(courses) == 0:
                print("입력된 과목이 없습니다.")
                continue

            gpaSum = 0
            gpa_f = 0
            scoreSum = 0
            for sbj in courses:
                if gradeToNum(sbj.grade): 
                    gpaSum += sbj.gpa
                    scoreSum += sbj.gpa * gradeToNum(sbj.grade)
                else: gpa_f += sbj.gpa
                
            print(f"제출용: {gpaSum}학점(GPA: {scoreSum/gpaSum})\n열람용: {gpaSum+gpa_f}학점(GPA: {scoreSum/(gpaSum+gpa_f)})")

        case 5:
            break

        case _:
            print("잘못된 입력입니다.")

