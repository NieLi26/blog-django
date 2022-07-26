from django.db import models
from django.urls import reverse
# Create your models here.

class NewsletterUser(models.Model):
    """Model definition for NewsletterUser."""

    # TODO: Define fields here
    email = models.EmailField('Correo',null=False, unique=True)
    date_added = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for NewsletterUser."""

        verbose_name = 'NewsletterUser'
        verbose_name_plural = 'NewsletterUsers'

    def __str__(self):
        """Unicode representation of NewsletterUser."""
        return self.email

class Newsletter(models.Model):
    """Model definition for Newsletter."""

    EMAIL_STATUS_CHOICES=(
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )

    # TODO: Define fields here
    name = models.CharField('Nombre', max_length=250)
    subject = models.CharField('Asunto', max_length=250)
    body = models.TextField(blank=True)
    email = models.ManyToManyField(NewsletterUser)
    created = models.DateTimeField('Creado', auto_now=False, auto_now_add=True)
    status = models.CharField('Status', max_length=10, choices=EMAIL_STATUS_CHOICES)

    class Meta:
        """Meta definition for Newsletter."""

        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
        ordering = ('-created',)

    def __str__(self):
        """Unicode representation of Newsletter."""
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard:detail,', args=[str(self.id)])