"""
models.py
"""
from django.core.validators import MinLengthValidator
from django.db import models


class Book(models.Model):
    """
    Model representing a book.
    """

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, validators=[MinLengthValidator(13)])


class Car(models.Model):
    """
    Model representing a car.
    """

    TRANSMISSION_CHOICES = [
        ("Automatic", "Automatic"),
        ("Manual", "Manual"),
    ]

    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES)


class Song(models.Model):
    """
    Model representing a song.
    """

    GENRE_CHOICES = [
        ("Pop", "Pop"),
        ("Rock", "Rock"),
        ("Hip Hop", "Hip Hop"),
        ("Electronic", "Electronic"),
    ]

    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    duration = models.FloatField()


class Movie(models.Model):
    """
    Model representing a movie.
    """

    RATING_CHOICES = [
        ("G", "G"),
        ("H", "H"),
        ("I", "I"),
        ("K", "K"),
        ("L", "L"),
        ("M", "M"),
        ("N", "N"),
        ("O", "O"),
        ("P", "P"),
        ("Q", "Q"),
        ("R", "R"),
    ]

    title = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    release_year = models.IntegerField()
    rating = models.CharField(max_length=5, choices=RATING_CHOICES)


class JobPosting(models.Model):
    """
    Model representing a job posting.
    """

    EMPLOYMENT_TYPE_CHOICES = [
        ("Full-time", "Full-time"),
        ("Part-time", "Part-time"),
        ("Contract", "Contract"),
    ]

    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES)


class Category(models.Model):
    """
    Model representing a category.
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model representing a product.
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Project(models.Model):
    """
    Model representing a project.
    """

    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    Model representing a task.
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class PostCategory(models.Model):
    """
    Model representing a post category.
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Model representing a post.
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)


class Student(models.Model):
    """
    Model representing a student.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    """
    Model representing a course.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    """
    Model representing an enrollment.
    """

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """
    this signal creates auth token for users
    """
    if created:
        Token.objects.create(user=instance)