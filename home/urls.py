from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('malware_viz/products_and_services',
         views.products_services, name='malware_products'),
    path('malware_viz', views.malwarehome, name='malware_viz_main'),
    path('malware_viz/joinus',
         views.malware_joinus, name='malware_viz_joinus'),
]
