from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView 
from .models import Post 
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

def home(request):
 
 return render(request, 'blog/home.html',)


  
class listview(LoginRequiredMixin, ListView): 
  
    # specify the model for list view 
 model = Post 


class createview(LoginRequiredMixin, CreateView):
 model=Post
 fields = ['title', 'content']


 def form_valid(self, form):
  form.instance.author = self.request.user
  return super().form_valid(form)
  
class detailview(DetailView): 
    # specify the model to use 
    model=Post

class updateview(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    # specify the model you want to use 
 model=Post
 fields = ['title', 'content']

 def form_valid(self, form):
  form.instance.author = self.request.user
  return super().form_valid(form)
 
 def test_func(self):
  post = self.get_object()
  if self.request.user==post.author:
   return True
  return False


class deleteview(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    # specify the model you want to use 
 model=Post 
 success_url = '/views/'
 def test_func(self):
  post = self.get_object()
  if self.request.user==post.author:
   return True
  return False

def allblogs(request, slug):
 posts=Post.objects.filter(author=slug)
 
 context={'posts':posts}
 return render(request, 'blog/allblog.html', context)
