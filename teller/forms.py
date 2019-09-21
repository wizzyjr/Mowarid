from django import forms

from teller.models import TellerPost

class CreateTellerForm(forms.ModelForm):

    class Meta:
        model = TellerPost
        fields = ['title', 'body', 'image']


class UpdateTellerPostForm(forms.ModelForm):

    class Meta:
        model = TellerPost
        fields = ['title', 'body', 'image']

    def save(self, commit=True):
        teller_post = self.instance
        teller_post.title = self.cleaned_data['title']
        teller_post.body = self.cleaned_data['body']

        if self.cleaned_data['image']:
            teller_post.image = self.cleaned_data['image']

        if commit:
            _post(save)
        return teller_post
