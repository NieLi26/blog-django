from django import forms

from .models import NewsletterUser, Newsletter

class NewsletterUserSingUpForm(forms.ModelForm):
    """Form definition for NewsLetterUserSingUp."""

    class Meta:
        """Meta definition for NewsLetterUserSingUpform."""

        model = NewsletterUser
        fields = ('email',)

class NewsletterCreationForm(forms.ModelForm):
    """Form definition for NewsLetterCreation."""

    class Meta:
        """Meta definition for NewsLetterCreationform."""

        model = Newsletter
        fields = ('name','subject', 'body', 'email', 'status')

