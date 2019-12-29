from django.urls import path

from . import views

urlpatterns = [
    path('',views.Homepageview.as_view(),name='home'),
    path('about/',views.AboutpageView.as_view(),name='about'),
    path('contact/',views.Contact.as_view(),name='contact')
]