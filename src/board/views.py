from django.shortcuts import render

# Create your views here.
from .models import BoardPost



def board_post_detail_page(request, post_id):
    obj = BoardPost.objects.get(id=post_id)
    template_name = 'blog_post_detail.html'
    context = {'object': obj}

    return render(request, template_name, context)