from django.views.generic import TemplateView, DetailView
from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
# for tomorrow's class
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm



class HomePageView( LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get(self, request):
        posts = Post.objects.all().order_by('-id')
        context = {'posts': posts}
        return render(request, self.template_name, context)

class DetailPageView( LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)
    
    
# for tomorrow
class PostCreateView( LoginRequiredMixin, CreateView):
    model = Post
    fields = ['author', 'title', 'description', 'published_date']
    template_name = 'post_create.html' # Add this line
    success_url = reverse_lazy('home')
    
    
class PostUpdateView(UpdateView):
    model = Post
    fields = ['author', 'title', 'description', 'published_date']
    template_name = 'post_edit.html' # Add this line
    success_url = reverse_lazy('home')
    
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'post_confirm_delete.html'
    
class LandingPageView(TemplateView):

    template_name = "index.html"
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {user}')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})