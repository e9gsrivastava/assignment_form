"""
admin.py

"""

from django.contrib import admin
from .models import (
    Book,
    Car,
    Song,
    Movie,
    JobPosting,
    Category,
    Product,
    Project,
    Task,
    PostCategory,
    Post,
    Student,
    Course,
    Enrollment,
)

# Register your models here.


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    """
    Admin configuration for the Book model.
    """

    list_display = ["title", "author", "publication_date", "isbn"]


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    """
    Admin configuration for the Car model.
    """

    list_display = ["make", "model", "year", "transmission"]


@admin.register(Song)
class AdminSong(admin.ModelAdmin):
    """
    Admin configuration for the Song model.
    """

    list_display = ["title", "artist", "genre", "duration"]


@admin.register(Movie)
class AdminMovie(admin.ModelAdmin):
    """
    Admin configuration for the Movie model.
    """

    list_display = ["title", "director", "release_year", "rating"]


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    """
    Admin configuration for the Category model.
    """

    list_display = ["name"]


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    """
    Admin configuration for the Product model.
    """

    list_display = ["name", "description", "category"]


@admin.register(JobPosting)
class AdminJobPosting(admin.ModelAdmin):
    """
    Admin configuration for the JobPosting model.
    """

    list_display = ["title", "company", "location", "employment_type"]


@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    """
    Admin configuration for the Task model.
    """

    list_display = ["name", "description", "project"]


@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    """
    Admin configuration for the Project model.
    """

    list_display = ["name", "description"]


@admin.register(PostCategory)
class AdminPostCategory(admin.ModelAdmin):
    """
    Admin configuration for the PostCategory model.
    """

    list_display = ["name"]


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    """
    Admin configuration for the Post model.
    """

    list_display = ["title", "content", "category"]


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    """
    Admin configuration for the Student model.
    """

    list_display = ["name"]


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    """
    Admin configuration for the Course model.
    """

    list_display = ["name"]


@admin.register(Enrollment)
class AdminEnrollment(admin.ModelAdmin):
    """
    Admin configuration for the Enrollment model.
    """

    list_display = ["student", "course", "grade"]
