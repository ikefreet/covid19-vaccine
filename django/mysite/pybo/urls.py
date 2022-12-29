from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('question/create/', views.question_create, name='question_create'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('reservation/', views.reservation, name='reservation'),
    path('reservation_delete/', views.reservation_delete, name='reservation_delete'),
    path('reservation_check/', views.reservation_check, name='reservation_check'), 
]
