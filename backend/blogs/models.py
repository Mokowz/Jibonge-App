from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='profile_pics/default_profile.jpeg')

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name()
    

class Blog(models.Model):
    # Add the fields
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

