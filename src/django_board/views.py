from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm

def home_page(request):
        my_title = "%$$#"
        context = {"title": "my_title"}
        if request.user.is_authenticated:
                context = {"title": my_title, 'my_list': [1,2,23,4,5]}
        return render(request, "home.html", context)


def about_page(request):
        return HttpResponse("<h1>About Us</h1>")


def contact_page(request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
                print(form.cleaned_data)
                form = ContactForm()
        context = {
                'title': 'Contact us', 
                'form': form,
        }
        return render(request, 'form.html', context)

def example_page(request):
        context          = {'title': 'example'}
        template_name   = 'hello.html'
        template_obj = get_template(template_name)
        return HttpResponse(template_obj.render(context))
