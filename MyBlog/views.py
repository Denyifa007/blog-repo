from django.views.generic import TemplateView, DetailView
from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
# for tomorrow's class
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        posts = Post.objects.all().order_by('-id')
        context = {'posts': posts}
        return render(request, self.template_name, context)

class DetailPageView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)
    
    
# for tomorrow
class PostCreateView(CreateView):
    model = Post
    fields = ['author', 'title', 'description', 'published_date']
    template_name = 'post_create.html' # Add this line
    success_url = reverse_lazy('home')