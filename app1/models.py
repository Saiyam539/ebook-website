from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookGenre(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    

class Books(models.Model):
    book_name = models.CharField(max_length=30)
    book_desc = models.CharField(max_length=400)
    book_author = models.CharField(max_length=30,default='Author')
    book_genre  = models.ForeignKey(BookGenre,on_delete=models.DO_NOTHING,null=True)
    book_cover = models.ImageField(upload_to='covers/',default='')
    pdf_file = models.FileField(upload_to='pdfs/',default='')
    
    def __str__(self):
        return self.book_name

class Wishes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    book = models.ForeignKey(Books,on_delete=models.CASCADE,null=True)
    # book = models.ManyToManyField(Books)
    