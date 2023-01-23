from django.shortcuts import render
from .models import *

def home(request):
	title = request.GET.get('query')
	laptops = Laptop.objects.all()
	if title:
		laptops = laptops.filter(title__icontains=title)
		brands = Brand.objects.all()
		cpubrands = CPUBrand.objects.all()
		gpubrands = GPUBrand.objects.all()
		usages = Usage.objects.all()
		rams = LaptopRam.objects.all()
		drives = LaptopDrive.objects.all()
		sizes = LaptopSize.objects.all()
		displays = LaptopDisplay.objects.all()
		context = {
        'laptops': laptops,
        'brands': brands,
        'cpubrands': cpubrands,
        'gpubrands': gpubrands,
        'usages': usages,
        'rams': rams,
        'drives': drives,
        'sizes': sizes,
        'displays': displays,
    	}
		return render(request, 'productlist.html', context)
	else:
		laptops = laptops.filter(title__icontains='white')
		brands = Brand.objects.all()
		cpubrands = CPUBrand.objects.all()
		gpubrands = GPUBrand.objects.all()
		usages = Usage.objects.all()
		rams = LaptopRam.objects.all()
		drives = LaptopDrive.objects.all()
		sizes = LaptopSize.objects.all()
		displays = LaptopDisplay.objects.all()
		context = {
        'laptops': laptops,
        'brands': brands,
        'cpubrands': cpubrands,
        'gpubrands': gpubrands,
        'usages': usages,
        'rams': rams,
        'drives': drives,
        'sizes': sizes,
        'displays': displays,
    	}
		return render(request, 'index.html',context)

def product_list(request):
    title = request.GET.get('title')
    selected_brands = request.GET.getlist('brand')
    selected_cpubrands = request.GET.getlist('cpubrand')
    selected_gpubrands = request.GET.getlist('gpubrand')
    selected_usages = request.GET.getlist('usage')
    selected_rams = request.GET.getlist('ram')
    selected_drives = request.GET.getlist('drive')
    selected_sizes = request.GET.getlist('size')
    selected_displays = request.GET.getlist('disp')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    laptops = Laptop.objects.all()
    if title:
        laptops = laptops.filter(title__icontains=title)
    if selected_brands:
        laptops = laptops.filter(brand__pk__in=selected_brands)
    if selected_cpubrands:
        laptops = laptops.filter(cpubrand__pk__in=selected_cpubrands)
    if selected_gpubrands:
        laptops = laptops.filter(gpubrand__pk__in=selected_gpubrands)
    if selected_usages:
        laptops = laptops.filter(usage__pk__in=selected_usages)
    if selected_rams:
        laptops = laptops.filter(ram__pk__in=selected_rams)
    if selected_drives:
        laptops = laptops.filter(drive__pk__in=selected_drives)
    if selected_sizes:
        laptops = laptops.filter(size__pk__in=selected_sizes)
    if selected_displays:
        laptops = laptops.filter(display__pk__in=selected_displays)
    if min_price or max_price:
        laptops = laptops.filter(price__gte=min_price, price__lte=max_price)

        
    brands = Brand.objects.all()
    cpubrands = CPUBrand.objects.all()
    gpubrands = GPUBrand.objects.all()
    usages = Usage.objects.all()
    rams = LaptopRam.objects.all()
    drives = LaptopDrive.objects.all()
    sizes = LaptopSize.objects.all()
    displays = LaptopDisplay.objects.all()

    context = {
        'laptops': laptops,
        'brands': brands,
        'cpubrands': cpubrands,
        'gpubrands': gpubrands,
        'usages': usages,
        'rams': rams,
        'drives': drives,
        'sizes': sizes,
        'displays': displays,
    }

    return render(request, 'productlist.html', context)

def product_detail(request):
	title = request.GET.get('query')
	laptops = Laptop.objects.all()
	if title:
		laptops = laptops.filter(title__icontains=title)
		brands = Brand.objects.all()
		cpubrands = CPUBrand.objects.all()
		gpubrands = GPUBrand.objects.all()
		usages = Usage.objects.all()
		rams = LaptopRam.objects.all()
		drives = LaptopDrive.objects.all()
		sizes = LaptopSize.objects.all()
		displays = LaptopDisplay.objects.all()

	context = {
        'laptops': laptops,
        'brands': brands,
        'cpubrands': cpubrands,
        'gpubrands': gpubrands,
        'usages': usages,
        'rams': rams,
        'drives': drives,
        'sizes': sizes,
        'displays': displays,
    }
	return render(request, 'productdetail.html', context)