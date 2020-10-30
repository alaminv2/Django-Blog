from django.urls import path
from App_blog import views

app_name = 'App_blog'

urlpatterns = [
    path('', views.Blog_List_View.as_view(), name="blog_list"),
    path('write_blog/', views.Write_Blog_View.as_view(), name="write_blog"),
    path('blog_details/<slug:slug>/', views.Blog_Details_View, name="blog_details"),
    path('like_blog/<pk>/', views.Like_View, name="like_blog"),
    path('unlike_blog/<pk>/', views.Unlike_View, name="unlike_blog"),
    path('my_blogs/', views.MyBlogs_View.as_view(), name="my_blogs"),
    path('edit_blog/<pk>/', views.Update_Blog_View.as_view(), name="edit_blog"),
]
