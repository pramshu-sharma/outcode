from django.urls import path
from .views import ShortenURLView, RedirectURLView

urlpatterns = [
    path('', ShortenURLView.as_view(), name='shorten-url'),
    path('<str:hash_id>/', RedirectURLView.as_view(), name='redirect-url')
]