from django.urls import path

from .views import BlogListView, BlogDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, SphereListView, PostLikeRedirect, EmailSending
urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('blog/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('blog/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('blog/sphere/<str:sphere_name>/', CategoryView.as_view(), name='category'),
    path('sphere_list', SphereListView.as_view(), name='sphere_list'),
    path('like/<int:pk>', PostLikeRedirect.as_view(), name='like_post'),
    path('email', EmailSending.as_view(), name='send_mail')

]