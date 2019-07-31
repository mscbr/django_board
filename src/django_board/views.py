from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from board.models import BoardPost

def home_page(request):
        my_title = "%$$#"
        qs = BoardPost.objects.all()[:5]
        context = {"title": "wilkomen to django_board", 'board_list': qs}
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
