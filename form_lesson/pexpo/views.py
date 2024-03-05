"""
views.py
"""
from django.views.generic.edit import FormView
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
)


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
        return context


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
        return context


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
        return context


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
        return context
