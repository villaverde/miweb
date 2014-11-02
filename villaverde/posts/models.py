from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=110)

	def __str__(self):
		return self.name


class Post(models.Model):
	title = models.CharField(max_length=200) #Titulo de los post
	slug = models.SlugField(max_length=210) #Slug del post
	body = models.TextField() #Contenido del post
	creation_date = models.DateTimeField(auto_now_add=True) #Fecha de creacion post
	update_date = models.DateTimeField(auto_now=True) #Fecha edicion post
	user = models.ForeignKey(User) #Usuario al que pertenece el post
	category = models.ForeignKey(Category) #Categoria a la que pertenece el post

	def __str__(self):
		return self.title


class Image(models.Model):
	post = models.ForeignKey(Post)
	image = models.ImageField(upload_to='PostsImages')
	upload_date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.image


