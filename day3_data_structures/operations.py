from typing import Dict

from db import load_students, save_students
from model import Student


class StudentService:
    """
    Handles all core operations such as adding, removing,
    updating students, enrolling courses, adding grades
    """

    def __init__(self):
        """
        Loads existing students from the JSON file into memory.
        """
        self.students: Dict[int, Student] = load_students()

    def add_student(self, student_id: int, name: str, age: int):
        """
        Add a new student.

        :param student_id: unique id of student
        :type student_id: int
        :param name: name of the student
        :type name: str
        :param age: age of the student
        :type age: int
        """
        if student_id in self.students:
            print("Student_id already exists.")
            return
        self.students[student_id] = Student(student_id, name, age)
        save_students(self.students)
        print("students added successfully")

    def remove_student(self, student_id: int):
        """
        removing student

        :param student_id: unique id of student
        :type student_id: int
        """
        if student_id not in self.students:
            print("student not found")

            return

        del self.students[student_id]
        save_students(self.students)
        print("Student removed successfully.")

    def search_student(self, student_id: int):
        """
        search student

        :param student_id: unique id of student
        :type student_id: int
        """
        if student_id not in self.students:
            print("student not found")
            return
        print(self.students[student_id].to_dict())

    def update_student(self, student_id: int, name: str, age: int):
        """
        update student

        :param student_id: unique id of student
        :type student_id: int
        :param name: Name of student
        :type name: str
        :param age: age of student
        :type age: int
        """
        if student_id not in self.students:
            print("student not found")
            return
        self.students[student_id].name = name
        self.students[student_id].age = age
        save_students(self.students)
        print("student updated successfully")

    def enroll_course(self, student_id: int, course: str):
        """
        for adding courses

        :param student_id: unique id of student
        :type student_id: int
        :param course: course enrolled by the student
        :type course: str
        """
        if student_id not in self.students:
            print("student not found")
            return
        if course not in self.students[student_id].courses:
            self.students[student_id].courses.append(course)
            save_students(self.students)
            print("Course enrolled successfully")
        else:
            print("Already enrolled in this course.")

    def add_grade(self, student_id: int, course: str, grade: float):
        """
        adding grade

        :param student_id: unique id of student
        :type student_id: int
        :param course: course enrolled by the student
        :type course: str
        :param grade: grade obtained by the student
        :type grade: float
        """
        if student_id not in self.students:
            print("student not found")
            return
        if course not in self.students[student_id].courses:
            print("student not enrolled in this course.")
            return
        self.students[student_id].grades[course] = grade
        save_students(self.students)
        print("Grade added successfully.")

    def display_students(self):
        """
        Display all students currently stored in the system.

        """
        if not self.students:
            print("No students available.")
            return
        for student in self.students.values():
            print(student.to_dict())
            print("---------------------------------")
