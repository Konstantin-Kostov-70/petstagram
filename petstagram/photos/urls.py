from django.urls import path, include

from petstagram.photos.views import add_photos, photo_details, edit_photos, delete_photo

urlpatterns = [
    path('photos/add/', add_photos, name='add-photos'),
    path('photos/<int:pk>/', include([
        path('', photo_details, name='photo_details'),
        path('edit/', edit_photos, name='photo_edit'),
        path('delete/', delete_photo, name='delete photo'),

    ])),
]