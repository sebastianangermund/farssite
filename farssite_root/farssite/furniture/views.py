from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView

from .models import Furniture


class HomeListView(generic.ListView):
    """Generic class-based view displaying home page."""
    model = Furniture
    template_name = 'home.html'


class FurnitureListView(generic.ListView):
    """Generic class-based view listing all pieces on site."""
    model = Furniture
    template_name = 'furniture/furniture_list.html'
    paginate_by = 10


class FurnitureDetailView(generic.DetailView):
    """Generic class-based view displaying a specific piece."""
    model = Furniture
    template_name = 'furniture/furniture_detail.html'


class FurnitureCreate(LoginRequiredMixin, CreateView):
    """Generic class-based view, generating form to create new furniture object."""
    model = Furniture
    template_name = 'furniture/furniture_form.html'
    fields = ['title', 'piece', 'photo', 'description']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(FurnitureCreate, self).form_valid(form)
