from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookSearchView, CarSearchView,sampleView, CarViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', BookSearchView.as_view(), name='book-search'),
    path('carsearch/', CarSearchView.as_view(), name='car-search'),
    path('sample/', sampleView.as_view({'get':'list'}), name='sample'),
]


