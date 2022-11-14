from django.urls import path
from . import views
urlpatterns = [
    #Nom Nom 3 Nom
    path('',views.CreatePost.as_view(),name='create-post')
]
