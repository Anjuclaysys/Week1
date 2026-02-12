from operations import StudentService


def main():
    service = StudentService()

    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Enroll in Course")
        print("6. Add Grade")
        print("7. Display Students")
        print("8. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                sid = int(input("Enter ID: ").strip())
                name = input("Enter Name: ").strip()
                age = int(input("Enter Age: ").strip())
                service.add_student(sid, name, age)

            elif choice == "2":
                sid = int(input("Enter ID: "))
                service.remove_student(sid)

            elif choice == "3":
                sid = int(input("Enter ID: "))
                service.search_student(sid)

            elif choice == "4":
                sid = int(input("Enter ID: "))
                name = input("Enter New Name: ")
                age = int(input("Enter New Age: "))
                service.update_student(sid, name, age)

            elif choice == "5":
                sid = int(input("Enter ID: "))
                course = input("Enter Course Name: ")
                service.enroll_course(sid, course)

            elif choice == "6":
                sid = int(input("Enter ID: "))
                course = input("Enter Course Name: ")
                grade = float(input("Enter Grade: "))
                service.add_grade(sid, course, grade)

            elif choice == "7":
                service.display_students()

            elif choice == "8":
                print("Exiting...")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Invalid input type.")


if __name__ == "__main__":
    main()
