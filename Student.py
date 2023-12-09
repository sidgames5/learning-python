import math


class Student:
    def __init__(self, name, grades: list):
        self.name = name
        self.grades = grades
        gpa = 0
        for grade in grades:
            gpa += grade
        gpa = gpa / len(grades)
        gpa = gpa / 25
        self.gpa = gpa
