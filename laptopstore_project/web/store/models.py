from django.db import models
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars

class Usage(models.Model):
	title = models.CharField(max_length=20, unique=True)
	image = models.ImageField(upload_to='static/img/usage/')
	def __str__(self):
		return self.title

class Brand(models.Model):
	title = models.CharField(max_length=20, unique=True)
	image = models.ImageField(upload_to='static/img/laptopbrand/')
	def __str__(self):
		return self.title

class CPUBrand(models.Model):
	title = models.CharField(max_length=20, unique=True)
	image = models.ImageField(upload_to='static/img/cpubrand/')
	teamcolor = models.CharField(max_length=20, unique=True)
	def __str__(self):
		return self.title

class CPU(models.Model):
	title = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.title

class GPUBrand(models.Model):
	title = models.CharField(max_length=20, unique=True)
	image = models.ImageField(upload_to='static/img/gpubrand/')
	teamcolor = models.CharField(max_length=20, unique=True)
	def __str__(self):
		return self.title

class GPU(models.Model):
	title = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.title

class LaptopImage(models.Model):
	title = models.CharField(max_length=100, unique=True)
	image = models.ImageField(upload_to='static/img/laptop/')
	def __str__(self):
		return self.title

class LaptopRam(models.Model):
	title = models.CharField(max_length=10, unique=True, default='8 GB')
	def __str__(self):
		return self.title

class LaptopDrive(models.Model):
	title = models.CharField(max_length=10, unique=True, default='SSD 500 GB')
	def __str__(self):
		return self.title

class LaptopSize(models.Model):
	title = models.CharField(max_length=10, unique=True, default='15.6')
	def __str__(self):
		return self.title

class LaptopDisplay(models.Model):
	title = models.CharField(max_length=20, unique=True, default='1920 x 1080')
	def __str__(self):
		return self.title

class Laptop(models.Model):
	title = models.CharField(max_length=100, unique=True)
	img = models.ForeignKey(LaptopImage, on_delete = models.CASCADE)
	usage = models.ForeignKey(Usage, on_delete = models.CASCADE)
	brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
	cpubrand = models.ForeignKey(CPUBrand, on_delete = models.CASCADE)
	cpu = models.ForeignKey(CPU, on_delete = models.CASCADE)
	gpubrand = models.ForeignKey(GPUBrand, on_delete = models.CASCADE)
	gpu = models.ForeignKey(GPU, on_delete = models.CASCADE)
	ram = models.ForeignKey(LaptopRam, on_delete = models.CASCADE)
	drive = models.ForeignKey(LaptopDrive, on_delete = models.CASCADE)
	size = models.ForeignKey(LaptopSize, on_delete = models.CASCADE)
	disp = models.ForeignKey(LaptopDisplay, on_delete = models.CASCADE)
	price = models.IntegerField(default = 10000)
	readyforsell = models.BooleanField(default = True)
	def __str__(self):
		return self.title
	def short_description(self):
		return truncatechars(self.title)
	def admin_photo(self):
		return mark_safe('<img src="{}" width="100" height="100" />'.format(self.img.image.url))
	admin_photo.short_description = 'Image'
	admin_photo.allow_tags = True
