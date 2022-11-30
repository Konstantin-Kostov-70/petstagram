from django.shortcuts import render, redirect

from petstagram.common.forms import CommentPostForm
from petstagram.core.utils import apply_likes_count, apply_user_liked_photo
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet
from petstagram.pets.utils import get_pet_by_name_and_username


def pet_details(request, username, pet_slug):

    pet = get_pet_by_name_and_username(pet_slug, username)
    photos = [apply_likes_count(photo) for photo in pet.photo_set.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]

    context = {
        'pet': pet,
        'photos_count': pet.photo_set.count(),
        'pet_photos': photos,
        'comment_form': CommentPostForm(),
    }
    return render(request, 'pet-details-page.html', context)


def add_pet(request):
    if request.method == 'GET':
        form = PetCreateForm()
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()

            return redirect('profile-details', pk=request.user.pk)
    context = {
        'form': form,
    }
    return render(request, 'pet-add-page.html', context)


def pet_edit(request, username, pet_slug):
    # TODO use username when auth
    pet = Pet.objects.filter(slug=pet_slug).get()
    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username=username, pet_slug=pet_slug)
    context = {
        'form': form,
        'username': username,
        'pet_slug': pet_slug,
    }
    return render(request, 'pet-edit-page.html', context)


def pet_delete(request, username, pet_slug):
    # TODO use username when auth
    pet = Pet.objects.filter(slug=pet_slug).get()
    if request.method == 'GET':
        form = PetDeleteForm(instance=pet)
    else:
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile-details', pk=1)
    context = {
        'form': form,
        'username': username,
        'pet_slug': pet_slug,
    }
    return render(request, 'pet-delete-page.html', context)
