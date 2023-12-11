import math


class Student:
    def __init__(self, name, grades: list):
        self.name = name
        self.grades = grades

    def getGpa(self):
        gpa = 0
        for grade in self.grades:
            gpa += grade
        gpa = gpa / len(self.grades)
        gpa = gpa / 25
        return gpa
