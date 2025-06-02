from django.db import models
from django.urls import reverse

class Journalist(models.Model):
    """modello generico di giornalista"""
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.first_name}  {self.last_name}"


class Article(models.Model):
    """Modello generico di un articolo di news"""
    title = models.CharField(max_length=100)
    contenuto = models.TextField()
    journalist = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name="articles")
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk":self.pk})
    
    
