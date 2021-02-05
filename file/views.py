from account.models import CustomUser
from django.shortcuts import redirect, render
from .models import UploadGroup, UploadedFile
import requests
from django.contrib.auth.decorators import login_required
from excel_response import ExcelResponse
# Create your views here.


def get_md5_hash(file):
    url = 'https://api.hashify.net/hash/md5/hex'
    headers = {'Content-type': 'text/plain'}
    # file_0 = open(file, 'rb')
    r = requests.post(url, headers=headers, data=file)
    res = r.json()
    return res.get('Digest')


@login_required(login_url='/auth/login/')
def home(request):
    if request.method == 'POST':
        user_obj = CustomUser.objects.get(pk=request.user.id)
        upload_group = UploadGroup.objects.create(user=user_obj)

        # Get all the Form data
        file_names = request.POST.getlist('file-name')
        files = request.FILES.getlist('file')
        """Instead of the making this API call in Loop in Real App We should assign a background Task to make this in backgrounds to Improve Overall Performance"""
        for name, file_obj in zip(file_names, files):
            UploadedFile.objects.create(
                user_group=upload_group, file_obj=file_obj, file_title=name, md5_hash=get_md5_hash(file_obj))
        return redirect('results', upload_group.id)

    return render(request, 'file/home.html')


@login_required(login_url='/auth/login/')
def results(request, id):
    if request.method == "POST":
        upload_files = UploadedFile.objects.filter(user_group__id=id)
        return ExcelResponse(upload_files)

    upload_files = UploadedFile.objects.filter(user_group__id=id)
    user_group_id = id
    context = {'upload_files': upload_files, 'user_group_id': user_group_id}
    return render(request, 'file/results.html', context)


@login_required(login_url='/auth/login/')
def all_upload_groups(request):
    upload_groups = UploadGroup.objects.filter(user__id=request.user.id)
    upload_groups_count = UploadGroup.objects.filter(
        user__id=request.user.id).count()
    context = {'upload_groups': upload_groups,
               'upload_groups_count': upload_groups_count}
    return render(request, 'file/all_groups.html', context)
