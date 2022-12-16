import pytest
from rest_framework.test import APIClient

from students.models import Student, Course
from model_bakery import baker

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_create_course(client, course_factory):
    course = course_factory()
    response = client.get('api/v1/courses')
    data = response.json()
    assert data == course


