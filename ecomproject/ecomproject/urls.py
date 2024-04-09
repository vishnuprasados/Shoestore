from django.urls import path

from ecomapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/',admin.site.urls),
    path("home",views.Home.as_view(),name="home"),
    path("signup",views.SignUpView.as_view(),name="signup"),
    path("productdetail/<int:id>",views.ProductDetailView.as_view(),name="productdetail"),
    path("signin",views.SignInView.as_view(),name="signin"),
    path("signout",views.SignOutView.as_view(),name="signout"),
    path("userhome",views.userhome.as_view(),name="user"),
    path("carts/<int:id>",views.CartCreateView.as_view(),name="carts"),
    path("cartlist",views.ListView.as_view(),name="list"),
    path("placeorder/<int:proid>/<int:cartid>",views.PlaceorderView.as_view(),name="order"),
    path("Cartdelete/<int:id>",views.DeleteView.as_view(),name="cart_delete"),
    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


