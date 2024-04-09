from typing import Any
from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.views import View
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,DetailView,UpdateView
from ecomapp.forms import SignUpForm,SignInForm,CartForm,PlaceOrderForm

from ecomapp.models import Categories,Products,Carts,Placeorder
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages




 











# Create your views here.

class Home(TemplateView):
    template_name='index.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        products=Products.objects.all()
        context['products']=products
        return context
    


class SignUpView(CreateView):
    template_name='signup.html'
    model=User
    form_class=SignUpForm
    success_url=reverse_lazy('home')

    def from_valid(self,form):

        return super().form_valid(form)
    
class userhome(TemplateView):
    template_name='userhome.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        products=Products.objects.all()
        context['products']=products
        return context
    


class SignInView(View):

    def get(self,request,*args, **kwargs):
        form=SignInForm()
        return render(request,'signin.html',{'form':form})
    
    def post(self,request,*args, **kwargs):

        form=SignInForm(request.POST)
        if form.is_valid():

            u=form.cleaned_data.get("username")
            p=form.cleaned_data.get("password")
            user=authenticate(request,username=u,password=p)

            if user:

                messages.success(request,'login successfull')
                login(request,user)
                return redirect('user')
            
            else:
                messages.error(request,'login failed')
                return redirect('signin')


class SignOutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        return redirect('home')
    


class ProductDetailView(DetailView):
    template_name='detail.html'
    model=Products
    context_object_name='product'
    pk_url_kwarg='id'


class CartCreateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        product=Products.objects.get(id=id)
        form=CartForm()
        return render(request,'carts.html',{'products':product,'form':form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        product=Products.objects.get(id=id)
        # quantity= CartForm(request.POST)
        quantity=request.POST.get('quantity')
        Carts.objects.create(user=request.user,product_name=product,quantity=quantity)
        messages.success(request,'added to cart')
        return redirect('user')
    

class ListView(View):
    def get(self,request,*args,**kwargs):
        products=Carts.objects.filter(user=request.user).exclude(status="order-placed")
        return render(request,'cartlist.html',{'cart':products})
        
class PlaceorderView(View):
    def get(self,request,*args,**kwargs):
        form=PlaceOrderForm()
        return render(request,'placeorder.html',{'form':form})

    def post(self,request,*args,**kwargs):
        
        product_id=kwargs.get("proid") 
        cart_id=kwargs.get("cartid")
        pro=Products.objects.get(id=product_id)
        cart=Carts.objects.get(id=cart_id)
        user=request.user
        address=request.POST.get('address')
        Placeorder.objects.create(user=user,product=pro,address=address)
        cart.status='order-placed'
        cart.save()
        # request.user.carts_set.all().exclude(id=cart.id).delete()
        messages.success(request,'order-placed')
        
        return redirect('user')
    
class DeleteView(View):

    def get(self,request,*args, **kwargs):

        id =kwargs.get("id")

        data=Carts.objects.get(id=id)
        data.delete()

        return redirect('list')
        

    





    



