from django.contrib.auth import views as auth_views, get_user_model


from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import UserCreateForm, UserLoginForm, UserEditForm

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


# 1234QWERty5678


class SignInView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'login-page.html'
    next_page = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


class UserDetailsView(views.DetailView):

    model = UserModel
    template_name = 'profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['pets_count'] = self.object.pet_set.count()

        photos = self.object.photo_set.prefetch_related('photolike_set')

        context['photos_count'] = photos.count()

        likes = sum([photo.photolike_set.count() for photo in photos.all()])
        context['likes'] = likes

        return context


class UserEditView(views.UpdateView):
    model = UserModel
    form_class = UserEditForm
    template_name = 'profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={
            'pk': self.object.pk,
        })


class DeleteUserView(views.DeleteView):
    model = UserModel
    template_name = 'profile-delete-page.html'
    success_url = reverse_lazy('index')
