from django.shortcuts import render
from .models import Contact 
from .models import Usero
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from datetime import datetime 
from django.utils import timezone


@login_required
def home(request):
    context = {
        'contacts': sorted(Contact.objects.filter(author = request.user), key = lambda u : u.name),
        'user' : request.user,
        'current_url' : request.path,
        'time' : datetime.now()
    }
    return render(request, 'contacts/home.html', context)


@login_required
def home2(request):
    context = {
        'contacts': sorted(Contact.objects.filter(author = request.user), key = lambda u : u.name),
        'user' : request.user,
        'current_url' : request.path,
        'time' : datetime.now(),
    }
    return render(request, 'contacts/home.html', context)



class ContactDetailView(DetailView):
    model = Contact

class ContactCreateView(LoginRequiredMixin,CreateView):
    model = Contact
    fields = ['name','number','relationship_type','email','info','image']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Contact
    fields = ['name','number','relationship_type','email','info','image']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    
    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.author: return True 
        return False 
    
class ContactDeleteView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView):
    model = Contact
    success_url = '/'

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.author: return True 
        return False 