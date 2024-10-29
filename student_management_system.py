import json

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def display_student_info(self):
        self.display_person_info()
        print(f"ID: {self.student_id}")
        print(f"Enrolled Courses: {', '.join(self.courses) if self.courses else 'None'}")
        print(f"Grades: {self.grades if self.grades else 'No grades available'}")

class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def display_course_info(self):
        print(f"Course Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor}")
        print("Enrolled Students:")
        for student in self.students:
            print(f"- {student}")

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, name, age, address, student_id):
        if student_id not in self.students:
            self.students[student_id] = Student(name, age, address, student_id)
            print(f"Student {name} (ID: {student_id}) added successfully.")
        else:
            print("Student ID already exists.")

    def add_course(self, course_name, course_code, instructor):
        if course_code not in self.courses:
            self.courses[course_code] = Course(course_name, course_code, instructor)
            print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")
        else:
            print("Course code already exists.")

    def enroll_student_in_course(self, student_id, course_code):
        student = self.students.get(student_id)
        course = self.courses.get(course_code)
        if student and course:
            student.enroll_course(course.course_name)
            course.add_student(student.name)
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
        else:
            print("Invalid student ID or course code.")

    def add_grade_for_student(self, student_id, course_code, grade):
        student = self.students.get(student_id)
        course = self.courses.get(course_code)
        if student and course and course.course_name in student.courses:
            student.add_grade(course.course_name, grade)
            print(f"Grade {grade} added for {student.name} in {course.course_name}.")
        else:
            print("Student is not enrolled in the course or invalid student ID/course code.")

    def display_student_details(self, student_id):
        student = self.students.get(student_id)
        if student:
            print("Student Information:")
            student.display_student_info()
        else:
            print("Student not found.")

    def display_course_details(self, course_code):
        course = self.courses.get(course_code)
        if course:
            print("Course Information:")
            course.display_course_info()
        else:
            print("Course not found.")

    def save_data(self, filename="data.json"):
        data = {
            "students": {student_id: {"name": student.name, "age": student.age, "address": student.address,
                                      "grades": student.grades, "courses": student.courses}
                         for student_id, student in self.students.items()},
            "courses": {course_code: {"course_name": course.course_name, "instructor": course.instructor,
                                      "students": course.students}
                        for course_code, course in self.courses.items()}
        }
        with open(filename, "w") as f:
            json.dump(data, f)
        print("All student and course data saved successfully.")

    def load_data(self, filename="data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for student_id, student_data in data["students"].items():
                    student = Student(student_data["name"], student_data["age"], student_data["address"], student_id)
                    student.grades = student_data["grades"]
                    student.courses = student_data["courses"]
                    self.students[student_id] = student
                for course_code, course_data in data["courses"].items():
                    course = Course(course_data["course_name"], course_code, course_data["instructor"])
                    course.students = course_data["students"]
                    self.courses[course_code] = course
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")

def main():
    system = StudentManagementSystem()
    while True:
        print("\n==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")
        choice = input("Select Option: ")
        if choice == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            address = input("Enter Address: ")
            student_id = input("Enter Student ID: ")
            system.add_student(name, age, address, student_id)
        elif choice == "2":
            course_name = input("Enter Course Name: ")
            course_code = input("Enter Course Code: ")
            instructor = input("Enter Instructor Name: ")
            system.add_course(course_name, course_code, instructor)
        elif choice == "3":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            system.enroll_student_in_course(student_id, course_code)
        elif choice == "4":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            grade = input("Enter Grade: ")
            system.add_grade_for_student(student_id, course_code, grade)
        elif choice == "5":
            student_id = input("Enter Student ID: ")
            system.display_student_details(student_id)
        elif choice == "6":
            course_code = input("Enter Course Code: ")
            system.display_course_details(course_code)
        elif choice == "7":
            system.save_data()
        elif choice == "8":
            system.load_data()
        elif choice == "0":
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()