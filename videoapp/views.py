from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView
from .models import VideoModel
from django.urls import reverse_lazy
# Create your views here.

class VideoList(ListView):
    template_name = "list.html"
    model = VideoModel

class VideoDelete(DeleteView):
    template_name = "delete.html"
    model = VideoModel
    success_url = reverse_lazy("list")

class VideoDetail(DetailView):
    template_name = "detail.html"
    model = VideoModel

class VideoCreate(CreateView):
    template_name = "create.html"
    model = VideoModel
    fields = ("title", "video")
    success_url = reverse_lazy("list")
    