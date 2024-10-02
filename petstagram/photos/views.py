from django.shortcuts import render, redirect

from petstagram.common.forms import CommentPostForm
from petstagram.common.views import get_user_liked_photos
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.photos.models import Photo


def photo_details(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    is_user_photos_owner = photo.user == request.user
    context = {
        'photo': photo,
        'has_user_liked_photo': get_user_liked_photos(pk, request),
        'likes_count': photo.photolike_set.count(),
        'comment_form': CommentPostForm(),
        'is_user_photos_owner': is_user_photos_owner
    }
    return render(request, 'photo-details-page.html', context)


def add_photos(request):
    if request.method == 'GET':
        form = PhotoCreateForm()
    else:
        form = PhotoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            current_photo = form.save(commit=False)
            current_photo.user = request.user
            current_photo.save()
            form.save_m2m()

            return redirect('photo_details', pk=current_photo.pk)
    context = {
        'form': form,
    }
    return render(request, 'photo-add-page.html', context)


def edit_photos(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = PhotoEditForm(instance=photo)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save()
            return redirect('photo_details', pk=photo.pk)
    context = {
        'form': form,
        'photo': photo,
    }
    return render(request, 'photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.filter(pk=pk).get()
    photo.delete()
    return redirect('index')
