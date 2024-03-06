"""
urls.py
"""
from django.urls import path
from pexpo.views import (
    AddBookView,
    AddCarView,
    AddSongView,
    AddJobView,
    AddMovieView,
    ProductView,
    TaskView,
    PostView,
    EnrollmentView,
    Home,
    CategoryView,
    ProjectView,
    PostCategoryView,
    StudentView,
    CourseView,
)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("book", AddBookView.as_view(), name="add_book"),
    path("car", AddCarView.as_view(), name="add_car"),
    path("song", AddSongView.as_view(), name="add_song"),
    path("movie", AddMovieView.as_view(), name="add_movie"),
    path("job", AddJobView.as_view(), name="add_job"),
    path("product", ProductView.as_view(), name="add_product"),
    path("category", CategoryView.as_view(), name="add_category"),
    path("task", TaskView.as_view(), name="add_task"),
    path("project", ProjectView.as_view(), name="add_project"),
    path("post", PostView.as_view(), name="add_post"),
    path("post_category", PostCategoryView.as_view(), name="add_post_category"),
    path("enroll", EnrollmentView.as_view(), name="enroll"),
    path("course", CourseView.as_view(), name="course"),
    path("student", StudentView.as_view(), name="student"),
]
