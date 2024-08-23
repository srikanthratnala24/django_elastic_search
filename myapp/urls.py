from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookSearchView

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/search/', BookSearchView.as_view(), name='book-search'),
]


