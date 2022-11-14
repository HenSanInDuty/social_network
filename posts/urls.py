from django.urls import path
from . import views
urlpatterns = [
    #Nom Nom 1 Nom
    path('',views.CreatePost.as_view(),name='create-post')
]
