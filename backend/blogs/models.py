from django.db import models
from django.contrib.auth import get_user_model

# Get the custom user
User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='profile_pics/default_profile.jpeg')

    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def __str__(self):
        return self.full_name()
    

class Blog(models.Model):
    # Add the fields
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True, default=1)

    def __str__(self):
        return self.title
    

