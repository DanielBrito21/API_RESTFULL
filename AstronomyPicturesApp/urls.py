from django.urls import path
from .views import PictureAPIView, PicturedetailAPIView

urlpatterns=[
    path('',PictureAPIView.as_view()),
    path('detail/<int:id>/',PicturedetailAPIView.as_view())
]