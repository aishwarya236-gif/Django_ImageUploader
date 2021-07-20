from django.shortcuts import render

from .forms import ImageForm 
from .models import Image 

# Create your views here.

def home(request):
    if request.method == "POST": 
        form = ImageForm(data = request.POST, files = request.FILES) 
        if form.is_valid(): 
            form.save() 
            obj = form.instance 
            return render(request, "home.html", {"obj":obj})

    form = ImageForm() 
    img = Image.objects.all() 
    return render(request, "home.html", {"img":img, "form":form})
