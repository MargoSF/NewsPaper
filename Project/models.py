from django.db import models

class Autor
    name = models.Charfield(max_length=107)
    rating = models.IntegerField(default=0)

class Category
    category_name = models.CharField(max_length=107, unique=True)

class Post
    author = models.ForeignKey('Autor', on_delete=models.CASCADE)
    post_type = models.CharField(max_length=4, choices=PostType, default=news)
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', through='PostCategory')
    headline = models.CharField(max_length=300)
    text = models.TextField()
    rating = models.IntegerField(default=0)

class PostCategory
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Comment
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=0)

