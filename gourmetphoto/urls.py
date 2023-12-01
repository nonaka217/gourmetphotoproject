from django.urls import path
from . import views

app_name = 'gourmetphoto'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.CreatePhotoView.as_view(), name='post'),
    path('post_done', views.PostSuccessView.as_view(), name='post_done'),
    path('gourmetphoto/<int:Category>', views.CategoryView.as_view(), name = 'gourmetphotos_cat'),
    path('user-list/<int:user>', views.UserView.as_view(), name = 'user_list'),
]