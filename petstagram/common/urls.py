from django.urls import path

from petstagram.common import views
from petstagram.common.views import like_photo,  add_comment

urlpatterns = [
    path('', views.index, name='index'),
    path('like/<int:photo_id>/', like_photo, name='like photo'),
    path('comment/<int:photo_id>', add_comment, name='add comment'),

]
