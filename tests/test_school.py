import pytest
from source.school import Classroom, Student, Teacher, TooManyStudentsError


@pytest.fixture
def empty_classroom():
    teacher = Teacher("Professor Snape")
    return Classroom(teacher, [], "Potions")


@pytest.fixture
def classroom_with_students():
    teacher = Teacher("Professor McGonagall")
    students = [Student("Harry Potter"), Student("Hermione Granger"), Student("Ron Weasley")]
    return Classroom(teacher, students, "Transfiguration")


def test_add_student(empty_classroom):
    empty_classroom.add_student(Student("Draco Malfoy"))
    assert len(empty_classroom.students) == 1


def test_add_student_raises_error(classroom_with_students):
    with pytest.raises(TooManyStudentsError):
        classroom_with_students.add_student(Student("Neville Longbottom"))


def test_remove_student(classroom_with_students):
    classroom_with_students.remove_student("Hermione Granger")
    assert len(classroom_with_students.students) == 2


def test_change_teacher(classroom_with_students):
    classroom_with_students.change_teacher(Teacher("Professor Flitwick"))
    assert classroom_with_students.teacher.name == "Professor Flitwick"
