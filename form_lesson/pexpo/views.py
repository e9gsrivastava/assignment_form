"""
views.py
"""
from django.urls import reverse
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.http import HttpResponse
from .forms import (
    BookForm,
    CarForm,
    MovieForm,
    JobPostingForm,
    SongForm,
    ProductForm,
    TaskForm,
    PostForm,
    EnrollmentForm,
    CategoryForm,
    ProjectForm,
    PostCategoryForm,
    CourseForm,
    StudentForm,
)


class Home(ListView):
    """
    to navigate to all the urls from one screen
    """

    template_name = "home.html"
    context_object_name = "urls"

    def get_queryset(self):
        """
        to add query set
        """
        urls = [
            {"url": reverse("add_book"), "name": "Book List"},
            {"url": reverse("add_car"), "name": "Add Car"},
            {"url": reverse("add_song"), "name": "Add Song"},
            {"url": reverse("add_movie"), "name": "Add Movie"},
            {"url": reverse("add_job"), "name": "Add Job"},
            {"url": reverse("add_product"), "name": "Add Product"},
            {"url": reverse("add_task"), "name": "Add Task"},
            {"url": reverse("add_post"), "name": "Add Post"},
            {"url": reverse("enroll"), "name": "Enroll"},
        ]
        return urls


class AddBookView(FormView):
    """
    View for adding a book using BookForm.
    """

    template_name = "common.html"
    form_class = BookForm

    def form_valid(self, form):
        """Handle form submission for adding a book."""
        form.save()
        return HttpResponse("Book added successfully")

    def get_context_data(self, **kwargs):
        """Get context data for rendering the form."""
        context = super().get_context_data(**kwargs)
        context["form_type"] = "Book"
        return context


class AddCarView(FormView):
    """
    View for adding a car using CarForm.
    """

    template_name = "common.html"
    form_class = CarForm

    def form_valid(self, form):
        """Handle form submission for adding a car."""
        form.save()
        return HttpResponse("Car added successfully")

    def get_context_data(self, **kwargs):
        """Get context data for rendering the form."""
        context = super().get_context_data(**kwargs)
        context["form_type"] = "Car"
        return context


class AddSongView(FormView):
    """
    View for adding a song using SongForm.
    """

    template_name = "common.html"
    form_class = SongForm

    def form_valid(self, form):
        """Handle form submission for adding a song."""
        form.save()
        return HttpResponse("Song added successfully")

    def get_context_data(self, **kwargs):
        """Get context data for rendering the form."""
        context = super().get_context_data(**kwargs)
        context["form_type"] = "Song"
        return context


class AddMovieView(FormView):
    """
    View for adding a movie using MovieForm.
    """

    template_name = "common.html"
    form_class = MovieForm

    def form_valid(self, form):
        """Handle form submission for adding a movie."""
        form.save()
        return HttpResponse("Movie added successfully")

    def get_context_data(self, **kwargs):
        """Get context data for rendering the form."""
        context = super().get_context_data(**kwargs)
        context["form_type"] = "Movie"
        return context


class AddJobView(FormView):
    """
    View for adding a job posting using JobPostingForm.
    """

    template_name = "common.html"
    form_class = JobPostingForm

    def form_valid(self, form):
        """Handle form submission for adding a job."""
        form.save()
        return HttpResponse("Job added successfully")

    def get_context_data(self, **kwargs):
        """Get context data for rendering the form."""
        context = super().get_context_data(**kwargs)
        context["form_type"] = "Job"
        return context


class ProductView(FormView):
    """
    View for adding a product using ProductForm.
    """

    template_name = "common.html"
    form_class = ProductForm

    def form_valid(self, form):
        """Handle form submission for adding a product."""
        form.save()
        return HttpResponse("Product added successfully")

    def get_context_data(self, **kwargs):
        """Get context data for rendering the form."""
        context = super().get_context_data(**kwargs)
        context["form_type"] = "Product"
        context["add"] = True
        context["url_name"] = "add_category"
        return context


class CategoryView(FormView):
    """
    View for adding a task using CategoryForm.
    """

    template_name = "sub_type.html"
    form_class = CategoryForm

    def form_valid(self, form):
        """Handle form submission for adding a product."""
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Get context data for rendering the form."""
        context = super().get_context_data(**kwargs)
        context["form_type"] = "Category"
        return context

    def get_success_url(self):
        """To return to desired url"""
        return reverse("add_product")


class TaskView(FormView):
    """
    View for adding a task using TaskForm.
    """

    template_name = "common.html"
    form_class = TaskForm

    def form_valid(self, form):
        """Handle form submission for adding a task."""
        form.save()
        return HttpResponse("Task added successfully")

    def get_context_data(self, **kwargs):
        """Get context data for rendering the form."""
        context = super().get_context_data(**kwargs)
        context["form_type"] = "Task"
        context["add"] = True
        context["url_name"] = "add_project"
        return context


class ProjectView(FormView):
    """
    View for adding a task using ProjectForm.
    """

    template_name = "sub_type.html"
    form_class = ProjectForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_type"] = "Project"
        return context

    def get_success_url(self):
        return reverse("add_task")


class PostView(FormView):
    """
    View for adding a post using PostForm.
    """

    template_name = "common.html"
    form_class = PostForm

    def form_valid(self, form):
        """Handle form submission for adding a post."""
        form.save()
        return HttpResponse("Post added successfully")

    def get_context_data(self, **kwargs):
        """Get context data for rendering the form."""
        context = super().get_context_data(**kwargs)
        context["form_type"] = "Post"
        context["add"] = True
        context["url_name"] = "add_post_category"
        return context


class PostCategoryView(FormView):
    """
    View for adding a task using PostCategoryForm.
    """

    template_name = "sub_type.html"
    form_class = PostCategoryForm

    def form_valid(self, form):
        """Handle form submission for adding a post."""
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Get context data for rendering the form."""
        context = super().get_context_data(**kwargs)
        context["form_type"] = "PostCategory"
        return context

    def get_success_url(self):
        """To return to desired url"""
        return reverse("add_post")


class EnrollmentView(FormView):
    """
    View for enrollment using EnrollmentForm.
    """

    template_name = "common.html"
    form_class = EnrollmentForm

    def form_valid(self, form):
        """Handle form submission for enrollment."""
        form.save()
        return HttpResponse("Enrolled successfully")

    def get_context_data(self, **kwargs):
        """Get context data for rendering the form."""
        context = super().get_context_data(**kwargs)
        context["form_type"] = "Enroll"
        context["add"] = True
        context["add_more"] = True
        context["url_name"] = "course"
        context["url_name_more"] = "student"
        return context


class CourseView(FormView):
    """
    View for adding a task using CourseForm.
    """

    template_name = "sub_type.html"
    form_class = CourseForm

    def form_valid(self, form):
        """Handle form submission for adding a product."""
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Get context data for rendering the form."""
        context = super().get_context_data(**kwargs)
        context["form_type"] = "Course"
        return context

    def get_success_url(self):
        """To return to desired url"""
        return reverse("enroll")


class StudentView(FormView):
    """
    View for adding a task using StudentForm.
    """

    template_name = "sub_type.html"
    form_class = StudentForm

    def form_valid(self, form):
        """Handle form submission for adding a product."""
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Get context data for rendering the form."""
        context = super().get_context_data(**kwargs)
        context["form_type"] = "Student"
        return context

    def get_success_url(self):
        """To return to desired url"""
        return reverse("enroll")
