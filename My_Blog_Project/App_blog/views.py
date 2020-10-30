from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, TemplateView, View
from App_blog.models import Blog, Comment, Like
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
import uuid
from . import forms

# Create your views here.

class Blog_List_View(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'App_blog/blog_list.html'
    # queryset = Blog.objects.order_by('-publish_date')

class Write_Blog_View(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image')
    template_name = 'App_blog/create_blog.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        title = obj.blog_title
        obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        obj.save()
        return HttpResponseRedirect(reverse('index'))

@login_required
def Blog_Details_View(request, slug):
    blog = Blog.objects.get(slug=slug)
    user = request.user
    already_liked = Like.objects.filter(blog=blog, user=user)
    if already_liked:
        liked = True
    else:
        liked = False

    comment_form = forms.Comment_Form()
    if request.method == 'POST':
        comment_form = forms.Comment_Form(request.POST)
        if comment_form.is_valid():
            comment_obj = comment_form.save(commit=False)
            comment_obj.user = request.user
            comment_obj.blog = blog
            comment_obj.save()
            return HttpResponseRedirect(reverse('App_blog:blog_details', kwargs={'slug':slug}))

    return render(request, 'App_blog/blog_details.html', context={'blog' : blog, 'comment_form' : comment_form, 'liked':liked })


@login_required
def Like_View(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog, user=user)
    if not already_liked:
        new_obj = Like(blog=blog, user=user)
        new_obj.save()
    return HttpResponseRedirect(reverse('App_blog:blog_details', kwargs={'slug' : blog.slug}))


@login_required
def Unlike_View(request, pk):
        blog = Blog.objects.get(pk=pk)
        user = request.user
        already_liked = Like.objects.filter(blog=blog, user=user)
        already_liked.delete()
        return HttpResponseRedirect(reverse('App_blog:blog_details', kwargs={'slug' : blog.slug}))


class MyBlogs_View(LoginRequiredMixin, TemplateView):
    model = Blog
    template_name = 'App_blog/my_blogs.html'


class Update_Blog_View(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image')
    template_name = 'App_blog/edit_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('App_blog:blog_details', kwargs={'slug' : self.object.slug})
