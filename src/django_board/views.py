from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
        my_title = "%$$#"
        context = {"title": "my_title"}
        if request.user.is_authenticated:
                context = {"title": my_title, 'my_list': [1,2,23,4,5]}
        return render(request, "home.html", context)


def about_page(request):
        return HttpResponse("<h1>About Us</h1>")


def contact_page(request):
        return HttpResponse("<h1>Contact Us</h1>")

def example_page(request):
        context          = {'title': 'example'}
        template_name   = 'hello.html'
        template_obj = get_template(template_name)
        return HttpResponse(template_obj.render(context))
