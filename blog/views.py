from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.object.filter(status=1).order_by('created_on') #filter by published posts in order of the date they were created on
    template_name = 'index.html' 
    paginate_by = 6 #The max amount of posts visible on the page, Django will automatically add page navigation


