"""
serializers.py
"""
from rest_framework import serializers
from pexpo.models import (
    Book,
    Car,
    Song,
    Movie,
    JobPosting,
    Product,
    Task,
    Post,
    Enrollment,
    PostCategory,
    Category,
    Project,
    Student,
    Course,
)


class BookSerializer(serializers.ModelSerializer):
    """
    serializing data for book model
    """

    class Meta:
        model = Book
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    """
    serializing data for car model
    """

    class Meta:
        model = Car
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    """
    serializing data for song model
    """

    class Meta:
        model = Song
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    """
    serializing data for movie model
    """

    class Meta:
        model = Movie
        fields = "__all__"


class JobPostingSerializer(serializers.ModelSerializer):
    """
    serializing data for jobpost model
    """

    class Meta:
        model = JobPosting
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """
    serializing data for product model
    """

    class Meta:
        model = Product
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    """
    serializing data for task model
    """

    class Meta:
        model = Task
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    """
    serializing data for post model
    """

    class Meta:
        model = Post
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):
    """
    serializing data for enrollment model
    """
    student_detail=serializers.SerializerMethodField()
    course_detail=serializers.SerializerMethodField()
    url=serializers.HyperlinkedIdentityField(view_name='enroll')


    class Meta:
        model = Enrollment
        fields = "__all__"

    def get_student_detail(self,object):
        return StudentSerializer(object.student).data

    def get_course_detail(self,object):
        return StudentSerializer(object.course).data



class PostCategorySerializer(serializers.ModelSerializer):
    """
    serializing data for post model
    """

    class Meta:
        model = PostCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    serializing data for category model
    """

    class Meta:
        model = Category
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    """
    serializing data for project model
    """

    class Meta:
        model = Project
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    """
    serializing data for student model
    """

    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """
    serializing data for course model
    """

    class Meta:
        model = Course
        fields = "__all__"
