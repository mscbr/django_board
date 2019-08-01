from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

# Create your views here.
from .forms import BoardPostModelForm
from .models import BoardPost

def board_post_list_view(request):
    #list out obj / search 
    #search example
    #qs = BoardPost.objects.filter(title__icontains='title')
    qs = BoardPost.objects.all().published() #queryset - list of python obj
    if request.user.is_authenticated:
        my_qs = BoardPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'board/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

def board_post_detail_view(request, slug):
    #1 obj -> detail view
    obj = get_object_or_404(BoardPost, slug=slug)
    template_name = 'board/detail.html'
    context = {'object': obj}
    return render(request, template_name, context)

@staff_member_required() 
def board_post_update_view(request, slug): 
    obj = get_object_or_404(BoardPost, slug=slug)
    form = BoardPostModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'board/form.html'
    context = {'title': f'Update {obj.title}', 'form': form}
    return render(request, template_name, context)

#@login_required()
@staff_member_required() 
def board_post_create_view(request):
    #create objects
    form = BoardPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BoardPostModelForm()
        return redirect('/board')
    template_name = 'board/form.html'
    context = {'form': form}
    return render(request, template_name, context)

@staff_member_required() 
def board_post_delete_view(request, slug):
    obj = get_object_or_404(BoardPost, slug=slug)
    template_name = 'board/delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('/board')
    context = {'object': obj}
    return render(request, template_name, context)