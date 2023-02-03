from . import views
from django.urls import path

app_name = 'quote_site'
urlpatterns = [
    path("", views.index, name="index"),
    path('<int:id>/', views.author_detail, name='author_detail'),
]
