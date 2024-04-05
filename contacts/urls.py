from django.urls import path
from . import views
from .views import ContactDetailView, ContactCreateView, ContactUpdateView, ContactDeleteView

urlpatterns = [
    path('', views.home, name='contacts-home'),
    path('contacts/', views.home2, name = 'contacts-home2'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name = 'contact-detail'),
    path('contact/new/', ContactCreateView.as_view(), name = 'contact-create'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name = 'contact-update'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name = 'contact-delete'),
]