from rest_framework import viewsets
from .models import Book, Car
from .serializers import BookSerializer, CarSerializer
# from django_elasticsearch_dsl_drf.filter_backends.filtering import FilteringFilterBackend
# from django_elasticsearch_dsl_drf.constants import FILTER_TERMS

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

from django_elasticsearch_dsl.search import Search
from rest_framework.response import Response
from rest_framework.views import APIView
from .documents import BookDocument
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class BookSearchView(APIView):
    book_search_param = openapi.Parameter('q',in_=openapi.IN_QUERY,description='q',type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[book_search_param])
    def get(self, request):
        print('++++++++++++++0',self.request.auth)
        q = request.GET.get('q')
        search = Search(index='books').query("multi_match", query=q, fields=['title', 'author'])
        response = search.execute()
        return Response(response.to_dict()['hits']['hits'])
    
class CarSearchView(APIView):
    car_search_param = openapi.Parameter('q',in_=openapi.IN_QUERY,description='q',type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[car_search_param])
    def get(self, request):
        q = request.GET.get('q')
        search = Search(index='cars').query("multi_match", query=q, fields=['name'])
        response = search.execute()
        return Response(response.to_dict()['hits']['hits'])

class sampleView(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        print(self.request.user)
        return Book.objects.all()