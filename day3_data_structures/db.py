import json
from typing import Dict

from model import Student

FILE_NAME = "students.json"


def load_students() -> Dict[int, Student]:
    """
    Load all students from the JSON file

    :return: Dictionary of students where key is student ID
             and value is Student object.
    :rtype: Dict[int, Student]
    """
    students = {}

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            for item in data:
                student = Student.from_dict(item)
                print(student)
                students[student.id] = student

    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        print("error while reading jsonfile")

    return students


def save_students(students: Dict[int, Student]) -> None:
    """
    Save all students to the JSON file.

    :param students: Dictionary of students where key is
                     student ID and value is Student object.
    :type students: Dict[int, Student]
    """
    with open(FILE_NAME, "w") as file:
        json.dump([student.to_dict() for student in students.values()], file, indent=4)
