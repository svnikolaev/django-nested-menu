from django.urls import path
from .views import page_view

app_name = 'pages'
urlpatterns = [
    path('', page_view, kwargs={'slug': 'home'}, name='home'),
    path('<path:slug>/', page_view, name='page_view'),
]
