from django.shortcuts import render
from .forms import HomeworkForm
from django.shortcuts import redirect
from django.utils import timezone
from .models import Homework
# Create your views here.

def homeworks_list(request):
    posts = Homework.objects.order_by('id')
    return render(request, 'hw/homeworks_list.html', {'posts': posts})

def new_task(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = HomeworkForm()
    #Post.objects.create(title='Sample title', text='Test')
    return render(request, 'hw/new_post.html', {'form':form})
