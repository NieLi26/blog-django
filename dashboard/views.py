from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from django.conf import settings
from django.core.mail import send_mail

from newsletters.models import Newsletter
from newsletters.forms import NewsletterCreationForm

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/index.html')

def newsletter_dashboard(request):
        newsletters = Newsletter.objects.all()

        context = {
            'newsletters': newsletters
        }

        return render(request, 'dashboard/list.html', context)


def newsletter_create(request):
    form = NewsletterCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instace = form.save()
            newsletter=Newsletter.objects.get(id=instace.id)

            if newsletter.status == 'Published':
                subject = newsletter.subject
                message = newsletter.body
                from_email = settings.EMAIL_HOST_USER
                for email in newsletter.email.all():
                    send_mail(subject, message, from_email, [email], True)
            return redirect('dashboard:list')

    context = {
        'form': form
    }
    return render(request, 'dashboard/create.html', context)

def newsletter_detail(request, pk):
        newsletter = get_object_or_404(Newsletter, id=pk)
        context ={
            'newsletter': newsletter
        }
        return render(request, 'dashboard/detail.html', context)

def newsletter_update(request, pk):
    newsletter = Newsletter.objects.get(id=pk)
    form = NewsletterCreationForm(request.POST or None, instance=newsletter)
    if request.method == 'POST':
        if form.is_valid():
            instace = form.save()
            newsletter=Newsletter.objects.get(id=instace.id)

            if newsletter.status == 'Published':
                subject = newsletter.subject
                message = newsletter.body
                from_email = settings.EMAIL_HOST_USER
                for email in newsletter.email.all():
                    send_mail(subject, message, from_email, [email], True)
            return redirect('dashboard:detail', pk=newsletter.id)

    context = {
        'form': form
    }
    return render(request, 'dashboard/update.html', context)

def newsletter_delete(request, pk):
    newsletter = get_object_or_404(Newsletter, id=pk)
    if request.method == 'POST':
        newsletter.delete()
        return redirect('dashboard:list')

    context = {

    }
    return render(request, 'dashboard/delete.html', context)


class NewsletterDashboardHomeView(View):

    def get(self, request, *args, **kwargs):
        newsletters = Newsletter.objects.all()

        context = {
            'newsletters': newsletters
        }

        return render(request, 'dashboard/list.html', context)

class NewsletterDashboardCreateView(View):

    def get(self, request, *args, **kwargs): 
        form = NewsletterCreationForm()
        context = {
            'form': form
        }

        return render(request, 'dashboard/create.html', context)

    def post(self, request, *args, **kwargs): 
        form = NewsletterCreationForm(request.POST or None)
        if form.is_valid():
            instace = form.save()
            newsletter=Newsletter.objects.get(id=instace.id)

            if newsletter.status == 'Published':
                subject = newsletter.subject
                message = newsletter.body
                from_email = settings.EMAIL_HOST_USER
                for email in newsletter.email.all():
                    send_mail(subject, message, from_email, [email], True)
            return redirect('dashboard:list')

class NewsletterDashboardDetailView(View):
    def get(self, request, *args, **kwargs):      
        newsletter = get_object_or_404(Newsletter, id=self.kwargs['pk'])
        context ={
            'newsletter': newsletter
        }
        return render(request, 'dashboard/detail.html', context)

class NewsletterDashboardUpdateView(View):

    def get(self, request, *args, **kwargs): 
        newsletter = Newsletter.objects.get(id=self.kwargs['pk'])
        form = NewsletterCreationForm(instance=newsletter)
        context = {
            'form': form
        }

        return render(request, 'dashboard/update.html', context)

    def post(self, request, *args, **kwargs): 
        newsletter = Newsletter.objects.get(id=self.kwargs['pk'])
        form = NewsletterCreationForm(request.POST or None, instance=newsletter)
        if form.is_valid():
            instace = form.save()
            newsletter=Newsletter.objects.get(id=instace.id)

            if newsletter.status == 'Published':
                subject = newsletter.subject
                message = newsletter.body
                from_email = settings.EMAIL_HOST_USER
                for email in newsletter.email.all():
                    send_mail(subject, message, from_email, [email], True)
            return redirect('dashboard:detail', pk=newsletter.id)

class NewsletterDashboardDeleteView(View):

    def get(self, request, *args, **kwargs): 
        context = {

        }
        return render(request, 'dashboard/delete.html', context)

    def post(self, request, *args, **kwargs): 
        newsletter = get_object_or_404(Newsletter, id=self.kwargs['pk'])
        newsletter.delete()
        return redirect('dashboard:list')

       