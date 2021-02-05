from account.models import CustomUser
from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.


class UploadGroup(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name=_(
        "User"), on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class UploadedFile(models.Model):
    user_group = models.ForeignKey(UploadGroup, verbose_name=_(
        "Upload Group"), on_delete=models.CASCADE)
    file_obj = models.FileField(_("File"), upload_to="Files", max_length=100)
    file_title = models.CharField(_("File Title"), max_length=255)
    md5_hash = models.CharField(_(""), max_length=50, null=True, blank=True)

    def get_img(self):
        try:
            return self.file_obj.url
        except:
            return None

    def __str__(self):
        return f'{self.file_title}'
