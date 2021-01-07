from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, RedirectView, TemplateView
from django.views.generic.edit import FormView
from django_filters.views import FilterView

from .filters import OrderFilter
from .models import Post, Sphere
from .forms import EditForm, PostForm, EmailForm


class BlogListView(FilterView):
    paginate_by = 3
    model = Post
    template_name = 'blog_page/blog.html'
    filterset_class = OrderFilter
    ordering = ['age', 'sphere']
    
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

        context['sphere_menu'] = sphere_menu
        context['total_likes'] = total_likes
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


class SphereListView(TemplateView):
    template_name = 'blog_page/category_list.html'

    def get_context_data(self, *args, **kwargs):
        sphere_menu_list = Sphere.objects.all()
        context = super(SphereListView, self).get_context_data(*args, **kwargs)
        context['sphere_menu_list'] = sphere_menu_list
        return context


class CategoryView(TemplateView):
    template_name = 'blog_page/spheres.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        sphere_posts = Post.objects.filter(sphere=kwargs['sphere_name'])
        sphere_menu_list = Sphere.objects.all()
        context['sphere_posts'] = sphere_posts
        context['sphere_menu_list'] = sphere_menu_list
        return context


class PostLikeRedirect(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        url_ = post.get_absolute_url() + str(self.kwargs['pk'])
        user = self.request.user
        if user.is_authenticated:
            if user in post.likes.all():
                post.likes.remove(user)
            else:
                post.likes.add(user)
        return url_


class EmailSending(FormView):
    template_name = 'blog_page/email.html'
    form_class = EmailForm
    success_url = '/blog'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
