from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .forms import BoardPostForm
from .models import BoardPost





def board_post_list_view(request):
    #list out obj / search 
    #search example
    #qs = BoardPost.objects.filter(title__icontains='title')
    qs = BoardPost.objects.all() #queryset - list of python obj
    template_name = 'board/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

def board_post_detail_view(request, slug):
    #1 obj -> detail view
    obj = get_object_or_404(BoardPost, slug=slug)
    template_name = 'board/detail.html'
    context = {'object': obj}
    return render(request, template_name, context)

def board_post_update_view(request, slug): 
    obj = get_object_or_404(BoardPost, slug=slug)
    template_name = 'board/update.html'
    context = {'object': obj, 'form': None}
    return render(request, template_name, context)

def board_post_create_view(request):
    #create objects
    form = BoardPostForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        obj = BoardPost.objects.create(**form.cleaned_data)
        form = BoardPostForm()
    template_name = 'board/form.html'
    context = {'form': form}
    return render(request, template_name, context)

def board_post_delete_view(request, slug):
    obj = get_object_or_404(BoardPost, slug=slug)
    template_name = 'board/delete.html'
    context = {'object': obj}
    return render(request, template_name, context)