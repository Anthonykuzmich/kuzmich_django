from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Sphere
from .forms import EditForm, PostForm


class BlogListView(ListView):
    model = Post
    template_name = 'blog_page/blog.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        sphere_menu = Sphere.objects.all()
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        context['sphere_menu'] = sphere_menu
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_page/blog_details.html'

    def get_context_data(self, *args, **kwargs):
        sphere_menu = Sphere.objects.all()
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        context['sphere_menu'] = sphere_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog_page/add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog_page/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog_page/delete_post.html'
    success_url = reverse_lazy('blog')


def SphereListView(request):
    sphere_menu_list = Sphere.objects.all()
    return render(request, 'blog_page/category_list.html', context={'sphere_menu_list': sphere_menu_list})


def CategoryView(request, sphere_name):
    sphere_posts = Post.objects.filter(sphere=sphere_name)
    return render(request, 'blog_page/spheres.html', context={'sphere_posts': sphere_posts})
