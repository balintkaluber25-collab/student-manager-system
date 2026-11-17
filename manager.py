from students import Student
import json

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name, age, student_id):
        if student_id in self.students:
            raise ValueError("Student ID already existing.")

        student = Student(name,age,student_id)
        self.students[student_id] = student

    def remove_student(self,student_id):
        if student_id not in self.students:
            raise KeyError("Student ID not existing.")

        return self.students.pop(student_id)

    def find_student(self, student_id):
        if student_id not in self.students:
            raise KeyError("Student ID not exists.")

        return self.students[student_id]

    def list_students(self):
        return self.students.values()

    def calculate_class_average(self):
        total_grades = 0
        total_count = 0
        for student in self.students.values():
            for grade in student.grades:
                total_grades += grade
                total_count +=1

        if total_count == 0:
            return 0
        
        return total_grades / total_count

    def get_top_student(self):

        top_student = []
        top_average = 0
        
        for student in self.students.values():
            if not student.grades:
               continue

            
            average = student.calculate_average()

            if top_average < average:
                top_average = average
                top_student = [student]

            elif top_average == average:
                top_student.append(student)

        return top_student

    def get_students_by_grade(self,grade):

        students_with_that_grade = []

        if not isinstance(grade, int) or not 1 <= grade <= 5:
            raise ValueError("Grade must be an integer between 1 and 5.")

        
        for student in self.students.values():
            if grade in student.grades:
                students_with_that_grade.append(student)

        return students_with_that_grade

    def get_student_count(self):
        return len(self.students)

    def save_to_file(self, filename="students.json"):
        students_data = []

        for student in self.students.values():
            student_data = {
                "name" : student.name,
                "age" : student.age,
                "student_id" : student.student_id,
                "grades" : student.grades
            }

            students_data.append(student_data)

        with open(filename, "w") as file:
            json.dump(students_data, file, indent=4)

    def load_from_file(self, filename="students.json"):
            try:
                with open(filename, "r") as file:
                    data = json.load(file)

                for student_data in data:
                    name = student_data["name"]
                    age = student_data["age"]
                    student_id = student_data["student_id"]
                    grades = student_data["grades"]
                    student = Student(name, age, student_id)

                    student.grades = grades

                    self.students[student_id] = student

            except FileNotFoundError:
                return