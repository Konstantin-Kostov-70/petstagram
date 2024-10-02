from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, resolve_url

from petstagram.accounts.models import AppUser
from petstagram.common.forms import CommentPostForm, SearchForm
from petstagram.common.models import PhotoLike
from petstagram.core.utils import apply_likes_count, apply_user_liked_photo
from petstagram.photos.models import Photo
# import pyperclip

UserModel = get_user_model


def index(request):
    search_form = SearchForm(request.POST)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['pet_name']

    photos = Photo.objects.all()
    users = AppUser.objects.all()
    if search_pattern:
        photos = photos.filter(tagged_pets__name__icontains=search_pattern)

    photos = [apply_likes_count(photo) for photo in photos]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'photos': photos,
        'comment_form': CommentPostForm(),
        'search_form': SearchForm(),
        'users': users
    }
    return render(request, 'home-page.html', context)


def get_user_liked_photos(photo_id, request):
    return PhotoLike.objects.filter(photo_id=photo_id, user=request.user)


def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photos(photo_id, request)

    if user_liked_photos:
        user_liked_photos.delete()
    else:
        PhotoLike.objects.create(
            photo_id=photo_id,
            user=request.user

        )

    redirect_path = request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
    return redirect(redirect_path)


# def share_photo(request, photo_id):
#     pyperclip.copy(request.META['HTTP_HOST'] + resolve_url('photo_details', photo_id))
#
#     redirect_path = request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
#     return redirect(redirect_path)


def add_comment(request, photo_id):

    photo = Photo.objects.filter(pk=photo_id).get()
    form = CommentPostForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)  # Does not persist to the database
        comment.photo = photo
        comment.user = request.user
        comment.save()

    return redirect('index')

    # return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')



