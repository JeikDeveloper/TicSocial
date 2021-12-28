from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.TaskAPiView.as_view())
]