"""
urls.py
"""
from django.urls import path, include
from api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("book/", views.BookList.as_view()),
    path("book/<int:pk>/", views.BookDetail.as_view()),
    path("car/", views.CarList.as_view()),
    path("car/<int:pk>/", views.CarDetail.as_view()),
    path("song/", views.SongList.as_view()),
    path("song/<int:pk>/", views.SongDetail.as_view()),
    path("movie/", views.MovieList.as_view()),
    path("movie/<int:pk>/", views.MovieDetail.as_view()),
    path("jobposting/", views.JobPostingList.as_view()),
    path("jobposting/<int:pk>/", views.JobPostingDetail.as_view()),
    path("product/", views.ProductList.as_view()),
    path("product/<int:pk>/", views.ProductDetail.as_view()),
    path("task/", views.TaskList.as_view()),
    path("task/<int:pk>/", views.TaskDetail.as_view()),
    path("post/", views.PostList.as_view()),
    path("post/<int:pk>/", views.PostDetail.as_view()),
    path("enrollment/", views.EnrollmentList.as_view()),
    path("enrollment/<int:pk>/", views.EnrollmentDetail.as_view(),name='enroll'),
    path("postcategory/", views.PostCategoryList.as_view()),
    path("postcategory/<int:pk>/", views.PostCategoryDetail.as_view()),
    path("category/", views.CategoryList.as_view()),
    path("category/<int:pk>/", views.CategoryDetail.as_view()),
    path("project/", views.ProjectList.as_view()),
    path("project/<int:pk>/", views.ProjectDetail.as_view()),
    path("student/", views.StudentList.as_view() ),
    path("student/<int:pk>/", views.StudentDetail.as_view(), name='student'),
    path("course/", views.CourseList.as_view()),
    path("course/<int:pk>/", views.CourseDetail.as_view()),
    path("api-auth/", include("rest_framework.urls")),
    path("gettoken/", obtain_auth_token),
]
