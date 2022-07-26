from django.urls import path

from .views import (
    dashboard, newsletter_dashboard, newsletter_create, newsletter_detail, newsletter_update, newsletter_delete,
    NewsletterDashboardHomeView, NewsletterDashboardCreateView, NewsletterDashboardDetailView, 
    NewsletterDashboardUpdateView, NewsletterDashboardDeleteView 
    )

app_name='dashboard'

urlpatterns = [
    path('', dashboard, name='home'),
    # path('list/', newsletter_dashboard, name='list'),
    # path('create/', newsletter_create, name='create'),
    # path('detail/<int:pk>/', newsletter_detail, name='detail'),
    # path('update/<int:pk>/', newsletter_update, name='update'),
    # path('delete/<int:pk>/', newsletter_delete, name='delete'),

    path('list/', NewsletterDashboardHomeView.as_view(), name='list'),
    path('create/', NewsletterDashboardCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', NewsletterDashboardDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', NewsletterDashboardUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', NewsletterDashboardDeleteView.as_view(), name='delete'),
]