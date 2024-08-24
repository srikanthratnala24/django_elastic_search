from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
# from django_elasticsearch_dsl_drf.filter_backends.filtering import FilteringFilterBackend
# from django_elasticsearch_dsl_drf.constants import FILTER_TERMS

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from django_elasticsearch_dsl.search import Search
from rest_framework.response import Response
from rest_framework.views import APIView
from .documents import BookDocument

class BookSearchView(APIView):
    def get(self, request):
        q = request.GET.get('q')
        search = Search(index='books').query("multi_match", query=q, fields=['title', 'author'])
        response = search.execute()
        return Response(response.to_dict()['hits']['hits'])
    
class CarSearchView(APIView):
    def get(self, request):
        q = request.GET.get('q')
        search = Search(index='cars').query("multi_match", query=q, fields=['name'])
        response = search.execute()
        return Response(response.to_dict()['hits']['hits'])
