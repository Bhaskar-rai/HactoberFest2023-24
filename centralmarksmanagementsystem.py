def calculate_cgpa(grades):
    total_points = 0
    total_credits = 0

    for course, grade, credits in grades:
        grade_points = 0
        if grade == "A+":
            grade_points = 4.0
        elif grade == "A":
            grade_points = 3.7
        elif grade == "A-":
            grade_points = 3.3
        elif grade == "B+":
            grade_points = 3.0
        elif grade == "B":
            grade_points = 2.7
        elif grade == "B-":
            grade_points = 2.3
        elif grade == "C+":
            grade_points = 2.0
        elif grade == "C":
            grade_points = 1.7
        elif grade == "C-":
            grade_points = 1.3
        elif grade == "D":
            grade_points = 1.0

        total_points += grade_points * credits
        total_credits += credits

    cgpa = total_points / total_credits
    return round(cgpa, 2)

def calculate_grade(cgpa):
    if 3.67 <= cgpa <= 4.0:
        return "A+"
    elif 3.33 <= cgpa < 3.67:
        return "A"
    elif 3.0 <= cgpa < 3.33:
        return "A-"
    elif 2.67 <= cgpa < 3.0:
        return "B+"
    elif 2.33 <= cgpa < 2.67:
        return "B"
    elif 2.0 <= cgpa < 2.33:
        return "B-"
    elif 1.67 <= cgpa < 2.0:
        return "C+"
    elif 1.33 <= cgpa < 1.67:
        return "C"
    elif 1.0 <= cgpa < 1.33:
        return "C-"
    else:
        return "D"

def main():
    students = {}
    
    while True:
        print("\nCentral Management System")
        print("1. Add Student")
        print("2. Calculate CGPA and Grade")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_name = input("Enter Student Name: ")
            student_id = input("Enter Student ID: ")
            num_courses = int(input("Enter the number of courses: "))
            courses = []
            
            for _ in range(num_courses):
                course_name = input("Enter Course Name: ")
                course_grade = input("Enter Course Grade (A+, A, A-, etc.): ")
                course_credits = int(input("Enter Course Credits: "))
                courses.append((course_name, course_grade, course_credits))
            
            students[student_id] = {"name": student_name, "courses": courses}
            print(f"Student {student_name} with ID {student_id} added to the system.")

        elif choice == '2':
            student_id = input("Enter Student ID: ")
            student = students.get(student_id)
            if student:
                cgpa = calculate_cgpa(student["courses"])
                grade = calculate_grade(cgpa)
                print(f"Student ID: {student_id}")
                print(f"Name: {student['name']}")
                print(f"CGPA: {cgpa}")
                print(f"Grade: {grade}")
            else:
                print(f"Student with ID {student_id} not found.")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
