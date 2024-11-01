import json

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def enroll_course(self, course):
        self.courses.append(course)

    def display_student_info(self):
        print("Student Information:")
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Enrolled Courses: {', '.join(self.courses)}")
        print(f"Grades: {self.grades}")

class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        self.students.append(student.name)

    def display_course_info(self):
        print("Course Information:")
        print(f"Course Name: {self.course_name}")
        print(f"Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print(f"Enrolled Students: {', '.join(self.students)}")

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self):
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        address = input("Enter Address: ")
        student_id = input("Enter Student ID: ")
        student = Student(name, age, address, student_id)
        self.students[student_id] = student
        print(f"Student {name} (ID: {student_id}) added successfully.")

    def add_course(self):
        course_name = input("Enter Course Name: ")
        course_code = input("Enter Course Code: ")
        instructor = input("Enter Instructor Name: ")
        course = Course(course_name, course_code, instructor)
        self.courses[course_code] = course
        print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

    def enroll_student_in_course(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll_course(course.course_name)
            course.add_student(student)
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
        else:
            print("Invalid student ID or course code.")

    def add_grade(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        grade = input("Enter Grade: ")
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            if course_code in student.courses:
                student.add_grade(course_code, grade)
                print(f"Grade {grade} added for {student.name} in {self.courses[course_code].course_name}.")
            else:
                print("Student is not enrolled in this course.")
        else:
            print("Invalid student ID or course code.")

    def display_student_details(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            self.students[student_id].display_student_info()
        else:
            print("Student not found.")

    def display_course_details(self):
        course_code = input("Enter Course Code: ")
        if course_code in self.courses:
            self.courses[course_code].display_course_info()
        else:
            print("Course not found.")

    def save_data(self):
        data = {
            "students": {student_id: {
                "name": student.name,
                "age": student.age,
                "address": student.address,
                "grades": student.grades,
                "courses": student.courses
            } for student_id, student in self.students.items()},
            "courses": {course_code: {
                "course_name": course.course_name,
                "instructor": course.instructor,
                "students": course.students
            } for course_code, course in self.courses.items()}
        }
        with open('data.json', 'w') as f:
            json.dump(data, f)
        print("All student and course data saved successfully.")

    def load_data(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                for student_id, student_info in data["students"].items():
                    student = Student(student_info["name"], student_info["age"], student_info["address"], student_id)
                    student.grades = student_info["grades"]
                    student.courses = student_info["courses"]
                    self.students[student_id] = student
                for course_code, course_info in data["courses"].items():
                    course = Course(course_info["course_name"], course_code, course_info["instructor"])
                    course.students = course_info["students"]
                    self.courses[course_code] = course
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No data file found.")

def main():
    system = StudentManagementSystem()
    system.load_data()

    while True:
        print("==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")
        option = input("Select Option: ")

        if option == '1':
            system.add_student()
        elif option == '2':
            system.add_course()
        elif option == '3':
            system.enroll_student_in_course()
        elif option == '4':
            system.add_grade()
        elif option == '5':
            system.display_student_details()
        elif option == '6':
            system.display_course_details()
        elif option == '7':
            system.save_data()
        elif option == '8':
            system.load_data()
        elif option == '0':
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
