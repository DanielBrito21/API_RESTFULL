from django.http import HttpResponse
from django.shortcuts import render
from requests import delete
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .models import Picture
from .serializers import PictureSerializer
from rest_framework.pagination import PageNumberPagination
import django_filters
from rest_framework import generics



"""
##THIS PART Was made TO POPULATE THE DATABASE
import json
import requests

API_KEY='8AqyU0ho2BcxC0pagCgHUtzgJ58dxn86Z9yRNk6A'
API_URL='https://api.nasa.gov/planetary/apod'

params={
    'api_key':API_KEY,
    'hd':'True',
    'count':100,
}

response=requests.get(API_URL,params=params)
json_data=json.loads(response.text)"""

class ResponsePagination(PageNumberPagination):
    page_query_param='p'
    page_size=10
    page_size_query_param='page_size'
    max_page_size=10

class PictureFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Picture
        fields = ['price', 'release_date']

# Create your views here.
class PictureAPIView(APIView):
    def get(self,request):
        pictures=Picture.objects.all()
        #post=
        #pagination
        #paginator=ResponsePagination()
        #results=paginator.paginate_queryset(posts,request)
        serializer=PictureSerializer(pictures,many=True)
        return Response(serializer.data)

    def post(self,request):
        
        """
        #POPULATE THE API
        for dic in json_data:
            if dic['hdurl']:
                picture=Picture(title=dic['title'],url=dic['url'],hdurl=dic['hdurl'],explanation=dic['explanation'])
                picture.save()
        """
        serializer=PictureSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PicturedetailAPIView(APIView):
    def get_object(self,id):
        try:
            return Picture.objects.get(id=id)
        except Picture.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        picture=self.get_object(id)
        serializer=PictureSerializer(picture)
        return Response(serializer.data)

    def put(self,request,id):
        picture=self.get_object(id)
        serializer=PictureSerializer(picture,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        picture=self.get_object(id)
        picture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
