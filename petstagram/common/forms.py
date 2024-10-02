from django import forms

from petstagram.common.models import PhotoComment


class CommentPostForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ['comment_text', ]
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...',
                }
            ),
        }


class SearchForm(forms.Form):
    pet_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by pet name...'
            }
        )
    )


