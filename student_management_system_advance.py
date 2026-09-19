from collections import Counter

students = [
    {"name": "Rahim", "subject": "Math", "score": 85},
    {"name": "Karim", "subject": "Physics", "score": 72},
    {"name": "Sakib", "subject": "Math", "score": 91},
    {"name": "Nabil", "subject": "Physics", "score": 65},
    {"name": "Hasan", "subject": "Math", "score": 78},
    {"name": "Rafi", "subject": "Chemistry", "score": 88}
]

def analyze_students(students) :
 names=[student["name"] for student in students ]
 subjects=sorted(set(student["subject"] for student in students))
 scores=[student["score"] for student in students]
 
 total=sum(scores)
 avg_score=total/len(scores)
 highest=max(students, key=lambda student : student["score"])
 lowest=min(students, key=lambda student : student["score"])
 
 print(f"All student names : {names}\nAll subjects : {subjects}\nTotal score : {total}\nAverage score : {avg_score : .2f}\nHighest student name :  {highest['name']}~~~score : {highest['score']}\nLowest student name : {lowest['name']}~~~{lowest['score']}")
 
analyze_students(students)

def group_by_subject(students) :
    result={}
    for student in students :
        subject=student["subject"]
        if subject not in result :
            result[subject]=[ ]
        result[subject].append(student)
    return result

def subject_statistics(result) :
    for subject, student_list in result.items() :
        scores=[student['score'] for student in student_list]
        total=sum(scores)
        avg=total/len(students)
        highest=max(student_list, key= lambda student : student["score"])
        lowest=min(student_list, key= lambda student : student["score"])
        print(f"\n\nSubject : {subject}\nTotal score : {total}\nAverage score : {avg: .2f}\nHighest Scorer name  : {highest['name']} >>> {highest['score']} \nLowest scorer name : {lowest['name']} >>> {lowest['score']}")
        
result=group_by_subject(students)
subject_statistics(result)

def categorize_students(students) :
    categories={
    "excellent" : [],
    "good" : [],
    "need_to_improve" : []
    }
    for student in students :
        score=student["score"]
        if score>=90 :
            categories["excellent"].append(student)
        elif score>=70 :
            categories["good"].append(student)
        else :
            categories["need_to_improve"].append(student)
    print(f"\n\nExcelent : {categories['excellent']}\nGood : {categories['good']}\nNeed to improve : {categories['need_to_improve']}")
    
categorize_students(students)

def rank_students(students) :
    print("\n\n")
    sorted_students=sorted(students, key= lambda student : student["score"], reverse= True )
    for position,student in enumerate(sorted_students, start=1) :
        print(f"{position}. {student['name']} >>> {student['score']}")
        
rank_students(students)

def search_student(students, name) :
    found=False
    for student in students :
        if student["name"].lower()==name.lower() :
            print(f"\n\n1. {student['name']}\n2. {student['subject']}\n3. {student['score']} ")
            found=True
    if not found :
         print("\n\nNo student found named : ",name)

search_student(students, "Sahed")

def count_by_subject(students) :
    subjects=[]
    for student in students :
        subjects.append(student['subject'])
    counted_sub=Counter(subjects)
    print("\n\n",counted_sub)
    
count_by_subject(students)