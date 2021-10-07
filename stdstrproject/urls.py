"""stdstrproject URL Configuration"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("book", views.book, name="book"),
    path("uniform", views.uniform, name="uniform"),
    path("tablet", views.tablet, name="tablet"),
    path("pdf", views.pdf, name="pdf"),
    path("laptop", views.laptop, name="laptop"),
    path("stationery", views.stationery, name="stationery"),
    path("login", views.login, name="login"),
    path("registration", views.registration, name="registration"),
    path("cart", views.cart, name="cart"),
    path("logout", views.logout, name="logout"),
    path("checkout", views.checkout, name="checkout")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
