from django.shortcuts import render, redirect
from .models import ProjectModel, ContactModel

# Create your views here.
def home(request):
    return render(request, 'home.html')

def projects(request):
    data = ProjectModel.objects.all()
    return render(request, 'projects.html',{'data': data})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.POST.get('name') and request.POST.get('email') and request.POST.get('idea'):
        NAME = request.POST.get('name')
        EMAIL = request.POST.get('email')
        IDEA = request.POST.get('idea')
        print(NAME, EMAIL, IDEA)
        d = ContactModel(name = NAME, email = EMAIL, idea = IDEA)
        d.save()
        return render(request, 'contact.html', {'response':'Your response was submitted, I will get back to you as soon as possible'})
    else:
        return render(request, 'contact.html')