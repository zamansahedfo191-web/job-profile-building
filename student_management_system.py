students= []

def add_student():
    
    student_id= input("Enter student id : ")
    name= input("Enter student name : ")
    student_class= input("Enter student class : ")
    age= input("Enter student age : ")
    marks= float(input("Enter student marks : "))
    
    student = {
        "Id": student_id,
        "Name":  name,
        "Class": student_class,
        "Age" : age,
        "Marks" : marks
    }
    students.append(student)
    print("\nStudent added succesfully to your data")
    
def show_students():
    if not students:
        print("There is no student in your record")
        return
    
    for student in students:
            print("\n---------------------------")
            print(
            "1. Id: ", student["Id"],
            "\n2. Name: ", student["Name"],
            "\n3. Class: ", student["Class"],
            "\n4. Age: ", student["Age"],
            "\n5. Marks: ", student["Marks"] )
            
def search_student():
        student_id= input("\nEnter student Id you want to find : ")     
        for student in students:
            if student["Id"]==student_id:
                 print(
                 "1. Id: ", student["Id"],
                 "\n2. Name: ", student["Name"],
                 "\n3. Class: ", student["Class"],
                 "\n4. Age: ", student["Age"],
                 "\n5. Marks: ", student["Marks"] )
        print("\nThere is no student with this student id")
def delete_student():
     if not students:
         print("There is no student to delete")  
         return
         
     student_id= input("Enter student id you want to delete record : ")    
     for student in students:
            if student_id==student["Id"]:
                students.remove(student)
                print("Student has been deleted from your record ")
                return
     print("Student id dont match with our records")
     
def update_student():
     if not students:
         print("There is no student to update") 
     student_id=input("Enter student ID you want to edit : ")
     for student in students:
         if student_id==student["Id"]:
             student["Name"]= input("Enter new name : ")
             student["Age"]= input("Enter new age : ")
             student["Marks"]=input("Enter new marks : ")
             student["Class"]=input("Enter new Class : ")
             print(f"\nStudent with {student["Id"]} id updated succesfully")
         else :
              print("Invalid student ID")
     
while True :
    print("\n-----------------------")
    print("1. Add student\n2. Show students\n3. Delete student\n4. Search student\n5. Update student\n6. Exit") 
    choice=input("\nEnter serial no what you want to do : ")
     
    if choice=="1":
         add_student()
    elif choice=="2":
         show_students()
    elif choice=="3":
         delete_student()
    elif choice=="4":
         search_student()
    elif choice=="5":
        update_student()
    elif choice=="6":
         print("\nGood bye! ")
         break
    else :
         print("\nInvalid choice! Please choice between 1-4")
    