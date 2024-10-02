from django.contrib import admin

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date_of_publication', 'pets')

    @staticmethod
    def pets(current_photo_object):
        tagged_pets = current_photo_object.tagged_pets.all()
        if tagged_pets:
            return ', '.join([pet.name for pet in tagged_pets])
        return 'no pets'

