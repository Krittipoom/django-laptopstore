from django.contrib import admin
from .models import Usage, Brand, CPU, CPUBrand, GPU, GPUBrand, LaptopImage, LaptopRam, LaptopDrive, LaptopSize, LaptopDisplay, Laptop

admin.site.register(Usage)
admin.site.register(Brand)
admin.site.register(CPU)
admin.site.register(CPUBrand)
admin.site.register(GPU)
admin.site.register(GPUBrand)
admin.site.register(LaptopImage)
admin.site.register(LaptopRam)
admin.site.register(LaptopDrive)
admin.site.register(LaptopSize)
admin.site.register(LaptopDisplay)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'readyforsell', 'title', 'admin_photo', 'img', 'usage', 'brand', 'cpubrand', 'cpu', 'gpubrand', 'gpu', 'ram', 'drive', 'size', 'disp', 'price')
	list_editable = ('title', 'img', 'usage', 'brand', 'cpubrand', 'cpu', 'gpubrand', 'gpu', 'ram', 'drive', 'size', 'disp', 'price', 'readyforsell')

admin.site.register(Laptop, ProductAdmin)