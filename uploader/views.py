#from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import Upload


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages

from django.shortcuts import get_object_or_404


from .models import Upload, Like, Comment





'''@login_required(login_url='login')
def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = UploadForm()
    return render(request, 'uploader/upload.html', {'form': form})'''

# uploader/views.py

@login_required(login_url='login')
def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user  # ← Save uploader
            upload.save()
            return redirect('display')
    else:
        form = UploadForm()
    return render(request, 'uploader/upload.html', {'form': form})



#from django.shortcuts import get_object_or_404

@login_required(login_url='login')
def edit_upload(request, pk):
    upload = get_object_or_404(Upload, pk=pk, user=request.user)  # ← Only own uploads
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES, instance=upload)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = UploadForm(instance=upload)
    return render(request, 'uploader/edit.html', {'form': form})

@login_required(login_url='login')
def delete_upload(request, pk):
    upload = get_object_or_404(Upload, pk=pk, user=request.user)  # ← Only own uploads
    if request.method == 'POST':
        upload.delete()
        return redirect('display')
    return render(request, 'uploader/delete.html', {'upload': upload})







def display_view(request):
    uploads = Upload.objects.all().order_by('-id')
    return render(request, 'uploader/display.html', {'uploads': uploads})


def like_upload(request, upload_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to like images.")
        return redirect('display')  # Redirect to display or any page you want

    upload = get_object_or_404(Upload, id=upload_id)
    like, created = Like.objects.get_or_create(user=request.user, upload=upload)

    if not created:
        like.delete()  # Unlike if already liked

    return redirect('display')

@login_required
def add_comment(request, upload_id):
    if request.method == 'POST':
        upload = get_object_or_404(Upload, id=upload_id)
        Comment.objects.create(upload=upload, user=request.user, text=request.POST['comment'])
    return redirect('display')


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user == request.user:
        comment.delete()
    return redirect('display')  # Redirect back to display view





def home_view(request):
    return render(request, 'uploader/home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('upload')
    else:
        form = RegisterForm()
    return render(request, 'uploader/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('upload')
    else:
        form = AuthenticationForm()
    return render(request, 'uploader/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

