from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	price = models.FloatField()
	category = models.CharField(max_length=50)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url