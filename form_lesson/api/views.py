"""
views.py
"""
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
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
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Book object.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CarList(generics.ListCreateAPIView):
    """
    API view for listing and creating Car objects.
    """

    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Car object.
    """

    queryset = Car.objects.all()
    serializer_class = CarSerializer


class SongList(generics.ListCreateAPIView):
    """
    API view for listing and creating Song objects.
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Song object.
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer


class MovieList(generics.ListCreateAPIView):
    """
    API view for listing and creating Movie objects.
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    API view for retrieving, updating, and deleting a Movie object.
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class JobPostingList(generics.ListCreateAPIView):
    """
    API view for listing and creating JobPosting objects.
    """

    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer


class JobPostingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a JobPosting object.
    """

    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer


class ProductList(generics.ListCreateAPIView):
    """API view for listing and creating Product objects."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Product object.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TaskList(generics.ListCreateAPIView):
    """API view for listing and creating Task objects."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Task object.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class PostList(generics.ListCreateAPIView):
    """
    API view for listing and creating Post objects.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Post object.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EnrollmentList(generics.ListCreateAPIView):
    """
    API view for listing and creating Enrollment objects.
    """

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class EnrollmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a enrollment object.
    """

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class PostCategoryList(generics.ListCreateAPIView):
    """
    API view for listing and creating PostCategory objects.
    """

    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer


class PostCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a postcategory object.
    """

    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer


class CategoryList(generics.ListCreateAPIView):
    """
    API view for listing and creating Category objects.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Category object.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProjectList(generics.ListCreateAPIView):
    """
    API view for listing and creating Project objects.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Project object.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class StudentList(generics.ListCreateAPIView):
    """
    API view for listing and creating Student objects.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Student object.
    """

    queryset = Student.objects.all()
    serializer_class = CarSerializer


class CourseList(generics.ListCreateAPIView):
    """
    API view for listing and creating Course objects.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Course object.
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
