
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Name must be a non-empty string.")

        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be positive integer.")
        
        self._age = value

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        if not isinstance(value, int) or not 1000 <= value <= 5000:
            raise ValueError("Student ID must be between 1000 and 5000.")

        self._student_id = value

    def add_grade(self, grade):
        if not isinstance(grade, int) or not 1 <= grade <= 5:
            raise ValueError("Grades must be an integer between 1 and 5.")
        
        self.grades.append(grade)

    def remove_grade(self, index):
        try:
            return self.grades.pop(index)
        except IndexError:
            print(f"Invalid grade index, must be between 0 and {len(self.grades)-1}.")

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0

        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f"Student: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.calculate_average()}")

    def __str__(self):
        return f"{self.name} ({self.student_id}) - Average: {self.calculate_average()}"