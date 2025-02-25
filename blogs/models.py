from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments_serializer")
    Comment = models.TextField()

    def __str__(self):
        return self.Comment
