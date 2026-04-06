from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, CreateView,UpdateView,DeleteView#CRUD
from .form import UserForm, PostForm
from .models import User, Post
from django.urls import reverse_lazy
import logging
import datetime 
logger = logging.getLogger(__name__)

class HomePageview(TemplateView):
    template_name = "app_06/home.html"
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        logger.warning(f'someone visited home page at {datetime.datetime.now()}')
        return context
    

class UserListView(ListView):
    model = User
    context_object_name = "users"
    template_name = "app_06/user_list.html"
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context= super().get_context_data(**kwargs)
        logger.info('someone want our users list')
        return context


class UserDetailView(DetailView):
    model = User
    context_object_name = "user"
    template_name = "app_06/user_profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    # pk_url_kwarg='user_id'
    # localhost/users/username/


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "app_06/post_list.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "app_06/post_detail.html"
    pk_url_kwarg = "post_id"
    # localhost/app/posts/id


class UserPostView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "app_06/user_posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        print("#" * 50)
        username = self.kwargs["username"]
        user = get_object_or_404(User, username=username)
        context["user"] = user
        print(context)
        return context

    def get_queryset(self):
        username = self.kwargs["username"]
        user = get_object_or_404(User, username=username)
        # displaying the data at this order
        return Post.objects.filter(user=user).order_by("-created_at")


class RegisterUserView(CreateView):
    model = User
    form_class = UserForm
    template_name = "app_06/register.html"
    success_url = reverse_lazy("users-list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        logger.warning(f'{self.object.username} is created')
        return response
    


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "app_06/post_create.html"
    slug_url_kwarg='username'
    slug_field='username'

    def form_valid(self, form):
        user = get_object_or_404(User, username=self.kwargs["username"])
        form.instance.user = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "user-detail", kwargs={"username": self.object.user.username}
        )

class UpdateUserView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "app_06/register.html"
    
    def get_object(self) :
        return get_object_or_404(User,username=self.kwargs['username'])
    
    def get_success_url(self) :
        return reverse_lazy('user-detail',kwargs={'username':self.object.username})
    
    def form_valid(self, form):
        response = super().form_valid(form)
        logger.debug(self.request)
        logger.info(f"User updated: {self.object.username}")
        return response
    
class DeleteUserView(DeleteView):
    model= User
    template_name = 'app_06/delete_user.html'
    success_url = reverse_lazy('users-list')
    slug_url_kwarg = 'username'
    slug_field ='username'
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'app_06/post_create.html'
    form_class = PostForm
    slug_url_kwarg ='username'
    slug_field ='username'
    pk_url_kwarg ='post_id'
    def get_object(self):
        return get_object_or_404(Post,id=self.kwargs['post_id'])
    
    def get_success_url(self) :
        return reverse_lazy('user-posts',kwargs={'username':self.object.user.username})
    
class DeletePostView(DeleteView):
    model = Post
    template_name ='app_06/delete_post.html'
    pk_url_kwarg ='post_id'
    slug_url_kwarg ='username'
    slug_field ='username'
    def get_success_url(self) :
        return reverse_lazy('user-posts',kwargs={'username':self.object.user.username})
    
    
    
    