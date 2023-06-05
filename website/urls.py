from django.urls import include, path

from . import views
from .orders.views import order_handler



from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name='index'),
    path('order', views.order, name='order'),  
    path('order_process', views.order_process, name='order_process'),  
    path('profile', views.profile, name='profile'),  
    path('supplier_profile', views.supplier_profile, name='supplier_profile'),  

    path('api/order/<int:order_id>/<str:command>', order_handler, name='order_handler'),

    path('accounts/', include('website.auth.urls')),
    
    path('vue_test', TemplateView.as_view(template_name="vue_test.html"), name="app")


]
