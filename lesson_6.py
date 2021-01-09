# Урок 6: аннотации типов и dataclasses

from dataclasses import dataclass, field
from typing import List, Optional


# Аннотации не проверяются при запуске - это документация,
# которую умеют читать инструменты (mypy, IDE)
def average(grades: List[float]) -> float:
    return sum(grades) / len(grades)


# Optional[str] значит "строка или None"
def find_student(name: str, students: List[str]) -> Optional[str]:
    for student in students:
        if student == name:
            return student
    return None


# Раньше класс для хранения данных требовал написать __init__, __repr__,
# __eq__ руками. dataclass генерирует их из аннотаций полей
@dataclass
class Student:
    name: str
    age: int
    # Изменяемое значение по умолчанию задается через field(default_factory=...)
    # Если написать просто grades=[] - один список разделят ВСЕ студенты
    grades: List[float] = field(default_factory=list)

    def average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return average(self.grades)


ivan = Student("Иван", 15)
ivan.grades.append(4.5)
ivan.grades.append(5.0)

masha = Student("Маша", 14, grades=[5.0, 5.0])

# __repr__ сгенерирован автоматически - печатается красиво
print(ivan)
print(masha)

# __eq__ тоже: сравнение по значениям полей, а не по адресу в памяти
print(Student("Иван", 15) == Student("Иван", 15))

print("средний балл Ивана:", ivan.average_grade())
