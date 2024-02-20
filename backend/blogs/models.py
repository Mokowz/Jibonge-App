from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    # Add the fields
    title = models.CharField(max_length=100)
    content = models.TextField()
    tag = models.ManyToManyField(Tag, )
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
