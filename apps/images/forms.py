from urllib import request as Request

from django import forms
from django.core.files.base import ContentFile
from django.core.files import File
from django.utils.text import slugify


from PIL import Image as pil_image
from io import BytesIO

from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()

        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid image extensions')
        return url

    def save(self, user, force_insert=False, force_update=False, commit=True):
        image = super(ImageCreateForm, self).save(commit=False)

        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title), image_url.rsplit('.', 1)[1].lower())

        response = Request.urlopen(image_url)

        image.user = user
        image.image.save(image_name, ContentFile(response.read()), save=False)
        image.save()
        return image
