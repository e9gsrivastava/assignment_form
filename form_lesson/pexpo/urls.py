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
)

urlpatterns = [
    path("", AddBookView.as_view(), name="add_jobs"),
    path("car", AddCarView.as_view(), name="add_jobs"),
    path("song", AddSongView.as_view(), name="add_jobs"),
    path("movie", AddMovieView.as_view(), name="add_jobs"),
    path("job", AddJobView.as_view(), name="add_jobs"),
    path("product", ProductView.as_view(), name="add_jobs"),
    path("task", TaskView.as_view(), name="add_jobs"),
    path("post", PostView.as_view(), name="add_jobs"),
    path("enroll", EnrollmentView.as_view(), name="add_jobs"),
]
