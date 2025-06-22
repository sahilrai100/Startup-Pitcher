from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Idea(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    description = models.TextField(validators=[MinLengthValidator(50)])
    pitcher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ideas')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-likes_count', '-created_at']
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(validators=[MinLengthValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Comment by {self.commenter.username} on {self.idea.title}'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'idea']
    
    def __str__(self):
        return f'{self.user.username} likes {self.idea.title}'
    
    def save(self, *args, **kwargs):
        # Update likes count when saving
        super().save(*args, **kwargs)
        self.idea.likes_count = self.idea.likes.count()
        self.idea.save()
    
    def delete(self, *args, **kwargs):
        # Update likes count when deleting
        super().delete(*args, **kwargs)
        self.idea.likes_count = self.idea.likes.count()
        self.idea.save() 