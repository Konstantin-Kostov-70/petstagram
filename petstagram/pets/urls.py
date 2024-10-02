from django.urls import path, include

from petstagram.pets.views import add_pet, pet_details, pet_edit, pet_delete

urlpatterns = [
    path('pets/add/', add_pet, name='add-pet-page'),
    path('pets/<str:username>/pet/<slug:pet_slug>/', include([
        path('',  pet_details, name='pet-details'),
        path('edit/',  pet_edit, name='pet-edit'),
        path('delete/',  pet_delete, name='pet-delete'),
    ])),
]