from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on') #filter by published posts in order of the date they were created on
    template_name = 'index.html' 
    paginate_by = 6 #The max amount of posts visible on the page, Django will automatically add page navigation


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1) #filter our posts so we only have the active ones
        post = get_object_or_404(queryset, slug-slug) #getting the post by its slug
        comments = post.comments.filter(approved=True).order_by('created_on') #getting the comments which have been apporved in ascending order
        liked = False
        if post.likes.filter(id=self.request.user.id).exists(): #check the post likes to see if the user id exists if so will set to liked
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )