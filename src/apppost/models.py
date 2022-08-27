from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    name =  models.CharField(max_length=100)
    headline = models.CharField('Headline',max_length=100)
    contex = RichTextField(blank=True, null=True)
    date = models.DateTimeField(null=True)
    # contex = models.TextField()
    
    def __str__(self):
        return self.name
