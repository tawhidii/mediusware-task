from datetime import datetime
from django.views import generic
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator

from product.models import Variant,Product,ProductVariant,ProductVariantPrice


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


class ProductList(generic.View):
    """ Product list View definition """
    

    def get(self, request):
        template_name = 'products/list.html'
        all_variants = ProductVariant.objects.all()
        product_with_price_and_variants = ProductVariantPrice.objects.all()
        total_products = len(product_with_price_and_variants)
        # Pagination 
        paginator = Paginator(product_with_price_and_variants,5)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        context = {
            'all_variants':all_variants,
            'products':products,
            'total_products':total_products,
        }
        return render(request,template_name,context)
        
    def post(self,request):
        all_variants = ProductVariant.objects.all()
        template_name = 'products/list.html'
        product_title = request.POST.get('product_title')
        variant = request.POST.get('variant')
        price_from = 0 if request.POST.get('price_from') == '' else float(request.POST.get('price_from'))
        price_to = 0 if request.POST.get('price_to') == '' else float(request.POST.get('price_to'))
        date = request.POST.get('date')
        print(date)
        products = ProductVariantPrice.objects.filter(
            Q(product__title__contains=product_title.rstrip())|
            Q(product_variant_one__variant_title__contains=variant)|
            Q(price__range=[price_from,price_to]) |
            Q(product__created_at=date if date else None)

        )
        total_products = len(products)
         # Pagination 
        paginator = Paginator(products,5)
        page = request.GET.get('page')
        products = paginator.get_page(page)
        context = {
            'all_variants':all_variants,
            'products':products,
            'total_products':total_products,
        }

        return render(request,template_name,context)
