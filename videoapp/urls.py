from django.urls import path
from .views import VideoList, VideoDelete, VideoDetail, VideoCreate
urlpatterns = [
    path("list/", VideoList.as_view(), name="list"),
    path("delete/<int:pk>", VideoDelete.as_view(), name="delete"),
    path("detail/<int:pk>/", VideoDetail.as_view(), name="detail"),
    path("create/", VideoCreate.as_view(), name="create")
]