"""
views.py
"""
from rest_framework import generics
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
from api.serializers import (
    BookSerializer,
    CarSerializer,
    SongSerializer,
    MovieSerializer,
    JobPostingSerializer,
    ProductSerializer,
    TaskSerializer,
    PostSerializer,
    EnrollmentSerializer,
    PostCategorySerializer,
    CategorySerializer,
    ProjectSerializer,
    StudentSerializer,
    CourseSerializer,
)

class BookList(generics.ListCreateAPIView):
    """
    API view for listing and creating Book objects.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CarList(generics.ListCreateAPIView):
    """
    API view for listing and creating Car objects.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class SongList(generics.ListCreateAPIView):
    """
    API view for listing and creating Song objects.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class MovieList(generics.ListCreateAPIView):
    """
    API view for listing and creating Movie objects.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class JobPostingList(generics.ListCreateAPIView):
    """
    API view for listing and creating JobPosting objects.
    """
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class ProductList(generics.ListCreateAPIView):
    """API view for listing and creating Product objects."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class TaskList(generics.ListCreateAPIView):
    """API view for listing and creating Task objects."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class PostList(generics.ListCreateAPIView):
    """
    API view for listing and creating Post objects.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EnrollmentList(generics.ListCreateAPIView):
    """
    API view for listing and creating Enrollment objects.
    """
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class PostCategoryList(generics.ListCreateAPIView):
    """
    API view for listing and creating PostCategory objects.
    """
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer

class CategoryList(generics.ListCreateAPIView):
    """
    API view for listing and creating Category objects.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProjectList(generics.ListCreateAPIView):
    """
    API view for listing and creating Project objects.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class StudentList(generics.ListCreateAPIView):
    """
    API view for listing and creating Student objects.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseList(generics.ListCreateAPIView):
    """
    API view for listing and creating Course objects.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
