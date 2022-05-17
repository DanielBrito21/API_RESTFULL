from django.urls import path
from .views import GenericAPIView
from .views import PicturedetailAPIView
#from .views import PictureAPIView,

urlpatterns=[
    path('<int:id>/',PicturedetailAPIView.as_view()),
    path('',GenericAPIView.as_view()),
]