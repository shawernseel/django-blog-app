from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #one to many relationship

    #python dunder method, it controls what happens when you do str(obj)/print(obj)
    #dunder means double underscore method (also called magic methods or special methods)
    #This makes it so that Django Post.objects.all() shows each object like <Post: Blog 1> instead of <Post: Post object (1)>.
    def __str__(self):
        return self.title