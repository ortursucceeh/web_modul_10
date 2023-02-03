from django.db import models

# Create your models here.

class Author(models.Model):
    fullname = models.CharField(max_length=200)
    borndate = models.DateField()
    born_location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.fullname

class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption

class Quote(models.Model):
    text = models.TextField()
    tags = models.ManyToManyField(Tag)

    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="quotes")
    
    def __str__(self):
        return f"{self.author.fullname} {self.text[:20]}"

