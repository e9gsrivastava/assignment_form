"""
forms.py
"""
from django import forms
from .models import (
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


class BookForm(forms.ModelForm):
    """
    Form for adding a book.
    """

    class Meta:
        model = Book
        fields = ["title", "author", "publication_date", "isbn"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "author": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter author"}
            ),
            "isbn": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter ISBN"}
            ),
            "publication_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }


class CarForm(forms.ModelForm):
    """
    Form for adding a car.
    """

    transmission = forms.ChoiceField(
        choices=Car.TRANSMISSION_CHOICES, widget=forms.RadioSelect
    )

    class Meta:
        model = Car
        fields = ["make", "model", "year", "transmission"]
        widgets = {
            "make": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter make"}
            ),
            "model": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter model"}
            ),
            "year": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter year"}
            ),
        }


class SongForm(forms.ModelForm):
    """
    Form for adding a song.
    """

    class Meta:
        model = Song
        fields = ["title", "artist", "genre", "duration"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "artist": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter artist"}
            ),
            "genre": forms.Select(attrs={"class": "form-control"}),
            "duration": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter duration"}
            ),
        }


class MovieForm(forms.ModelForm):
    """
    Form for adding a movie.
    """

    class Meta:
        model = Movie
        fields = ["title", "director", "release_year", "rating"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "director": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter director"}
            ),
            "release_year": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Enter release year"}
            ),
            "rating": forms.Select(attrs={"class": "form-control"}),
        }


class JobPostingForm(forms.ModelForm):
    """
    Form for adding a job posting.
    """

    class Meta:
        model = JobPosting
        fields = ["title", "company", "location", "employment_type"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "company": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter company"}
            ),
            "location": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter location"}
            ),
            "employment_type": forms.Select(attrs={"class": "form-control"}),
        }


class ProductForm(forms.ModelForm):
    """
    Form for adding a product.
    """

    class Meta:
        model = Product
        fields = ["name", "description", "category"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter name"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter description"}
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
        }



class CategoryForm(forms.ModelForm):
    """
    Form for adding a Category.
    """

    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter category name",
                }
            ),
        }


class TaskForm(forms.ModelForm):
    """
    Form for adding a task.
    """

    class Meta:
        model = Task
        fields = ["name", "description", "project"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter name"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter description"}
            ),
            "project": forms.Select(attrs={"class": "form-control"}),
        }


class ProjectForm(forms.ModelForm):
    """
    Form for adding a Project.
    """

    class Meta:
        model = Project
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Project name",
                }
            ),
        }


class PostForm(forms.ModelForm):
    """
    Form for adding a post.
    """

    class Meta:
        model = Post
        fields = ["title", "content", "category"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter title"}
            ),
            "content": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter content"}
            ),
            "category": forms.Select(attrs={"class": "form-control"}),
        }


class PostCategoryForm(forms.ModelForm):
    """
    Form for adding a PostCategory.
    """

    class Meta:
        model = PostCategory
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter post name",
                }
            ),
        }


class EnrollmentForm(forms.ModelForm):
    """
    Form for enrollment.
    """

    class Meta:
        model = Enrollment
        fields = ["student", "course", "grade"]
        widgets = {
            "student": forms.Select(attrs={"class": "form-control"}),
            "course": forms.Select(attrs={"class": "form-control"}),
            "grade": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter category"}
            ),
        }


class CourseForm(forms.ModelForm):
    """
    Form for adding a Course.
    """

    class Meta:
        model = Course
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter post name",
                }
            ),
        }


class StudentForm(forms.ModelForm):
    """
    Form for adding a Student.
    """

    class Meta:
        model = Student
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter post name",
                }
            ),
        }
