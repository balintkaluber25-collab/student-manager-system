from manager import StudentManager

manager = StudentManager()
manager.load_from_file()

while True:
    print("---------------------------------")
    print("===STUDENT MANAGER===")
    print("1. Add student")
    print("2. Remove student")
    print("3. List all students")
    print("4. Search student")
    print("5. Add grade")
    print("6. Show student statistics")
    print("7. Save and exit")
    print("---------------------------------")

    x = input("Choose an option: ")
    try:
        choice = int(x)

    except ValueError:
        print("Choice is not an integer between 1 nad 7")
        continue

    if not 1 <= choice <= 7:
        print("Choose an option between 1 and 7.")
        continue

    print("---------------------------------")
    
    match choice:

        case 1:
            try:
                student_name = input("What is the students name? ")
                student_age = int(input("what is the students age? "))
                student_id = int(input("What is the students ID? "))
                manager.add_student(student_name, student_age, student_id)
                print("Student added successfully!")

            except (ValueError, TypeError) as e:
                print(f"Error: {e}")

            manager.save_to_file()

        case 2:
            try:
                student_id = int(input("What is the student ID that you want to delete? "))
                manager.remove_student(student_id)
                print(f"Student {student_id} removed succesfully.")

            except ValueError:
                print("Student ID must be an integer.")
            except KeyError as e:
                print(f"Error: {e}")

            manager.save_to_file()

        case 3:
            students = manager.list_students()

            if not students:
                print("There are no students.")

            else:
                count = manager.get_student_count()
                print(f"Total students: {count}")
                for student in students:
                    print("")
                    student.display_info()         

        case 4:
            try:
                student_id = int(input("Which student would you like to search up? (Student_id)"))
                student = manager.find_student(student_id)
                print("")
                print(student)
            except KeyError as e:
                print(f"Error: {e}")
            except ValueError:
                print("Student ID must be an integer.")

        case 5:
            try:
                student_id = int(input("Which student would you like to add a grade? "))
                student = manager.find_student(student_id)
                student.display_info()
                grade = int(input("What grade would you like to add? "))
                student.add_grade(grade)
                print("Grade added succesfully!")
            except KeyError as e:
                print(f"Error: {e}")
            except ValueError as e:
                print(f"Error: {e}")

            manager.save_to_file()

        case 6:
            print(f"Total student count: {manager.get_student_count()}")
            print(f"Class average: {manager.calculate_class_average():.2f}")
            top_students = manager.get_top_student()

            if not top_students:
                print("No students have grades yet.")
            else:
                print("Top student(s):")
                for student in top_students:
                    print(student)


        case 7:
            manager.save_to_file()
            print("Students saved successfully!")
            break