from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Product

class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        # Обработка формы
        print("=== НОВОЕ СООБЩЕНИЕ ===")
        print("Имя:", request.POST.get('name'))
        print("Email:", request.POST.get('email'))
        print("Сообщение:", request.POST.get('message'))
        context = self.get_context_data(**kwargs)
        context['success'] = True
        return self.render_to_response(context)
