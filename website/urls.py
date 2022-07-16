
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('blog.html', views.blog, name="blog"),
    path('testimonial.html', views.testimonial, name="testimonial"),
    path('products.html', views.products, name="products"),
]
