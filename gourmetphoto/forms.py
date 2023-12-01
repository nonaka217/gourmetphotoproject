from django.forms import ModelForm
from .models import GourmetphotoPost

class GourmetphotoPostForm(ModelForm):
    class Meta:
        model = GourmetphotoPost
        fields = ['Category', 'title', 'comment', 'image1', 'image2']
