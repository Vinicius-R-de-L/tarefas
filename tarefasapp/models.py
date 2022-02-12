from django.db import models

# Create your models here.

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Autor(models.Model):
 
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)

    class Meta:
        ordering = ['sobrenome', 'nome']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.sobrenome}, {self.nome}'

class Info(models.Model):

	conteudo = models.CharField(max_length=1000)
	
	def __str__(self):
		return self.conteudo


class Tarefa(models.Model):
    
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    info = models.ForeignKey(Info, on_delete=models.SET_NULL, null=True)

    def __str__(self):
    	return self.titulo

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])