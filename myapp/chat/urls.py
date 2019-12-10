from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:conversation_id>/', views.detail, name='detail'),
    # path('<int:conversation_id>/results', views.results, name='results'),
    path('<int:conversation_id>/send/', views.send, name='send'),
    path('new_conversation/', views.new_conversation, name='new_conversation')
]
