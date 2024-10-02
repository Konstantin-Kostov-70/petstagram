from django.urls import path, include

from petstagram.accounts.views import SignInView, SignUpView, \
    SignOutView, UserDetailsView, DeleteUserView, UserEditView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='account_register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='profile-details'),
        path('edit/', UserEditView.as_view(), name='profile-edit'),
        path('delete/', DeleteUserView.as_view(), name='profile-delete'),
    ]))
]