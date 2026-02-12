from typing import List, Dict


class Student:
    """
    Represent a student in student management system
    """
    def __init__(
        self,
        student_id: int,
        name: str,
        age: int,
        courses: List[str] = None,
        grades: Dict[str, float] = None,
    ):

        self.id = student_id
        self.name = name
        self.age = age
        self.courses = courses if courses else []
        self.grades = grades if grades else {}

    def to_dict(self) -> dict:
        """
        Convert the Student object into a dictionary.
        
        :param self: student details
        :return: Dictionary representation of the student.
        :rtype: dict
        """
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "courses": self.courses,
            "grades": self.grades,
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Create a Student object from a dictionary.
        
        :param data: Dictionary containing student data.
        :type data: dict
        """
        return Student(
            data["id"],
            data["name"],
            data["age"],
            data.get("courses", []),
            data.get("grades", {}),
        )
