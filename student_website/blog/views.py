from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Sphere
from .forms import EditForm, PostForm, EmailForm


class BlogListView(ListView):
    model = Post
    template_name = 'blog_page/blog.html'
    # ordering = ['-post_date']
    ordering = ['-id']

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

        correct_user = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = correct_user.total_likes()

        liked = False
        if correct_user.likes.filter(id=self.request.user.id).exists:
            liked = True
        context['sphere_menu'] = sphere_menu
        context['total_likes'] = total_likes
        context['liked'] = liked
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
    sphere_menu_list = Sphere.objects.all()
    return render(request, 'blog_page/spheres.html', context={'sphere_name': sphere_name, 'sphere_posts': sphere_posts, 'sphere_menu_list':sphere_menu_list})


def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = True
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))


def email_form(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject, message, email, ['cipom14532@nenekbet.com'], fail_silently=False)
    form = EmailForm()
    return render(request, 'blog_page/email.html', {'form': form})

