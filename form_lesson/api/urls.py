"""
urls.py
"""
from django.urls import path
from api import views

urlpatterns = [
    path("book/", views.BookList.as_view()),
    path("car/", views.CarList.as_view()),
    path("song/", views.SongList.as_view()),
    path("movie/", views.MovieList.as_view()),
    path("jobposting/", views.JobPostingList.as_view()),
    path("product/", views.ProductList.as_view()),
    path("task/", views.TaskList.as_view()),
    path("post/", views.PostList.as_view()),
    path("enrollment/", views.EnrollmentList.as_view()),
    path("postcategory/", views.PostCategoryList.as_view()),
    path("category/", views.CategoryList.as_view()),
    path("project/", views.ProjectList.as_view()),
    path("student/", views.StudentList.as_view()),
    path("course/", views.CourseList.as_view()),
]
