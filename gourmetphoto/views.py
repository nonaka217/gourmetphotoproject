from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import GourmetphotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import GourmetphotoPost
from django.views.generic import DetailView
from django.views.generic import DeleteView

class IndexView(ListView):
    template_name = 'gourmetphoto/index.html'
    queryset = GourmetphotoPost.objects.order_by('-posted_at')
    paginate_by = 9

@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    form_class = GourmetphotoPostForm
    template_name = "gourmetphoto/post_photo.html"
    success_url = reverse_lazy('gourmetphoto:post_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
    
class PostSuccessView(TemplateView):
    template_name = 'gourmetphoto/post_success.html'

class CategoryView(ListView):
    template_name = 'gourmetphoto/index.html'
    paginate_by = 9
    
    def get_queryset(self):
        Category_id = self.kwargs['Category']
        Categories = GourmetphotoPost.objects.filter(Category=Category_id).order_by('-posted_at')
        return Categories
    
# class UserView(ListView):
    # template_name = 'gourmetphoto/index.html'
    # paginate_by = 9

    # def get_queryset(self):
        # user_id = self.kwargs['user']
        # user_list = GourmetphotoPost.objects.filter(user=user_id).order_by('-posted_at')
        # return user_list
    
class DetailView(DetailView):
    template_name = 'gourmetphoto/detail.html'
    model = GourmetphotoPost

class MypageView(ListView):
    template_name = 'gourmetphoto/mypage.html'
    paginate_by = 9
    
    def get_queryset(self):
        queryset =GourmetphotoPost.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset
    
class PhotoDeleteView(DeleteView):
    model = GourmetphotoPost
    template_name = 'gourmetphoto/photo_delete.html'
    success_url = reverse_lazy('gourmetphoto:mypage')
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
