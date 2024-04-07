from django.urls import path
from .views import page_view

app_name = 'pages'
urlpatterns = [
    path('<slug:slug>/', page_view, name='page_view'),
]
