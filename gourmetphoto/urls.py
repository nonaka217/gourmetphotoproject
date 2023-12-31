from django.urls import path
from . import views

app_name = 'gourmetphoto'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('post/', views.CreatePhotoView.as_view(), name='post'),
    path('post_done', views.PostSuccessView.as_view(), name='post_done'),
    path('gourmetphoto/<int:Category>', views.CategoryView.as_view(), name = 'gourmetphotos_cat'),
    # path('user-list/<int:user>', views.UserView.as_view(), name = 'user_list'),
    path('photo-detail/<int:pk>', views.DetailView.as_view(), name = 'photo_detail'),
    path('mypage/', views.MypageView.as_view(), name = 'mypage'),
    path('gourmetphoto/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name = 'photo_delete'),
]
