from django.urls import path
from .views import (
    board_post_create_view,
    board_post_detail_view,
    board_post_list_view,
    board_post_update_view,
    board_post_delete_view,
)

urlpatterns = [
    path('<str:slug>/', board_post_detail_view),
    path('<str:slug>/edit/', board_post_update_view),
    path('<str:slug>/delete/', board_post_delete_view),
    path('', board_post_list_view),
]
