from django.shortcuts import render
from .models import SearchQuery
from board.models import BoardPost

def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {'query': query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        board_list = BoardPost.objects.search(query)
        context['board_list'] = board_list
    return render(request, 'search/view.html', context)
