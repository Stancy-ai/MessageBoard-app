from django.views.generic import ListView
from .models import Post


class HomepageView(ListView):
    model = Post
    template_name = 'home.html'


