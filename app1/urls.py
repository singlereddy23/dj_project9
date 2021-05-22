from django.urls import path
from app1 import views
app_name="app1"
urlpatterns = [
    path('sample2',views.sample2,name="sample2"),
]