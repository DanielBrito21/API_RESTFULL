
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from .models import Picture
from .serializers import PictureSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import mixins
from rest_framework.filters import SearchFilter,OrderingFilter


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
json_data=json.loads(response.text)
"""

class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    
    serializer_class=PictureSerializer
    queryset=Picture.objects.all()
    filter_backends=(SearchFilter,OrderingFilter)
    search_fields=('id','title','url','hdurl','explanation')

    authentication_classes=[SessionAuthentication,BasicAuthentication]
    #authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self,request):  
        return self.list(request)
    def post(self,request):         
        """
        #POPULATE THE API
        for dic in json_data:
            if dic['hdurl']:
                picture=Picture(title=dic['title'],url=dic['url'],hdurl=dic['hdurl'],explanation=dic['explanation'])
                picture.save()
        """
        return self.create(request)
    def put(self,request,id=None):
        return self.update(request,id)
    def delete(self,request,id):
        return self.destroy(request,id)
    

"""
# Create your views here.
class PictureAPIView(APIView):
    def get(self,request):
        pictures=Picture.objects.all()
        serializer=PictureSerializer(pictures,many=True)
        return Response(serializer.data)

    def post(self,request):

        serializer=PictureSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

"""
#for the use of the id
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
