from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage

from django.shortcuts import render
from django.views.generic import View

from newsletters.models import	 NewsletterUser
from newsletters.forms import NewsletterUserSingUpForm

# Create your views here.

def home(request):
    context = {

    }
    return render(request, 'index.html', context)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, 'index.html', context)
 

    def post(self, request, *args, **kwargs):
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

        return render(request, 'index.html')


class AboutView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'about.html', context)     

class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'contact.html', context)  

    def post(self, request, *args, **kwargs):
        form = request.POST
        message_name = form.get('full_name')
        message_email= form.get('email')
        message_phone= form.get('phone')
        message = form.get('message')

        send_mail(message_name, message, message_email, ['mail@test.com'])

        messages.success(request, 'Mensaje neviado correctamente')

        context = {

        }
        return render(request, 'contact.html', context)     
