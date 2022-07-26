from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage

from django.shortcuts import render

from .models import	 NewsletterUser
from .forms import NewsletterUserSingUpForm

# Create your views here.
def newsletter_signup(request):
    form = NewsletterUserSingUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Email already exists.')
        else:
            instance.save()
            messages.success(request, f'Hemos enviado un correo electronico a {instance.email}, abrelo para continuar con su entrenamiento')
            # correo electronico
            subject = 'Libro de cocina'
            from_email=settings.EMAIL_HOST_USER
            to_email= [instance.email]

            html_template='newsletters/email_templates/welcome.html'
            html_message=render_to_string(html_template)
            message=EmailMessage(subject, html_message, from_email, to_email)
            message.content_subtype='html'
            message.send()

    context={
        'form':form,
    }

    return render(request, 'start_here.html', context)


def newsletter_unsubscribe(request):
    form = NewsletterUserSingUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.succes(request, f'El correo {instance.email} ha sido eliminado')
        else:
            print('Email not found.')
            messages.warning(request, 'Email not found.')

    context={
        'form':form,
    }

    return render(request, 'unsubscribe.html', context)
