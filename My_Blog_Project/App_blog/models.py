from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=264, verbose_name="Put a title...")
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name="What's on your mind...?")
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Image')
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment_blog')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    comment = models.TextField(verbose_name='Wanna tell something...?')
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)

    def __str__(self):
        return self.comment


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='like_blog')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')


    def __str__(self):
        return str(self.user) + "   likes   " + str(self.blog.blog_title)
